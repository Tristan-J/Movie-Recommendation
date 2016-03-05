from printFile import printFile
from readFile import readFile

def reTrainData(uid, gd, age, oc, zc, \
	mid, tt, gn, \
	tuid, tmid, rt, tid):
	rgd	= []
	rage	= []
	roc	= []
	rzc	= []
	rtt	= []
	rgn	= []
	rrt	= []
	uPointer = 0
	mPointer = 0

	for i in range(len(tuid)):
		for j in range(len(uid)):
			if tuid[i] == uid[uPointer]:
				rgd.append(gd[uPointer])
				rage.append(age[uPointer])
				roc.append(oc[uPointer])
				rzc.append(zc[uPointer])
				for k in range(len(mid)):
					if tmid[i] == mid[mPointer]:
						rtt.append(tt[mPointer])
						rgn.append(gn[mPointer])
						rrt.append(rt[mPointer])
						break
					else:
						mPointer = (1 + mPointer) % len(mid)
				break
			else:
				uPointer = (1 + uPointer) % len(uid)
				print 'up:' + str(uPointer)

	rid = [i for i in range(len(tid))]
	printFile('/output/reTrainData.dat', \
		'id, gender, age, occupation, zipcode, title, genres, rating', \
		rid, '::', rgd, '::', rage, '::', roc, '::', rzc, '::', rtt, '::', rgn, '::', rrt)

uid	= []
gd	= []
age	= []
oc	= []
zc	= []

mid	= []
tt	= []
gn	= []

tuid	= []
tmid	= []
rt	= []
tid	= []

[uid, gd, age, oc, zc] = readFile('/original/users.dat', 0, '::')

[mid, tt, gn] = readFile('/original/movies.dat', 0, '::')

[tuid, tmid, rt, tid] = readFile('/original/training_ratings_for_kaggle_comp-backup.csv', 1, ',')

reTrainData(uid, gd, age, oc, zc, mid, tt, gn, tuid, tmid, rt, tid)