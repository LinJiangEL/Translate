import os
import shutil
import sys
import json
import urllib
from urllib import request, parse
import requests
import playsound

__author__ = "XV101"
__version__ = "5.2.7"

os.system("uname -a")

if not os.path.exists("/usr/local/translate/dict.txt"):
    with open("/usr/local/translate/dict.txt", "w") as f:
        f.write("")
else:
    pass


class Youdao:
    def __init__(self, type=0, word='hello'):
        word = word.lower()
        self._type = type
        self._word = word

        self._dirRoot = os.path.dirname(os.path.abspath(__file__))
        if self._type == 0:
            self._dirSpeech = os.path.join(self._dirRoot, 'Speech_US')
        elif self._type == 1:
            self._dirSpeech = os.path.join(self._dirRoot, 'Speech_EN')

        if not os.path.exists('/usr/local/translate/Speech_US'):
            os.makedirs('/usr/local/translate/Speech_US')
        if not os.path.exists('/usr/local/translate/Speech_EN'):
            os.makedirs('/usr/local/translate/Speech_EN')

    def setAccent(self, type=0):
        self._type = type

        if self._type == 0:
            self._dirSpeech = os.path.join(self._dirRoot, 'Speech_US')
        elif self._type == 1:
            self._dirSpeech = os.path.join(self._dirRoot, 'Speech_EN')

    def getAccent(self):
        return self._type

    def download(self, word):
        word = word.lower()
        tmp = self._getWordMp3FilePath(word)
        if tmp is None:
            print("")
            self._getURL()
            print('No exist %s.mp3 file\nURL:\n' % word, self._url, '\nWill download to:\n', self._filePath)
            audiof = requests.get(self._url)
            with open(self._filePath, 'wb') as af:
                af.write(audiof.content)
            print("")
            print('Successfully download %s.mp3' % self._word)
            print("")
        else:
            print("")
            print('Existed %s.mp3, so ignore response.' % self._word)
            print("")

        return self._filePath

    @staticmethod
    def play(word, audiotype):
        global audiofile, audiofiles
        if audiotype == 'US':
            audiofile = '/usr/local/translate/Speech_US/' + word + '.mp3'
        elif audiotype == 'EN':
            audiofile = '/usr/local/translate/Speech_EN/' + word + '.mp3'
        else:
            audiofiles = ['/usr/local/translate/Speech_US/' + word + '.mp3',
                          '/usr/local/translate/Speech_EN/' + word + '.mp3']
        playsound.playsound(audiofile)

    def _getURL(self):
        self._url = r'http://dict.youdao.com/dictvoice?type=' + str(self._type) + r'&audio=' + self._word

    def _getWordMp3FilePath(self, word):
        word = word.lower()
        self._word = word
        self._fileName = self._word + '.mp3'
        self._filePath = os.path.join(self._dirSpeech, self._fileName)

        if os.path.exists(self._filePath):
            return self._filePath
        else:
            return None


def translate(word):
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'

    key = {
        'type': "AUTO",
        'i': word,
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "ue": "UTF-8",
        "action": "FY_BY_CLICKBUTTON",
        "typoResult": "true"
    }

    response = requests.post(url, data=key)

    if response.status_code == 200:
        return response.text
    else:
        print("Cannot import the Translate API!")
        return None


