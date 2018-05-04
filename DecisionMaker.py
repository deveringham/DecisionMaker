#    ___          _     _            __  ___     __          
#   / _ \___ ____(_)__ (_)__  ___   /  |/  /__ _/ /_____ ____
#  / // / -_) __/ (_-</ / _ \/ _ \ / /|_/ / _ `/  '_/ -_) __/
# /____/\__/\__/_/___/_/\___/_//_//_/  /_/\_,_/_/\_\\__/_/   
#
# DecisionMaker.py
# Dylan Everingham for Marissa Kohan
#

# Inputs [Range] (Encoding) :
#
# Date
#	Day of Week					[0 6]
#	Year						[-100 100]		
# Time							[0 23]
# Weather						[0 4]			(Sunny, Cloudy, Raining, Snowing, Natural Disaster)
# Dylan/Marissa/Both			[0 2]
# Hunger Level					[-5 5]
# Thirst Level					[-5 5]
# Energy Level					[-5 5]
# Introversion Level			[-5 5]
# Stress Level					[-5 5]
# Mercury in Retrograde?		[0 1]

# Parameters struct
# Named tuple with a value for each input parameter
Parameters = collections.namedtuple(
	'Parameters', 
	['day', \
	 'year', \
	 'time', \
	 'weather', \
	 'person', \
	 'hunger', \
	 'thirst', \
	 'energy', \
	 'introversion', \
	 'stress', \
	 'retograde']
)

# Possibility object
# Has a min/max for each parameter,
#	weighting for each parameter,
#	and a baseline weight.

# Function which determines if this Possibility fits some Parameters


# DecisionMaker object
# Has a list of possibility objects

# Function to read in possibilities from database file and populate list

# Function which takes some Parameters and finds all Possibilities which fit.
#	Then it randomly chooses from that list based on weights,
#	and returns that Possibility.
