#!/usr/bin/python3
#-*- coding:utf-8 -*-

from random import randint
from string import ascii_letters, digits
from sys import argv

def main():
    LEN = 20
    if len(argv) > 1:
        try:
            LEN = int(argv[1])
        except:
            print("Аргумент командной строки должен быть в целочисленном формате")
            return
    st = ascii_letters + digits
    ln = len(st)-1
    result = "".join(st[randint(0, ln)] for x in range(LEN))
    print(result)

if __name__ == "__main__":
    main()
