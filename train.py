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
			v[i] = 1.0
		else:
			v[i] = 0
	return v

def setLayerPregr(e, v, it):
	for i in range(len(e)):
		v[i] = 0
	for i in range(len(it)):
		for j in range(len(e)):
			if e[j]==it[i]:
				v[j] = 1.0
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

e_year = [str(i) for i in range(190, 202)]
w_year = getRanWeight(len(e_year), 1)

e_genres = ['Action', 'Adventure', 'Animation', "Children's", 'Comedy', 'Crime'
			, 'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror', 'Musical'
			, 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']
w_genres = getRanWeight(len(e_genres), 1)

[id, gender, age, occupation, zipcode, title, genres, rating] = readFile('/test/reTrainData.test.dat', 1, '::')

gender = np.array([[0.0] for i in range(len(e_gender))])
age = np.array([[0.0] for i in range(len(e_age))])
occu = np.array([[0.0] for i in range(len(e_occu))])
zcode = np.array([[0.0] for i in range(len(e_zcode))])
year = np.array([[0.0] for i in range(len(e_year))])
genres = np.array([[0.0] for i in range(len(e_genres))])
rating = 0

layer0 = np.array([[0.0] for i in range(6)]) # value of layer0
syn0 = getRanWeight(len(layer0), len(layer0) * 2)

layer1 = None
syn1 = getRanWeight(len(layer0) * 2, 1)

layer2 = 0

# exp settings:
syn0 = np.array([
[-2.00658113459,-2.2992390908,-2.32947372612,8.09149795982,-1.83203927745,-2.41180503246,-2.17646762155,-2.47577199681,-1.9882010713,-17.1381995169,-1.86173302746,-2.16597575484,],
[-0.471295112609,-0.956579331106,-0.888219600802,1.62100563461,-0.78685135085,0.441487965864,-0.99489246289,-0.477493246989,-1.66500351055,-1.10077548923,-0.847273062607,-0.297603689763,],
[-1.64675435834,-0.915370718941,0.28955173825,0.419697097687,-1.05188578754,-0.419420641875,-1.99691621977,-1.09171398243,-0.473198133997,-2.44170989417,-0.244910094664,-0.637150687199,],
[-2.41300855632,0.306604112012,-0.161811054379,0.375415316465,-0.887641232934,-1.3505956622,-1.00079158883,-0.750570736273,-2.10095621782,-2.44813116146,-0.554562886961,0.0207392201396,],
[0.198993627755,-2.31684730931,-1.87936628999,-12.703807932,-2.57379176547,-0.55604296651,0.09000446892,-0.113929705337,-0.358121762065,20.6531329436,-2.17801675728,-2.49466839401,],
[-1.50745682117,0.903059186241,-0.121906437432,-16.6374078774,1.18504185535,-1.06815860215,-1.3020275511,-1.36551034699,-1.20181725974,23.1478460286,-0.860140472557,-1.93551083045,],
])
syn1 = np.array([
[-1.35624735],
[-1.45088864],
[-1.51907888],
[ 1.84042621],
[-1.1460251],
[-1.41188797],
[-1.39970903],
[-1.42762788],
[-1.33727634],
[ 1.74202305],
[-1.29148517],
[-1.29080068],
])
w_gender = np.array([
[ 4.26306097],
[ 4.84894701],
])
w_age = np.array([
[-1.28047501],
[-1.91502842],
[-1.796983],
[-1.66562826],
[-1.3857216],
[-1.25213371],
[-1.11781741],
])
w_occu = np.array([
[-0.51518308],
[-0.27534752],
[-0.51554168],
[-0.46698879],
[-0.38185871],
[-0.92315484],
[-0.43107217],
[-0.64426718],
[-0.38582693],
[-0.43296681],
[-1.05147139],
[-0.5120028],
[-0.27564806],
[-1.14803774],
[-0.59193144],
[-0.58294508],
[-0.49799595],
[-0.72575302],
[-0.66832529],
[-0.42273496],
[-0.53789018],
])
w_zcode = np.array([
[-1.01703715],
[-1.02116184],
[-0.95516434],
[-1.12364033],
[-0.77840597],
[-0.84226112],
[-0.94627627],
[-0.91681588],
[-0.8060052],
[-0.85654317],
])
w_year = np.array([
[ 0.97772218],
[ 0.4961365],
[-1.38390831],
[ 0.6745806],
[-6.79251904],
[-1.86488282],
[ 0.26865503],
[ 7.2133609],
[ 2.25913554],
[ 2.77251015],
[-0.73989534],
[ 0.35767107],
])
w_genres = np.array([
[-3.77018304],
[ 2.85360987],
[ 4.12702835],
[-5.44628183],
[-2.84807406],
[ 16.45277852],
[-2.21568599],
[-0.9108213],
[-0.82258527],
[-15.18772361],
[-3.86107712],
[ 1.45444031],
[-7.44509658],
[ 2.22033546],
[ 7.77141051],
[ 13.30112476],
[-0.88686095],
[ 4.294227],
])
# l2_bias = 0.8/5.0
l2_bias = 0
error_record = [[] for i in range(15)]

# file = '/test/reTrainData.test.dat'
file = '/output/reTrainData.dat'
path = os.getcwd() + file
f = open(path, 'r')
startLine = f.tell()

for loop in range(15):
	count = 1
	error_count = 0
	error_count_abs = 0
	f.seek(startLine, 0)
	while True:
		line = f.readline().strip()
		if not line:
			break
		items = re.split('::', line)

		try:
			gender = setLayerPre(e_gender, gender, items[1])
			age = setLayerPre(e_age, age, items[2])
			occu = setLayerPre(e_occu, occu, items[3])
			zcode = setLayerPre(e_zcode, zcode, items[4][0])
			matchYear = re.match( r'.*([0-9]{4}).*', items[5])
			year = setLayerPre(e_year, year, str(matchYear.group(1))[0:3])
			genres = setLayerPregr(e_genres, genres, items[6].split('|'))
			rating = float(items[7])
		except Exception:
			print Exception
			print 'error@' + str(count) + ' :'
			print line
			continue

		layer0[0] = nonlin(np.dot(gender.T, w_gender))
		layer0[1] = nonlin(np.dot(age.T, w_age))
		layer0[2] = nonlin(np.dot(occu.T, w_occu))
		layer0[3] = nonlin(np.dot(zcode.T, w_zcode))
		layer0[4] = nonlin(np.dot(year.T, w_year))
		layer0[5] = nonlin(np.dot(genres.T, w_genres))

		layer1 = nonlin(np.dot(layer0.T, syn0))
		layer2 = nonlin(np.dot(layer1, syn1)) + l2_bias

		l2_error = rating/5.0 - layer2
		if count%1000 == 0:
			error_record[loop].append((error_count_abs*5)/count)
		if count%10000 == 0:
			print str(loop) 
			print 'Average Error: ' + str((error_count*5)/count)
			print 'Average Abs Error: ' + str((error_count_abs*5)/count)
			count = 1
			error_count = 0
			error_count_abs = 0
		error_count += l2_error
		error_count_abs += np.abs(l2_error)
		if np.abs(l2_error)>=0.4:
			l2_error *= 0.5

		l2_delta = l2_error * nonlin(layer2, deriv=True)

		l1_error = l2_delta.dot(syn1.T)

		l1_delta = l1_error * nonlin(layer1, deriv=True)

		pre_error = l1_delta.dot(syn0.T)

		pre_delta = pre_error.T * nonlin(layer0, deriv=True)

		gender_delta = gender*pre_delta[0]
		age_delta = age*pre_delta[1]
		occu_delta = occu*pre_delta[2]
		zcode_delta = zcode*pre_delta[3]
		year_delta = year*pre_delta[4]
		genres_delta = genres*pre_delta[5]

		syn1 += layer1.T.dot(l2_delta)
		syn0 += np.dot(layer0, l1_delta)

		w_gender += gender*gender_delta
		w_age += age*age_delta
		w_occu += occu*occu_delta
		w_zcode += zcode*zcode_delta
		w_year += year*year_delta
		w_genres += genres*genres_delta

		count += 1
	print '------------------------------------'

f.close()

file = '/output/record'
path = os.getcwd() + file
f = open(path, 'a')

f.write('---' + strftime("%a, %d %b %Y %H:%M:%S +8h", gmtime()) + '\n')
f.write('syn0 = np.array([\n')
for i in syn0:
	f.write('[')
	for j in i:
		f.write(str(j) + ',')
	f.write('],\n')
f.write('])\n')

f.write('syn1 = np.array([\n')
for i in syn1:
	f.write(str(i) + ',\n')
f.write('])\n')

f.write('w_gender = np.array([\n')
for i in w_gender:
	f.write(str(i) + ',\n')
f.write('])\n')

f.write('w_age = np.array([\n')
for i in w_age:
	f.write(str(i) + ',\n')
f.write('])\n')

f.write('w_occu = np.array([\n')
for i in w_occu:
	f.write(str(i) + ',\n')
f.write('])\n')

f.write('w_zcode = np.array([\n')
for i in w_zcode:
	f.write(str(i) + ',\n')
f.write('])\n')

f.write('w_year = np.array([\n')
for i in w_year:
	f.write(str(i) + ',\n')
f.write('])\n')

f.write('w_genres = np.array([\n')
for i in w_genres:
	f.write(str(i) + ',\n')
f.write('])\n')


f.write('error_record = [\n')
for i in error_record:
	f.write(str(i) + ',\n')
f.write(']\n')




f.close()