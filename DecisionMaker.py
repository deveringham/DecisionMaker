#
#    ___          _     _            __  ___     __          	 /\_______/\
#   / _ \___ ____(_)__ (_)__  ___   /  |/  /__ _/ /_____ ____ 	 /_  ___   \
#  / // / -_) __/ (_-</ / _ \/ _ \ / /|_/ / _ `/  '_/ -_) __/	/ @\/ @ \   \
# /____/\__/\__/_/___/_/\___/_//_//_/  /_/\_,_/_/\_\\__/_/   	\__/\___/   /
#																 \_\/______/
#  DecisionMaker.py 											 /     /\\\\\ 
#  Dylan Everingham for Marissa Kohan							|      \\\\\\\ 
#																 \      \\\\\\\ 
#																  \______/\\\\\
#																	_||_||_

#
# Contains necessary classes for DecisonMaker app backend
# Used in main.py

# Dependencies
import random
import collections

# Parameters [Range] (Encoding) :
#
# Date
#	Day of Week					[0 6]
#	Year 						[-100 100]		
# Time							[0 23]
# Weather 						[0 4]			(Sunny, Cloudy, Raining, Snowing, Natural Disaster)
# Dylan/Marissa/Both			[0 2]
# Hunger Level					[-5 5]
# Thirst Level					[-5 5]
# Energy Level					[-5 5]
# Introversion Level			[-5 5]
# Stress Level					[-5 5]
# Mercury in Retrograde?		[0 1]

# Parameters struct
# Named tuple with a value for each input parameter
Parameter_Fields = \
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

Parameters = collections.namedtuple(
	'Parameters', 
	Parameter_Fields
)

# Possibility object
# Has a min/max for each parameter, weighting for each parameter, and a baseline weight
class Possibility:

	# Possibility class constructor
	# Arguments:
	#	min_params: tuple containing minimum parameter values under which this possibility can be selected
	#	max_params: tuple containing maximum parameter values under which this possibility can be selected
	#	param_weights: tuple containing probability weight scale factors for each input parameter
	#	base_weight: base probability weight. should be a float in range [0 1]
	#	message: string displayed when this Possibility is chosen
	def __init__(self, min_params, max_params, param_weights, base_weight, message):
		# Save all parameter limits
		self.param_limits = Parameters(*tuple([[min_params[i], max_params[i]] for i in range(len(Parameter_Fields))]))

		# Save all parameter weights
		self.param_weights = param_weights
		self.base_weight = base_weight

		# Save message
		self.message = message

	# Function to return probability weight of this possibility being chosen under some Parameters.
	# If the Parameters are outside this Possibility's limits, return 0.
	# Arguments:
	#	params: Parameters under which we want to calculate the weighted probability of this Possibility
	#			being chosen
	# Return values:
	#	prob: probability of this Possibility being chosen. Can be any non-negative float. Percent probability
	#			is calculated by dividing this by the sum of all other Possibility's weights
	def getProb(self, params):
		# Make sure the parameters fit first
		if not (self.inLimits(params)):
			return 0

		# Sum up parameter weights
		#prob = sum([[params.f * self.param_weights.f] for f in Parameter_Fields])

		# Add base weight
		prob += self.base_weight
		return prob
	
	# Function which determines if some Parameters fall within this Possibility's limits
	# Arguments:
	#	params: Parameters under which we want to see if this Possibility can be chosen
	# Return values:
	#	limits_satisfied: boolean value which is true if all limits are satisfied, and false otherwise
	def inLimits(self, params):
		# Check all limits
		satisfied_list = [[(params[i] >= self.param_limits[i][0]) and (params[i] <= self.param_limits[i][1])] \
			for i in range(len(Parameter_Fields))]
		return (sum(satisfied_list) == len(satisfied_list))

	# Getter for Possibility message
	# Arguments:
	#	None
	# Return values:
	#	message: Probability message
	def getMsg(self):
		return self.message

# DecisionMaker object
# Has a list of possibility objects
class DecisionMaker:
	# DecisionMaker class constructor
	# Arguments:
	#	db_fname: name of file to read in Possibility data from
	def __init__(self, db_fname):
		# Save database filename
		self.db_fname = db_fname

		# Start with an empty list of Possibilities
		self.possibilities = []

		# Seed rng
		random.seed()

	# Function to add Possibility to internal list
	def addPossibility(self, possibility):
		self.possibilities.append(possibility)

	# Function to read in possibilities from database file and populate list

	# Function which takes some Parameters and finds all Possibilities which fit.
	#	Then it randomly chooses from that list based on weights,
	#	and returns the chosen Possibility's message
	# Arguments:
	#	params: Parameters under which a Possibility is being chosen
	# Return values:
	#	message: string representing the correct decision to be made under these Parameters
	def choose(self, params):
		# Get all possibility weights
		weights = [[p.getProb(params)] for p in self.possibilities]

		# Get weighted random choice
		decision = random.choices(self.possibilities, weights)

		# Return decision
		return decision.getMsg()
