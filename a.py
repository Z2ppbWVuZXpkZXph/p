import os, sys, time
from sympy.crypto.crypto import encipher_shift, decipher_shift

GL = "\033[96;1m"
BB = "\033[34;1m"
YY = "\033[33;1m"
GG = "\033[32;1m"
WW = "\033[0;1m"
RR = "\033[31;1m"
CC = "\033[36;1m"
B = "\033[34m"
Y = "\033[33;1m"
G = "\033[32m"
W = "\033[0;1m"
R = "\033[31m"
C = "\033[36;1m"
M = "\033[35;1m"

def false():
        sutil(RR+"Vuelve a intentar!")
        os.system("sleep 1")
        os.system("clear")
        print (RR+"            CIPHER VTA")
        op()

def op():
        os.system("sleep 1")
        print (CC+"\n¿Que es lo que quieres hacer ahora mismo?")
        print (YY+"1) " + BB+"Cifrar\n" + YY +"2) " + BB+"Descifrar\n" + YY+"3) " + BB+"Salir\n")
        try:
                ca = int(input(GG+"\nEscoge una opcion: " + WW))
                if ca == 1:
                        cipher()
                elif ca == 2:
                        decipher()
                elif ca == 3:
                        skip()
                else:
                        false()
        except ValueError:
                sutil(RR+"Vuelve a poner los valores, esta vez revisalos\nmejor!...")
                os.system("sleep 1;clear")
                op()

def decipher():
        print (RR+"\n             Descifrador de frases")
        ba = input(GG+"Escribe la frase para descifrar\n>>> " + WW)
        bk = int(input(GG+"Escribe la llave: " + WW))
        bc = decipher_shift(ba, bk)
        print (RR+"\nPalabra descifrada!\n>>> " + WW, bc)
        op()

def cipher():
        print (RR+"\n             Cifrador de Mensajes")
        aa = input(GG+"Escribe la frase\n>>> " + WW)
        ak = int(input(GG+"Escribe la llave: " + WW))
        ac = encipher_shift(aa, ak)
        print (RR+"\nFrase cifrada!\n>>> " + WW, ac)
        op()

def skip():
        sutil(M+"\nSaliendo del programa... ")
        os.system("sleep 1;clear;figlet Valletta")

def sutil(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(12. / 150)

os.system("clear")
print (RR+"            CIPHER VTA")
print (CC+"\nQue es lo que deseas hacer?")
print (YY+"1) " + BB+"Cifrar\n" + YY +"2) " + BB+"Descifrar\n" + YY+"3) " + BB+"Salir\n")
try:
        rp = int(input(GG+"Escoje una opcion: " + WW))

        if rp == 1:
                cipher()
        elif rp == 2:
                decipher()
        elif rp == 3:
                skip()
        else:
                false()

except ValueError:
        sutil(RR+"Vuelve a poner los valores, esta vez revisalos\nmejor!...")
        os.system("sleep 1;clear")
        op()
