#! /usr/bin/env python3

import sys

        
def calculator(num, g):

    try:
        m = int(g)
    except:
        print("Parameter Error")
        exit()
    s = m - 3500 - m*0.165
    l = m*0.165
    if s < 0:
        print("{}:{:.2f}".format(num,m-l))
    elif s <= 1500:
        print("{}:{:.2f}".format(num,m-l-(s*0.03-0)))
    elif s > 1500 and s <= 4500:
        print("{}:{:.2f}".format(num,m-l-(s*0.10-105)))
    elif s > 4500 and s <= 9000:
        print("{}:{:.2f}".format(num,m-l-(s*0.20-555)))
    elif s > 9000 and s <= 35000:
        print("{}:{:.2f}".format(num,m-l-(s*0.25-1005)))
    elif s >35000 and s <= 55000:
        print("{}:{:.2f}".format(num,m-l-(s*0.30-2755)))
    elif s > 55000 and s <= 80000:
        print("{}:{:.2f}".format(num,m-l-(s*0.35-5505)))
    else:
        print("{}:{:.2f}".format(num,m-l-(s*0.45-13505)))
              
 

if __name__=="__main__":
    for argv in sys.argv[1:]:
        num, salary = argv.split(':')
        calculator(num, salary)
