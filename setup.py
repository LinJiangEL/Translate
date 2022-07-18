import os
import sys
import time
import platform

if sys.platform == "win32" and "Windows" in platform.platform():
    command = """
                mkdir C:\\Windows\\bin && 
                setx PATH "%PATH%;C:\\Windows\\bin" /M && 
                move /Y translate.exe C:\\Windows\\bin 
              """
elif sys.platform == "linux":
    command = """
                sudo mkdir /usr/local/translate -p
                sudo mv translate.py /usr/local/translate
                sudo mv translate /usr/bin && 
                sudo chmod 777 /usr/bin/translate
              """
else:
    sys.exit(f"\033[31mSorry! This execute cannot run on {sys.platform} !"
             f"Your platform: {sys.platform}"
             f"SystemInformation: {platform.platform}\033[0m")

global_command: str = """
                    pip3 install -U pip setuptools wheel &&
                    pip3 install requests==2.28.1 &&
                    pip3 install urllib3 &&
                    pip3 install playsound &&
                    pip3 install platinfo &&
                    pip3 install pydes
                    sleep 3 &&
                    clear
        """
if sys.argv[2] == 'build':
    print("Copying files, wait ... ", end='')
    time.sleep(3)
    print("done.")
    print("\nNow you can run 'python3 setup.py install' to install it.\n")
elif sys.argv[2] == 'install':
    print("Copying files, wait ... ", end='')
    time.sleep(3)
    print("done.\n\n")
    os.system(command)
    os.system(global_command)
    print("Installing collected packages: translate-base, TSL-SYSTEM-Frame")
    print(f"Successfully installed translate-base-5.2.7 TSL-SYSTEM-Frame-{sys.version.split(' ')[0]}")
else:
    raise NameError(sys.argv[2],"is not defined")
input("\nPress Enter to exit")
