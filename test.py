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

list = ['arg1', 'arg2', 'arg3']

import sys
i = 0
x = sys.argv[i]

for x in list:
    i = +1
    print(x)