def get_reuslt(repsonse):
    result = json.loads(repsonse)
    print("")
    print("Input : %s" % result['translateResult'][0][0]['src'])
    print("Result : %s" % result['translateResult'][0][0]['tgt'])
    ra = open("/usr/local/translate/dict.txt", "r").readlines()
    a = open("/usr/local/translate/dict.txt", "a+")
    wordinfo = '{"link":"youdao","' + result['translateResult'][0][0]['src'] + \
               '":"' + result['translateResult'][0][0]['tgt'] + '"}'
    b = []
    for i in ra:
        b.append("".join(i.split('}')[0] + '}'))
    if wordinfo in b:
        print("")
        print("\033[33mWordResultWarning:word '" +
              result['translateResult'][0][0]['src'] +
              "' is existing！System will ignore response！\033[0m"
              )
    elif str(result['translateResult'][0][0]['src']) == str(result['translateResult'][0][0]['tgt']):
        print("")
        print("\033[33mWordResultWarning:word '" +
              result['translateResult'][0][0]['src'] +
              "' is as the same as its result！System will ignore response！\033[0m"
              )
    else:
        a.write(wordinfo)
        a.write("\n")
        a.close()
        print("")
        print("\033[32mWordResultInfo:word '" +
              result['translateResult'][0][0]['src'] +
              "' has written into dictionary successfully！\033[0m"
              )
    print("")


def fanyi(keyword):
    base_url = 'https://fanyi.baidu.com/sug'

    data = {
        'kw': keyword
    }

    data = parse.urlencode(data)

    header = {
        "User-Agent": "mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
    }

    req = request.Request(url=base_url, data=bytes(data, encoding='utf-8'), headers=header)
    res = request.urlopen(req)
    str_json = res.read().decode('utf-8')
    myjson = json.loads(str_json)
    info = myjson['data'][0]['v']
    print("")
    print("Input :", keyword)
    print("Result :", info)
    ra = open("/usr/local/translate/dict.txt", "r").readlines()
    a = open("/usr/local/translate/dict.txt", "a+")
    wordinfo = '{"' + keyword + '":"' + info + '"}'
    b = []
    for i in ra:
        b.append("".join(i.split('}')[0] + '}'))
    if wordinfo in b:
        print("")
        print("\033[33mWordResultWarning:word '" + keyword + "' is existing！System will ignore response！\033[0m")
    else:
        a.write(wordinfo)
        a.write("\n")
        a.close()
        print("")
        print("\033[32mWordResultInfo:word '" + keyword + "' has written into dictionary successfully！\033[0m")

    print("")


