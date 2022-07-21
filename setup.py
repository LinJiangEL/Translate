import os
import sys
import time
import platform
import shutil

if sys.platform == "win32" and "Windows" in platform.platform():
    if not os.path.exists("C:\\Windows\\bin"):
        os.makedirs("C:\\Windows\\bin")
    if not "C:\\Windows\\bin" in os.environ.get('PATH'):
        os.system('"setx /M "%path%" "%path%C:\\Windows\\bin;""')
    if not os.path.exists("C:\\Windows\\bin\\translate.exe"):
        shutil.copy("translate.exe","C:\\Windows\\bin")
    ignore = True

elif sys.platform == "linux":
    command = """
                sudo mkdir /usr/local/translate -p
                sudo mv translate.py /usr/local/translate
              """
    ignore = False
else:
    sys.exit(f"\033[31mSorry! This execute cannot run on {sys.platform} !"
             f"Your platform: {sys.platform}"
             f"SystemInformation: {platform.platform}\033[0m")

global_command: str = """
                    pip3 install -U pip setuptools wheel &&
                    pip3 install requests==2.28.1 urllib3 playsound platinfo pydes&&
                    sleep 3 &&
                    clear
        """
def main(n):
    if sys.argv[n] == 'build':
        if os.system('gcc -v'):
            sys.exit('\033[31mGCCNotFoundError:can not find any gcc compiler in your Machine PATH! Please make gcc on your system and retry it!\033[0m')
        print("Copying files, wait ... ", end='')
        os.system("sudo cc translate.c -o translate")
        os.system("sudo mv translate /usr/bin")
        os.system("sudo rm translate.c")
        print("done.")
        print("\nNow you can run 'python3 setup.py install' to install it.")
    elif sys.argv[n] == 'install':
        if not ignore:
            os.system(command)
        os.system(global_command)
        print("Installing collected packages: translate-base, TSL-SYSTEM-Frame")
        print(f"Successfully installed translate-base-5.2.7 TSL-SYSTEM-Frame-{sys.version.split(' ')[0]}")
    else:
        raise NameError(sys.argv[n], "is not defined")

try:
    main(1)
except IndexError:
    raise NameError(sys.argv[1], "is not defined")

input("\nPress Enter to exit.")
