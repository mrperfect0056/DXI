import os,sys,random

os.system('clear')

logo2 = """
\x1b[1;96m /$$$$$$$              /$$
| $$__  $$            | $$
| $$  \ $$  /$$$$$$  /$$$$$$    /$$$$$$
| $$$$$$$  /$$__  $$|_  $$_/   |____  $$
| $$__  $$| $$$$$$$$  | $$      /$$$$$$$
| $$  \ $$| $$_____/  | $$ /$$ /$$__  $$
| $$$$$$$/|  $$$$$$$  |  $$$$/|  $$$$$$$
|_______/  \_______/   \___/   \_______/
                                        """
logo3 = 'Hello I am Beta'

print logo2 + logo3
nmbr = str(random.randint(11111, 99999))
be = '\x1b[1;92mBeta-Successful'
logo1 = """ | """
k = str('1000000')
c = str('786000')
for n in range(500):
    print be +  logo1 +k+nmbr + logo1 + c
