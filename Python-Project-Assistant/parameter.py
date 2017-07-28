#!/usr/bin/python3
# -*- coding: iso-8859-15 -*-

import sys

print('Usage: python parameter.py [...] [...] [...] ....|[crDir, crClass, crRelease, crInstall]!')

class param:
    def abfrage(self):
        try:
            if CRDIR == 'crDir':
                print('Grundstrucktur wurde angelegt')
            else:
                print('Grundstrucktur wurde nicht angelegt!')

            if CRCLASS == 'crClass':
                print('Klasse wurde angelegt')
            else:
                print('Klasse wurde nicht angelegt!')

            if CRRELEASE == 'crRelease':
                print('Release wurde angelegt')
            else:
                print('Release wurde nicht angelegt!')

            if CRINSTALL == 'crInstall':
                print('Installer wurde angelegt')
            else:
                print('Installer wurde nicht angelegt!')
        except ValueError:
            print('Fehler')

try:
    CRDIR = str(sys.argv[1])
except IndexError:
    CRDIR = None

try:
    CRCLASS = str(sys.argv[2])
except IndexError:
    CRCLASS = None

try:
    CRRELEASE = str(sys.argv[3])
except IndexError:
    CRRELEASE = None

try:
    CRINSTALL = str(sys.argv[4])
except IndexError:
    CRINSTALL = None


def main():
    create = param()
    create.abfrage()

if __name__ == "__main__":
    main()

