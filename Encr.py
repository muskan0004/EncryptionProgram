import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
#  typecasting it
chars = list(chars)
key = chars.copy()
random.shuffle(key)
# print(f"chars: {chars} ")
# print(f"keys: {key}")

# ENCRYPT
pt = input("enter you message")
ct = "" # empty string
for x in pt:
    i = chars.index(x)
    ct += key[i]
print(f"Original message :{pt}")
print(f" encrypted message :{ct}")
print("  ")

# DECRYPT
ct= input("enter you message")
pt = ""
for x in ct:
    i = key.index(x)
    pt += chars[i]
print(f" encrypted message :{ct}")
print(f"Original message :{pt}")

