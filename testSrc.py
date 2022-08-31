import sys
import os

#def func(argv):
    #with open(argv,"w") as f:
    #    f.write("Hello World!")


if __name__ == '__main__':
    if(len(sys.argv)>1):
        #func(sys.argv[1])
        print(sys.argv[1:])
    print(os.stat(r'\\192.168.88.253\bk\whui\1.txt').st_size)
