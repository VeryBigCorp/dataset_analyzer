"""
	Input: the ith domain
	Output: key-value dictionary will successful missions in those domains (successful >= 3)
"""
def checkOneDomain(i):	\

	array1 = {}
	successArray = {}
	# fill list with all possibilities of domain
	for row in data:
		array1[row[i]] = array1.get(row[i], 0) + 1

	for key in array1:
		for row in data:
			if key in row:
				# include this check because some success statuses are ? and T
				if row[8] not in ('?', 'T'):
					if(int(row[8]) >= 3):
						#if success status is >= 3, count is as a success and add it to list
						successArray[row[i]] = successArray.get(row[i], 0) + 1

	#print out success rates for each possibility in said domain
	for key, value in sorted(successArray.iteritems()):
		print key, value
	print "\n"

"""
	Input: the ith and the jth domains
	Output: key-value dictionary will successful missions in those domains (successful >= 3).
	If comparing domain1 and domain2, the result will appear as:

	domain1 Counter ({('possible_domain_2', 1) : # of successes, ({('possible_domain_2', 1) : # of successes, }) etc

"""
def checkTwoDomains(i, j):	
	from collections import defaultdict
	from collections import Counter

	array1 = {}
	array2 = {}
	successArray = defaultdict(list)
	count = 0;
	# similar to checkOneDomain, create two lists, each holding eveyr possibility of respective domain
	for row in data:
		array1[row[i]] = array1.get(row[i], 0) + 1
		array2[row[j]] = array2.get(row[j], 0) + 1
	#cross analyze each domain against each other; if a combination is found with a success rate of at least 3, add it to the successArray (which holds all "successful" combinations)
	for key1 in array1:
		for key2 in array2:
			for row in data:
				if all(x in row for x in [key1, key2]):
					if row[8] not in ('?', 'T'):
						if(int(row[8]) >= 3):
							successArray[key1].append((key2, 1))
	#implement Counter to remove duplicates/tally total successes of each combination
	for key in successArray:
		successArray[key] = Counter(successArray[key])
	"""
	for key, value in sorted(successArray.iteritems()):
		print key, value
		print "\n"
	"""
	return successArray

"""
	Input: a list consisting of all the domains you want to cross analyze
	Output: key-value dictionary will successful missions in those domains (successful >= 3).
	If comparing domain1 and domain2, the result will appear as:

	domain1 Counter ({('possible_domain_2', 1) : # of successes, ({('possible_domain_2', 1) : # of successes, }) etc

"""
def checkNDomains(listOfDomains):	
	from collections import defaultdict
	from collections import Counter

	successArray = defaultdict(list)
	domains = {}
	#dynamically create lists for each domain entered in input list; each domain gets it own list
	for domain in listOfDomains:
		domains[domain] = {}
	for domain1, domain1_checks in domains.items():
		for domain2 in listOfDomains:
			if domain2 != domain1:
				domain1_checks[domain2] = checkTwoDomains(domain1,domain2)
	return domains
	#attempt to cross check each combination...don't know how to do this since the # of loops are unknown...maybe do a more efficient way for this?
	"""for row in data:
		if all(x in row for x in listOfDomains):
			if row[8] not in ('?', 'T'):
				if(int(row[8]) >= 3):
					successArray[key1].append((key2, 1))
	"""



					
"""
	Main method
"""

if __name__ == "__main__":
	import csv

	data = []
	with open('cubesat.csv', 'rb') as csvfile:
		analyzer = csv.reader(csvfile, delimiter=",", quotechar="|")
		data = list(analyzer);
	#checkOneDomain(4)
	#checkTwoDomains(4, 7)
	domains = checkNDomains([4,7,8,9])
	print domains