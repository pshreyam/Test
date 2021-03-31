#!/usr/bin/python

from datetime import datetime
import time

for i in range(10):
    date = datetime.now().strftime('%H:%M:%s')
    filename = date + '.txt'
    
    with open(filename, 'w') as f:
        f.write(date)

    print(f'{filename} written!')

    time.sleep(1)
