###########################################################################
# Description: read table data from a file
# Author: tristan.xiery@gmail.com
###########################################################################
# Typical invoking: [data0, data1, data3] = readFile('/input/data', 1, ',', '|~', '|-')
# Return: multi-dimensional vector A
# Exceptions: None
# Dependance: import re; import os

import re
import os

def readFile(file, titleLines, *arg):
	path = os.getcwd() + file
	f = open(path, 'r')
	splitStr = ''
	for i in arg:
		splitStr += i
	for i in range(titleLines):
		f.readline()
	startLine = f.tell()
	l = len(re.split(splitStr, f.readline()))
	# startLine = 0 if startLine==0 else startLine-1
	f.seek(startLine, 0)
	A = [[] for i in range(l)]

	while True:
		line = f.readline().strip()
		if not line:
			f.close()
			break
		items = re.split(splitStr, line)
		for i in range(l):
			A[i].append(items[i])

	return A