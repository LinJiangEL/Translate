a
    +�b"  �                	   @   s6  U d dl Z d dlZd dlZd dlZejdkr>de�� v r>dZn4ejdkrNdZn$e�dej� dej� d	ej� d
�� dZeed< ej	d dkr�e
ddd� e�d� e
d� e
d� nvej	d dk�re
ddd� e�d� e
d� e �e� e �e� e
d� e
dej�d�d  � �� neej	d d��ed� dS )�    NZwin32ZWindowsz�
                mkdir C:\Windows\bin && 
                setx PATH "%PATH%;C:\Windows\bin" /M && 
                move /Y translate.exe C:\Windows\bin 
              Zlinuxz�
                sudo mkdir /usr/local/translate -p
                sudo mv translate.py /usr/local/translate
                sudo mv translate /usr/bin && 
                sudo chmod 777 /usr/bin/translate
              z'[31mSorry! This execute cannot run on z !Your platform: zSystemInformation: z[0maa  
                    pip3 install -U pip setuptools wheel &&
                    pip3 install requests==2.28.1 &&
                    pip3 install urllib3 &&
                    pip3 install playsound &&
                    pip3 install platinfo &&
                    pip3 install pydes
                    sleep 3 &&
                    clear
        �global_command�   �buildzCopying files, wait ... � )�end�   zdone.z;
Now you can run 'python3 setup.py install' to install it.
Zinstallzdone.

z?Installing collected packages: translate-base, TSL-SYSTEM-Framez=Successfully installed translate-base-5.2.7 TSL-SYSTEM-Frame-� zis not definedz
Press Enter to exit)�os�sys�time�platformZcommand�exitr   �str�__annotations__�argv�print�sleep�system�version�split�	NameError�input� r   r   �setup.py�<module>   s8   

��






