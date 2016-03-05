import MySQLdb

def loginDB():
	# Open database connection
	db = MySQLdb.connect("localhost","fmovie","3sSQmQhmGMR9fTZv","fmovie" )
	return db

def createTB():
	db = loginDB()

	# prepare a cursor object using cursor() method
	cursor = db.cursor()

	# Drop table if it already exist using execute() method.
	cursor.execute("DROP TABLE IF EXISTS SHOWALL")

	# Create table as per requirement
	sql = """CREATE TABLE SHOWALL (
	         RATINGID INT NOT NULL PRIMARY KEY,
	         USERID INT,
	         GENDER CHAR(1),
	         AGE INT,
	         OCCUPATION INT,
	         ZCODE INT,
	         MOVIEID INT,
	         MTITLE VARCHAR(100),
	         MGENRES VARCHAR(60),
	         RATING FLOAT)"""

	cursor.execute(sql)

	# Drop table if it already exist using execute() method.
	cursor.execute("DROP TABLE IF EXISTS USER")

	# Create table as per requirement
	sql = """CREATE TABLE USER (
	         USERID INT NOT NULL PRIMARY KEY,
	         GENDER CHAR(1),
	         AGE INT,
	         OCCUPATION INT,
	         ZCODE INT)"""

	cursor.execute(sql)

	# Drop table if it already exist using execute() method.
	cursor.execute("DROP TABLE IF EXISTS MOVIE")

	# Create table as per requirement
	sql = """CREATE TABLE MOVIE (
	         MOVIEID INT NOT NULL PRIMARY KEY,
	         MTITLE VARCHAR(100),
	         MGENRES VARCHAR(60))"""

	cursor.execute(sql)

	# Drop table if it already exist using execute() method.
	cursor.execute("DROP TABLE IF EXISTS RATING")

	# Create table as per requirement
	sql = """CREATE TABLE RATING (
	         RATINGID INT NOT NULL PRIMARY KEY,
	         USERID INT,
	         MOVIEID INT,
	         RATING FLOAT)"""

	cursor.execute(sql)

	# disconnect from server
	db.close()

	return 0

def insertUser(uid, gd, age, oc, zc):
	db = loginDB()
	cursor = db.cursor()

	for i in range(len(uid)):
		sql = "INSERT INTO USER \
		VALUES (%d, '%c', %d, %d, %d)" %\
		(int(uid[i]), gd[i], int(age[i]), int(oc[i]), int(zc[i]))

		try:
		   # Execute the SQL command
		   cursor.execute(sql)
		   # Commit your changes in the database
		   db.commit()
		except:
		   # Rollback in case there is any error
		   db.rollback()

	db.close()

def insertMovie(mid, tt, gn):
	db = loginDB()
	cursor = db.cursor()

	for i in range(len(mid)):
		sql = "INSERT INTO MOVIE \
		VALUES (%d, '%s', '%s')" %\
		(int(mid[i]), tt[i], gn[i])

		try:
		   # Execute the SQL command
		   cursor.execute(sql)
		   # Commit your changes in the database
		   db.commit()
		except:
		   # Rollback in case there is any error
		   db.rollback()

	db.close()

def insertRating(rid, ruid, rmid, rt):
	db = loginDB()
	cursor = db.cursor()

	for i in range(len(rid)):
		sql = "INSERT INTO RATING \
		VALUES (%d, %d, %d, %f)" %\
		(int(''.join(rid[i].split('_'))), int(ruid[i]), int(rmid[i]), float(rt[i]))

		try:
		   # Execute the SQL command
		   cursor.execute(sql)
		   # Commit your changes in the database
		   db.commit()
		except:
		   # Rollback in case there is any error
		   db.rollback()

	db.close()
