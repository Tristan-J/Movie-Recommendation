###########################################################################
# Description: print table data to a file
# Author: tristan.xiery@gmail.com
###########################################################################
# Typical invoking: printFile('/output/damp', 'id, name, age', id, '-', name, '_', age)
# Return: 0
# Exceptions: None
# Dependance: import os

import os

def printFile(file, firstLine, *arg):
	path = os.getcwd() + file
	f = open(path, 'a')
	f.write(firstLine)
	countList = None

	for i in arg:
		if isinstance(i, list):
			countList = i
			break

	if not countList:
		printLine = ''
		for i in arg:
			printLine += i
		f.write(printLine)
		return 0

	for i in range(len(countList)):
		printLine = ''
		for k in range(len(arg)):
			printLine += str(arg[k][i]) if isinstance(arg[k], list) else str(arg[k])
		printLine += "\n"
		f.write(printLine)

	return 0