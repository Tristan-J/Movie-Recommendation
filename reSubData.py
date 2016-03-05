from printFile import printFile
from readFile import readFile

def reSubData(uid, gd, age, oc, zc, \
	mid, tt, gn, \
	suid, rt, sid):
	rgd	= []
	rage	= []
	roc	= []
	rzc	= []
	rtt	= []
	rgn	= []
	uPointer = 0
	mPointer = 0

	for i in range(len(suid)):
		for j in range(len(uid)):
			if suid[i] == uid[uPointer]:
				rgd.append(gd[uPointer])
				rage.append(age[uPointer])
				roc.append(oc[uPointer])
				rzc.append(zc[uPointer])
				for k in range(len(mid)):
					tmid = sid[i].split('_')[-1]
					if tmid == mid[mPointer]:
						rtt.append(tt[mPointer])
						rgn.append(gn[mPointer])
						break
					else:
						mPointer = (1 + mPointer) % len(mid)
				break
			else:
				uPointer = (1 + uPointer) % len(uid)
				print 'up:' + str(uPointer)

	rid = [i for i in range(len(sid))]
	printFile('/output/reSubData.dat',
		'id, gender, age, occupation, zipcode, title, genres\n',
		rid, '::', rgd, '::', rage, '::', roc, '::', rzc, '::', rtt, '::', rgn)

uid	= []
gd	= []
age	= []
oc	= []
zc	= []

mid	= []
tt	= []
gn	= []

suid	= []
rt	= []
sid	= []


[uid, gd, age, oc, zc] = readFile('/original/users.dat', 0, '::')

[mid, tt, gn] = readFile('/original/movies.dat', 0, '::')

# [tuid, tmid, rt, tid] = readFile('/original/training_ratings_for_kaggle_comp-backup.csv', 1, ',')
[suid, rt, sid] = readFile('/original/sample_submission.utf8.csv', 1, ',')

reSubData(uid, gd, age, oc, zc, mid, tt, gn, suid, rt, sid)