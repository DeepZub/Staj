import rpyc
import math
conn=rpyc.classic.connect("localhost")
conn.execute('import math')

def piSayisiIleCarp(x):
    print(x*math.pi)

def ikiSayiCarp(sayi1,sayi2):
    print("sayi1*sayi2="+str(sayi1*sayi2))


fn=conn.teleport(piSayisiIleCarp)
fn(3)

sayi1=4
sayi2=10
cn=conn.teleport(ikiSayiCarp)
cn(sayi1,sayi2)


