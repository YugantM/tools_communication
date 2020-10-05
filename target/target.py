#!/usr/bin/env python
import json
import sys,getopt

def target(key):

    print("from the traget function","".join(sys.stdin))
    #string = json.dumps(sys.stdin)
    string = json.loads(json.dumps("".join(sys.stdin)))

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

    print(target(key))
    return target(key)


if __name__ == '__main__':
    main(sys.argv[1:])