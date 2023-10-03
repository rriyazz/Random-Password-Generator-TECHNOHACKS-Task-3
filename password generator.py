import string
import random

pwdLen = int(input("Enter password length :  "))
s1 = string.ascii_lowercase
s2 = string.ascii_uppercase
s3 = string.punctuation
s4 = string.digits

s = []
s.extend(s1)
s.extend(s2)
s.extend(s3)
s.extend(s4)

random.shuffle(s)
print("".join(s[0:pwdLen]))
