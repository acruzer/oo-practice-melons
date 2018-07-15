############
# Part 1   #
############


class MelonType(object):
	"""A species of melon at a melon farm."""

	def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
				 name):
		"""Initialize a melon."""

		self.code = code
		self.first_harvest = first_harvest
		self.color = color
		self.is_seedless = is_seedless
		self.is_bestseller = is_bestseller
		self.name = name
		self.pairings = []
		

		# Fill in the rest

	def add_pairing(self, *args):
		"""Add a food pairing to the instance's pairings list."""

		# Fill in the rest
		self.pairings.extend(args)


	def update_code(self, new_code):
		"""Replace the reporting code with the new_code."""

		# Fill in the rest
		self.code = new_code





def make_melon_types():
	"""Returns a list of current melon types."""

	all_melon_types = []

	# Fill in the rest
	musk = MelonType("musk",1998,'green',True, True,"Muskmelon")
	musk.add_pairing("mint")
	all_melon_types.append(musk)

	cas = MelonType("cas", 2003, "orange", True, False, "Casaba")
	cas.add_pairing("stawberries", "mint")
	all_melon_types.append(cas)

	cren = MelonType("cren",1996, "green",False,False,"Crenshaw")
	cren.add_pairing("proscuitto")
	all_melon_types.append(cren)

	yw = MelonType("yw",2013,"yellow",False,True,"Yellow Watermelon")
	yw.add_pairing("ice cream")
	all_melon_types.append(yw)

	return all_melon_types

#print(make_melon_types())
#print(make_melon_types()[0].code)

def print_pairing_info(melon_types):
	"""Prints information about each melon type's pairings."""

	# Fill in the rest
		
	for melon in melon_types:
		var_pairings = "\n - ".join(melon.pairings)
#		print (f"potato {var}" )

		print("{} pairs with\n - {}\n".format(melon.name,var_pairings))

#print_pairing_info(make_melon_types())

def make_melon_type_lookup(melon_types):
	"""Takes a list of MelonTypes and returns a dictionary of melon type by code."""

	# Fill in the rest
	melon_dict = {}
	for instance in melon_types:
		melon_dict[instance.code] = instance

#	for key,value in melon_dict.items():
#		print(key, value)
	return melon_dict

make_melon_type_lookup(make_melon_types())


############
# Part 2   #
############

class Melon(object):
	"""A melon in a melon harvest."""
	def __init__(self,melon_type,shape_rating,color_rating,field,harvester):
		self.melon_type = melon_type
		self.shape_rating = shape_rating
		self.color_rating = color_rating
		self.field = field
		self.harvester = harvester

	# Fill in the rest
	# Needs __init__ and is_sellable methods
	#melon_dict = make_melon_type_lookup(make_melon_types())


	def is_sellable(self):

		if self.field == 3:
			return False
		elif self.shape_rating < 5 and self.color_rating < 5:
			return False
		else: 
			return True


		


def make_melons(melon_types):
	"""Returns a list of Melon objects."""

	# Fill in the rest

def get_sellability_report(melons):
	"""Given a list of melon object, prints whether each one is sellable."""

	# Fill in the rest 



melon1 = Melon("yw",8,7,2,"Shiela")

print(melon1.is_sellable())


melon_dict = make_melon_type_lookup(make_melon_types())

print(melon_dict[melon1.melon_type].first_harvest)
