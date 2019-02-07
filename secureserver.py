import socket
import hashlib
import os
import itertools
import threading
import time
import sysimport Crypto.Cipher.AES as AES
from Crypto.PublicKey import RSA
from CryptoPlus.Cipher import IDEA

host = input("Server Address -> ")
port = int(input("Port -> "))

check = False