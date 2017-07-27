#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
#======================================================================================================================
#   Python Project Assistant
#   Copyright (C) 2017  Kevin Ziegler <ziegler.kevin@outlook.de>
#
#   This program is free software; you can redistribute it and/or modify it under the terms of
#   the GNU General Public License as published by the Free Software Foundation; either version
#   3 of the License, or (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
#   without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#   See the GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License along with this program;
#   if not, see <http://www.gnu.org/licenses/>.
#======================================================================================================================

import sys

from create import ProjectDIR

x = ProjectDIR()


print('Usage: python parameter.py [...] [...] [...] ....|[crDir, crClass, crRelease, crInstall]!')

class param:
    def abfrage(self):
        try:
            if CRDIR == 'crDir':
                print('Grundstrucktur wurde angelegt')
            else:
                print('Grundstrucktur wurde NICHT angelegt!')

            if CRCLASS == 'crClass':
                print('Klasse wurde angelegt')
            else:
                print('Klasse wurde NICHT angelegt!')

            if CRRELEASE == 'crRelease':
                print('Release wurde angelegt')
            else:
                print('Release wurde NICHT angelegt!')

            if CRINSTALL == 'crInstall':
                print('Installer wurde angelegt')
            else:
                print('Installer wurde NICHT angelegt!')
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

