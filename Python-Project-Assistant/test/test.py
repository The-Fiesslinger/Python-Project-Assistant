# #!/usr/bin/python3
# # -*- coding: iso-8859-15 -*-
# import sys
#
# argumente = ['crdir', 'crclass']
#
# for argumente in sys.argv:
#     print(argumente)
#
#
# class test:
#     def testen(self):
#         if sys.argv[1] == 'crdir':
#             print('DIR GEHT')
#         else:
#             print('crdir geht nicht')
#
#         if sys.argv[2] == 'crclass':
#             print('CLASS GEHT')
#         else:
#             print('class geht nicht')
#
# def main():
#     bla = test()
#     bla.testen()
#
#
# if __name__ == "__main__":
#     main()

#!/usr/bin/python
#
# list = ['arg1', 'arg2', 'arg3']
#
# import sys
# i = 0
# x = sys.argv[i]
#
# for x in list:
#     i = +1
#     print(x)
#

# import argparse
#
# parser = argparse.ArgumentParser()
# parser.add_argument('-o','--open-file', help='Description', required=False)
# parser.add_argument('-s','--save-file', help='Description', required=False)
#
# args = parser.parse_args()
#
# print(args.open_file)
# print(args.save_file)

# # -*- coding: utf-8 -*-
# import sys
#
#
# def namen_ausgeben(vorname, name):
#     print('ein Name ist', vorname, name)
#
#
# def main():
#     if len(sys.argv) < 3:
#         # Wird ausgeführt wenn das Programm nicht korrekt aufgerufen wurde
#         print(
#         """namen_wiedergeben.py
#         Gibt den Namen aus, der als Parameter dem Programm uebergeben wurde.
#         Funktionsweise:
#             python namen_wiedergeben.py Vorname Nachname
#         Beispiel:
#             python namen_wiedergeben.py Albert Einstein
#             Schreibt "Dein Name ist Albert Einstein" in die Konsole.
#         """)
#         sys.exit()
#
#     # Programm ausführen, das heisst, etwas Nützliches machen
#     vorname = sys.argv[1]
#     name = sys.argv[2]
#     namen_ausgeben(vorname, name)
#
#
# if __name__ == '__main__':
#     main()


#!/usr/bin/python

import sys

print(sys.argv)

liste = ['crdir', 'crclass']

print('der mit for-Schleife:')

for i in range(len(sys.argv)):
    if i == 0:
        print("Funktionsname: %s" % sys.argv[0])
    else:
        print("%d. Argument: %s" % (i,sys.argv[i]))
        if sys.argv[i] in liste:
            print('Grundstrucktur wurde angelegt')
            i = +1
        else:
            print('Grundstrucktur wurde nicht angelegt!')




