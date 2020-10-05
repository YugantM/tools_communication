#!/usr/bin/env python
import json
import sys,getopt

def select(argv):
	opts, args = getopt.getopt(argv,"k",["key"])

	for opt, arg in opts:
        if opt == '-k':

            key = arg

        string = ''

	for line in sys.stdin:
		string += str(line)


	string = json.dumps(string)
	string = json.loads(string)

	if key in string.keys():
		print(string[key])

		return string[key]

	else:

		print('No such keys found')
		return 0



if __name__ == '__main__':
	select(sys.argv[1:])