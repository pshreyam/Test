#!/usr/bin/python

import os

for file in os.listdir():
    if file.endswith('.txt'):
        os.remove(file)
