#!/usr/bin/python3

from os import system
from sys import argv
from time import sleep


system('clear')

optionlist = [
    '--assume-yes --allow-downgrades --fix-broken --fix-missing --fix-policy --no-install-recommends --no-install-suggests --show-progress --verbose-versions',
    '--allow-insecure-repositories --list-cleanup',
]

commandlist = [
    'update {}'.format(optionlist[1]),
    'upgrade {}'.format(optionlist[0]),
    'full-upgrade {}'.format(optionlist[0]),
    'dist-upgrade {}'.format(optionlist[0]),
    'autoremove {}'.format(optionlist[0]),
    'clean',
]

if (len(argv) > 1):
    arglist = argv[1:]
    arglist.sort(reverse=True)

    for package in arglist:
        commandlist.insert(1, 'install {} {}'.format(package, optionlist[0]))


for command in commandlist:
    system('clear')
    print(command)
    print('\n')
    system('sudo apt-get {}'.format(command))
    sleep(2)
