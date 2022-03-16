#from django.test import TestCase
import os
# Create your tests here.
def binConvert(n):
    bin = []
    while(n > 0):
        bin.append(n%2)
        n = int(n/2)

    # bin = bin.reverse()
    while(len(bin)<32):
        bin.insert(0,0)
    return bin
def decConvert(n):
    i=0
    sum = 0
    n = int(n)
    while(n>0):
        rem = n%10
        sum += rem*(pow(2,i))
        i+=1
        n = int(n/10)
    return sum
def compliment(n):
    for i in range(len(n)):
        if n[i] ==0:
            n[i] = 1
        else:
            n[i] = 0
    return n
def lonelyinteger(a):
   for i in a:
       bin_no = binConvert(i)
       bin_no.reverse()
       comp_bin = compliment(bin_no)
       comp_bin = int("".join(map(str, comp_bin)))
       dec = decConvert(comp_bin)
       print(dec)


if __name__ == '__main__':
    a = [0]
    lonelyinteger(a)

