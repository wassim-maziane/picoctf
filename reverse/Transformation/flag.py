#!/usr/bin/python3
file = open('enc', 'r').read()
flag = ''
for character in file:
    flag += chr(ord(character) >> 8)
    flag += chr(ord(character) & 127)
print(flag)
