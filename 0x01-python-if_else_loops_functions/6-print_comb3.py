#!/usr/bin/python3
for k in range(0, 8):
    for l in range(k, 10):
        if k != l:
            print("{:d}{:d}".format(k, l), end=", ")
print("89")
