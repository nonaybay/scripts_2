#!/usr/bin/python3
from os import system
from sys import argv

system('clear')

servers_list = [
    'hkp://keyserver.ubuntu.com:80',
]

if len(argv) > 1:
    keys_list = argv[1:]

    for key in keys_list:
        for server in servers_list:
            system('sudo gpg --keyserver {} --recv {}'.format(server, key))
            system('sudo gpg --export --armor {} | sudo apt-key add - '.format(key))
