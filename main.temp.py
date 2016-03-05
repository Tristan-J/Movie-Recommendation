from printFile import printFile
from readFile import readFile

import re
import os
from time import gmtime, strftime
import numpy as np

np.random.seed(1)

def getRanWeight(r, c):
	return 2 * np.random.random((r, c)) - 1 # mean = 0

def setLayerPre(e, v, it):
	for i in range(len(e)):
		if e[i]==it:
			v[i] = 1
		else:
			v[i] = 0
	return v

def setLayerPregr(e, v, it):
	for i in range(len(e)):
		v[i] = 0
	for i in range(len(it)):
		for j in range(len(e)):
			if e[j]==it[i]:
				v[j] = 1
	return v

def nonlin(x,deriv=False):
	if(deriv==True):
		return x*(1-x)
	return 1/(1+np.exp(-x))

e_gender = ['F', 'M']
w_gender = getRanWeight(len(e_gender), 1) # matrix: 1*n

e_age = ['1', '18', '25', '35', '45', '50', '56']
w_age = getRanWeight(len(e_age), 1)

e_occu = [str(i) for i in range(21)]
w_occu = getRanWeight(len(e_occu), 1)

e_zcode = [str(i) for i in range(10)]
w_zcode = getRanWeight(len(e_zcode), 1)

e_year = ['('+ str(i) for i in range(190, 202)]
w_year = getRanWeight(len(e_year), 1)

e_genres = ['Action', 'Adventure', 'Animation', "Children's", 'Comedy', 'Crime'
			, 'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror', 'Musical'
			, 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']
w_genres = getRanWeight(len(e_genres), 1)

[id, gender, age, occupation, zipcode, title, genres, rating] = readFile('/test/reTrainData.test.dat', 1, '::')

# file = '/test/reTrainData.test.dat'
file = '/output/reTrainData.dat'
path = os.getcwd() + file
f = open(path, 'r')

gender = np.array([0 for i in range(len(e_gender))])
age = np.array([0 for i in range(len(e_age))])
occu = np.array([0 for i in range(len(e_occu))])
zcode = np.array([0 for i in range(len(e_zcode))])
year = np.array([0 for i in range(len(e_year))])
genres = np.array([0 for i in range(len(e_genres))])
rating = 0

layer0 = np.array([0 for i in range(6)]) # value of layer0
syn0 = getRanWeight(len(layer0), len(layer0) * 2)

layer1 = np.array([])
syn1 = getRanWeight(len(layer0) * 2, 1)

layer2 = 0

count = 0

while True:
	line = f.readline().strip()
	if not line:
		f.close()
		break
	items = re.split('::', line)

	try:
		gender = setLayerPre(e_gender, gender, items[1])
		age = setLayerPre(e_age, age, items[2])
		occu = setLayerPre(e_occu, occu, items[3])
		zcode = setLayerPre(e_zcode, zcode, items[4][0])
		matchYear = re.match( r'.*([0-9]{4}).*', items[5])
		year = setLayerPre(e_year, year, matchYear.group(1))
		genres = setLayerPregr(e_genres, genres, items[6].split('|'))
		rating = float(items[7])
	except Exception:
		print Exception
		print 'error@' + str(count) + ' :'
		print line
		continue

	layer0[0] = nonlin(np.dot(gender, w_gender))
	layer0[1] = nonlin(np.dot(age, w_age))
	layer0[2] = nonlin(np.dot(occu, w_occu))
	layer0[3] = nonlin(np.dot(zcode, w_zcode))
	layer0[4] = nonlin(np.dot(year, w_year))
	layer0[5] = nonlin(np.dot(genres, w_genres))

	layer1 = nonlin(np.dot(np.transpose(layer0), syn0))
	layer2 = nonlin(np.dot(layer1, syn1))

	l2_error = rating/5.0 - layer2
	if count%1000 == 0:
		print 'Error:' + str(np.abs(l2_error))

	l2_delta = l2_error * nonlin(layer2, deriv=True)

	l1_error = l2_delta.dot(syn1.T)

	l1_delta = l1_error * nonlin(layer1, deriv=True)

	pre_error = l1_delta.dot(syn0.T)

	pre_delta = pre_error * nonlin(layer0, deriv=True)

	gender_delta = gender*pre_delta[0]
	age_delta = age*pre_delta[1]
	occu_delta = occu*pre_delta[2]
	zcode_delta = zcode*pre_delta[3]
	year_delta = year*pre_delta[4]
	genres_delta = genres*pre_delta[5]

	syn1 += np.transpose(layer1).dot(l2_delta)
	syn0 += np.dot(layer0, l1_delta)
	w_gender += gender*gender_delta
	w_age += age*age_delta
	w_occu += occu*occu_delta
	w_zcode += zcode*zcode_delta
	w_year += year*year_delta
	w_genres += genres*genres_delta

	count += 1

f.close()

file = '/output/record'
path = os.getcwd() + file
f = open(path, 'a')

f.write('---' + strftime("%a, %d %b %Y %H:%M:%S +8h", gmtime()) + '\n')
f.write('syn0:\n')
for i in syn0:
	f.write(str(i) + '\n')
f.write('syn1:\n')
for i in syn1:
	f.write(str(i) + '\n')
f.write('w_gender:\n')
for i in w_gender:
	f.write(str(i) + '\n')
f.write('w_age:\n')
for i in w_age:
	f.write(str(i) + '\n')
f.write('w_occu:\n')
for i in w_occu:
	f.write(str(i) + '\n')
f.write('w_zcode:\n')
for i in w_zcode:
	f.write(str(i) + '\n')
f.write('w_year:\n')
for i in w_year:
	f.write(str(i) + '\n')
f.write('w_genres:\n')
for i in w_genres:
	f.write(str(i) + '\n')

f.close()