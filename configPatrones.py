#!/usr/bin/python

from ConfigParser import SafeConfigParser
from subprocess import Popen

def say(text):
    Popen(['espeak', '-v', 'es', text])
    
def main():
    parser = SafeConfigParser()
    parser.read('config.ini')
    escuchar = parser.get('cantidad', 'tres') + ' ' + parser.get('elemento', 'leones') + ' de ' + parser.get('material', 'metal')
    print escuchar
    say(escuchar)
   
if __name__ == "__main__":
    main()
