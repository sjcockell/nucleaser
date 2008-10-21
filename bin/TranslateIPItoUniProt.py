import sys
import os
import re
from nucleaser import MascotParser, IPIHandler
import PredictNucleases

def getUniProtID(ipi):
	p = re.compile('UniProtKB.+:(.{6})')
	try:
		handler = IPIHandler.IPIHandler(ipi)
	except ValueError:
		returnVal = 0
	else:
		xrefs = handler.getSequenceXRefs()
		for ref in xrefs:
			m = p.search(ref)
			if m is not None:
				print m.group(1)
				break


if __name__ == "__main__":
	try :
		if sys.argv[1] == '-e':
			experiment = sys.argv[2]
			ipi_ids = PredictNucleases.getIPIList(experiment)
			for ipi_id in ipi_ids:
				getUniProtID(ipi_id)
	except IndexError:
		print "Usage: python PredictNucleases.py -e expname"
