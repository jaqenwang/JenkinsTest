import sys

def func(argv):
    with open(argv,"w") as f:
        f.write("Hello World!")

if __name__ == '__main__':
    if(len(sys.argv)>1):
        func(sys.argv[1])
