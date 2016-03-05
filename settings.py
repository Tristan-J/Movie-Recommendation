import numpy as np

np.random.seed(1)
def getRanWeight(r, c):
	return 2 * np.random.random((r, c)) - 1 # mean = 0

# RATINGS FILE DESCRIPTION
# ================================================================================

# All ratings are contained in the file "ratings.dat" and are in the
# following format:

# UserID::MovieID::Rating::Timestamp

# - UserIDs range between 1 and 6040 
# - MovieIDs range between 1 and 3952
# - Ratings are made on a 5-star scale (whole-star ratings only)
# - Timestamp is represented in seconds since the epoch as returned by time(2)
# - Each user has at least 20 ratings


# USERS FILE DESCRIPTION
# ================================================================================

# User information is in the file "users.dat" and is in the following
# format:

# UserID::Gender::Age::Occupation::Zip-code

# All demographic information is provided voluntarily by the users and is
# not checked for accuracy.  Only users who have provided some demographic
# information are included in this data set.

# - Gender is denoted by a "M" for male and "F" for female
# - Age is chosen from the following ranges:

# 	*  1:  "Under 18"
# 	* 18:  "18-24"
# 	* 25:  "25-34"
# 	* 35:  "35-44"
# 	* 45:  "45-49"
# 	* 50:  "50-55"
# 	* 56:  "56+"

# - Occupation is chosen from the following choices:

# 	*  0:  "other" or not specified
# 	*  1:  "academic/educator"
# 	*  2:  "artist"
# 	*  3:  "clerical/admin"
# 	*  4:  "college/grad student"
# 	*  5:  "customer service"
# 	*  6:  "doctor/health care"
# 	*  7:  "executive/managerial"
# 	*  8:  "farmer"
# 	*  9:  "homemaker"
# 	* 10:  "K-12 student"
# 	* 11:  "lawyer"
# 	* 12:  "programmer"
# 	* 13:  "retired"
# 	* 14:  "sales/marketing"
# 	* 15:  "scientist"
# 	* 16:  "self-employed"
# 	* 17:  "technician/engineer"
# 	* 18:  "tradesman/craftsman"
# 	* 19:  "unemployed"
# 	* 20:  "writer"

e_gender = ['F', 'M']
w_gender = getRanWeight(len(e_gender), 1)

e_age = [1, 18, 25, 35, 45, 50, 56]
w_age = getRanWeight(len(e_age), 1)

e_occu = [i for i in range(21)]
w_occu = getRanWeight(len(e_occu), 1)

e_zcode = [i for i in range(10)]
w_zcode = getRanWeight(len(e_zcode), 1)

# MOVIES FILE DESCRIPTION
# ================================================================================

# Movie information is in the file "movies.dat" and is in the following
# format:

# MovieID::Title::Genres

# - Titles are identical to titles provided by the IMDB (including
# year of release)
# - Genres are pipe-separated and are selected from the following genres:

# 	* Action
# 	* Adventure
# 	* Animation
# 	* Children's
# 	* Comedy
# 	* Crime
# 	* Documentary
# 	* Drama
# 	* Fantasy
# 	* Film-Noir
# 	* Horror
# 	* Musical
# 	* Mystery
# 	* Romance
# 	* Sci-Fi
# 	* Thriller
# 	* War
# 	* Western

# - Some MovieIDs do not correspond to a movie due to accidental duplicate
# entries and/or test entries
# - Movies are mostly entered by hand, so errors and inconsistencies may exist
e_mtitle = ['Action', 'Adventure', 'Animation', "Children's", 'Comedy', 'Crime'
			, 'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror', 'Musical'
			, 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']
w_mtitle = getRanWeight(len(e_mtitle), 1)

e_year = ['('+ str(i) for i in range(190, 202)]
w_year = getRanWeight(len(e_year), 1)