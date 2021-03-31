#!/usr/bin/python

import os

for file in os.listdir():
    if file.endswith('.txt'):
        new_name = os.path.splitext(file)[0] + '-renamed.txt'
        os.rename(file, new_name)
