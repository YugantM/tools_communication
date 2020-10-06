#!/usr/bin/env python
import json
import sys,getopt,ast

def target(key):

    print("from the traget function","".join(sys.stdin))
    
    message = json.dumps(sys.stdin)
    dump = json.dumps(message)
    string = json.loads(dump.replace("'", "\""))

    print(len(string),dump,message,string)
    print(ast.literal_eval(string))
    print(string[key])

    if key in string.keys():
        print(string[key])


        return string

    else:

        print('No such keys found')
        return 0

def main(argv):

    opts, args = getopt.getopt(argv,"k",["key"])

    for opt, arg in opts:
        if opt == '-k':

            key = arg

    #print(target(key))
    return target(key)


if __name__ == '__main__':
    main(sys.argv[1:])