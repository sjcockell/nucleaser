import sys
import os
import re
from nucleaser import MascotParser, IPIHandler

def getIPIList(name):
	iplist = []
	directory = os.getcwd()
	data_directory = os.path.join(directory, "data")
	data_directory = os.path.join(data_directory, name)
	if os.access(data_directory, os.F_OK):
		files = os.listdir(data_directory)
		for file in files:
			p = re.compile('.htm$')
			if p.search(file):
				print len(iplist)
				file = os.path.join(data_directory, file)
				mp = MascotParser.MascotParser(file)
				iplist[len(iplist):] = mp.getIPICodes()
	else:
		print "Can't find data directory, please try again"


if __name__ == "__main__":
	try :
		if sys.argv[1] == '-e':
			experiment = sys.argv[2]
			getIPIList(experiment)
	except IndexError:
		print "Usage: python PredictNucleases.py -e expname"