def main():
    try:
        print("")
        print("\033[36m--------------------TSL Translate System--------------------")
        print("")
        print("                        \033[32mMade by XV101\033[0m")
        print("")
        tran_choice = input("Choice one to continue：[ common/senior/reader ] ")
        print("")
        if tran_choice == "common":
            for i in range(10):
                print("Input the word which you want to translate.")
                word = input('Input：')
                if word == "@SYSTEM exit":
                    print("")
                    print("\033[33mUserWarning:the system exited correctly!\033[0m")
                    input('\nPlease press Enter to exit.')
                    break
                elif word == "@SYSTEM back":
                    os.system("clear")
                    print("\033[33mUserWarning:user return main program.\033[0m")
                    main()
                elif word == "@SYSTEM clean":
                    shutil.rmtree('/usr/local/translate/Speech_US', ignore_errors=True)
                    shutil.rmtree('/usr/local/translate/Speech_EN', ignore_errors=True)
                    os.makedirs('/usr/local/translate/Speech_US')
                    os.makedirs('/usr/local/translate/Speech_EN')
                else:
                    list_trans = translate(word)
                    get_reuslt(list_trans)
        elif tran_choice == "senior":
            while True:
                print("Input the word which you want to translate.")
                word = input('Input：')
                if word == '@SYSTEM exit':
                    print("")
                    print("\033[33mUserWarning:the system exited correctly!\033[0m")
                    input('\nPlease press Enter to exit.')
                    break
                elif word == "@SYSTEM back":
                    os.system("clear")
                    print("\033[33mUserWarning:user return main program.\033[0m")
                    main()
                else:
                    try:
                        fanyi(word)
                    except IndexError:
                        print("")
                        print(
                            "\033[31mWordsNotFoundError:cannot find '{}' from the api "
                            "'https://api.explorerlab.io/development/translate/senior.php'!"
                            " Please check your input-word and try again!\033[0m".format(word)
                        )
                        input('\nPlease press Enter to exit.')
                        sys.exit()
        elif tran_choice == "reader":
            while True:
                print("Input the word which you want to listen.")
                word = input('Input：')
                if word == '@SYSTEM exit':
                    print("")
                    print("\033[33mUserWarning:the system exited correctly!\033[0m")
                    input('\nPlease press Enter to exit.')
                    break
                elif word == "@SYSTEM back":
                    os.system("clear")
                    print("\033[33mUserWarning:user return main program.\033[0m")
                    main()
                else:
                    sp = Youdao()
                    en_us = input("Please input audio standard [ English[en]/American[us]/All[en_us] ]：")
                    if en_us == "us":
                        sp.setAccent(0)
                        audiotype = 'US'
                        try:
                            sp.download(word)
                            sp.play(word, audiotype)
                        except urllib.error.URLError:
                            print(
                                "\033[31mConnectError:cannot connect 225.161.42.73:443! "
                                "Please check your network and try again!\033[0m"
                            )
                            input('\nPlease press Enter to exit.')
                    elif en_us == "en":
                        sp.setAccent(1)
                        audiotype = 'EN'
                        try:
                            sp.download(word)
                            sp.play(word, audiotype)
                        except urllib.error.URLError:
                            print(
                                "\033[31mConnectError:cannot connect 225.161.42.73:443! "
                                "Please check your network and try again!\033[0m"
                            )
                            input('\nPlease press Enter to exit.')
                    elif en_us == "en_us":
                        try:
                            sp.setAccent(0)
                            sp.download(word)
                            sp.setAccent(1)
                            sp.download(word)
                            audiotype = 'US_EN'
                            try:
                                sp.play(word, audiotype)
                            except urllib.error.URLError:
                                print(
                                    "\033[31mConnectError:cannot connect 225.161.42.73:443! "
                                    "Please check your network and try again!\033[0m"
                                )
                                input('\nPlease press Enter to exit.')
                        except urllib.error.URLError:
                            print(
                                "\033[31mConnectError:cannot connect 225.161.42.73:443!"
                                " Please check your network and try again!\033[0m"
                            )
                            input('\nPlease press Enter to exit.')
                        continue
                    else:
                        print("\033[31mSystemError:System wrong!\033[0m")
                        input('\nPlease press Enter to exit.')
                        sys.exit()

        else:
            print("\033[31mAPINotFoundError:cannot found this TSL-API! "
                  "Please make the name correctly and try again!\033[0m"
                  )
            input('\nPlease press Enter to exit.')
            sys.exit()
    except KeyboardInterrupt:
        print("")
        print("\033[31mUserError:user cancelled this operation!\033[0m")
        input('\nPlease press Enter to exit.')
    except json.decoder.JSONDecodeError:
        print("")
        print("\033[31mValueError:the value '\033[0m\033[7m \033[0m\033[31m' cannot be identified!\033[0m")
        print("\033[31mValueError:please press Enter before you enter a word or a sentence!\033[0m")
        input('\nPlease press Enter to exit.')
    except KeyError:
        print("")
        print("\033[31mValueError:value 'keyword' has no '\033[0m\033[7m \033[0m\033[31m'!\033[0m")
        print("\033[31mValueError:please press Enter before you enter a word or a sentence!\033[0m")
        input('\nPlease press Enter to exit.')
    except requests.exceptions.ConnectionError:
        print("")
        print(
            "\033[31mConnectError:cannot connect the phphost "
            "'https://api.explorerlab.io/development/translate/common.php'! "
            "Please check the network and try again!\033[0m"
        )
        input('\nPlease press Enter to exit.')
    except urllib.error.URLError:
        print("")
        print(
            "\033[31mConnectError:cannot connect the phphost "
            "'https://api.explorerlab.io/development/translate/senior.php'! "
            "Please check the network and try again!\033[0m"
        )
        input('\nPlease press Enter to exit.')


main()
