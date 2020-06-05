#!/usr/bin/python3
"""Made by https://github.com/CyberDemon-crypto"""
import os
from random import randint


def create():
    os.system('ifconfig')
    ip = input("Find there your device's IP: ")
    port = randint(0, 65535)
    os.system('clear')
    print(f'\u001b[0mLocal port opened. IP = \u001b[32m{ip}\u001b[0m, Port = \u001b[32m{port}\u001b[0m')
    print('Connect to P2P - \u001b[32mnc {IP} {PORT}\u001b[0m')
    print('Exit - \u001b[32mCtrl + C\u001b[0m')
    print('\u001b[35m-----------------------------\u001b[0m')
    os.system(f'nc -l -p {port}')
    print('\u001b[2D\u001b[35m-----------------------------\u001b[0m')


def connect():
    ip = input("IP: ")
    port = input('Open Port: ')
    os.system('clear')
    print(f'IP = \u001b[32m{ip}\u001b[0m, Port = \u001b[32m{port}\u001b[0m\nConnecting...')
    print('\u001b[35m-----------------------------\u001b[0m')
    os.system(f'nc {ip} {port}')
    print('\u001b[2D\u001b[35m-----------------------------\u001b[0m')


while True:
    print('[1]Create session\n[2]Connect to session\n[x]Exit')
    choice = input('# ')
    if choice == '1':
        create()
    elif choice == '2':
        connect()
    elif choice == 'x':
        exit('\u001b[31mDisconnected\u001b[0m')
    else:
        raise ValueError('\u001b[31mNo such option!\u001b[0m')
