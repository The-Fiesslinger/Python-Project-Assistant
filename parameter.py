#!/usr/bin/python3
# -*- coding: iso-8859-15 -*-

import sys

print('Usage: python parameter.py [...] [...] [...] ....|[crDir, crClass, crRelease, crInstall]!')

CRDIR = sys.argv
CRCLASS = sys.argv
CRRELEASE = sys.argv
CRINSTALL = sys.argv


class param:
    def abfrage(self):
        try:
            if CRDIR[1] == 'crDir':
                print('Grundstrucktur wurde angelegt')

            else:
                print('Grundstrucktur wurde nicht angelegt!')

            if CRCLASS[2] == 'crClass':
                print('Klasse wurde angelegt')
            else:
                print('Klasse wurde nicht angelegt!')

            if CRRELEASE[3] == 'crRelease':
                print('Release wurde angelegt')
            else:
                print('Release wurde nicht angelegt!')

            if CRINSTALL[4] == 'crInstall':
                print('Installer wurde angelegt')
            else:
                print('Installer wurde nicht angelegt!')
        except ValueError:
            print('Fehler')

def main():
    create = param()
    create.abfrage()

if __name__ == "__main__":
    main()

