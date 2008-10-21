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
#				print len(iplist)
				file = os.path.join(data_directory, file)
				mp = MascotParser.MascotParser(file)
				iplist[len(iplist):] = mp.getIPICodes(iplist)
	else:
		print "Can't find data directory, please try again"
	return iplist

def check_domain(list, ref):
	check = 0
	for domain in list:
		p = re.compile(domain)
		if p.search(ref):
			check = 1
			break
	return check

def classifyNuclease(ipi):
	prosite_list = ['PS00726', 'PS00727', 'PS00728', 'PS00729', 'PS00730', 'PS00731', 'PS00648', 'PS01321', 'PS01070', 'PS00919', 'PS00918', 'PS00764', 'PS01155', 'PS00812', 'PS50819', 'PS51392', 'PS00127', 'PS50879', 'PS01175', 'PS50142', 'PS00517', 'PS01277', 'PS00530', 'PS00531', 'PS50828', 'PS01137', 'PS01090', 'PS01091', 'PS50830', 'PS00841', 'PS00842']
	panther_list = ['PTHR10139', 'PTHR10150', 'PTHR10359', 'PTHR10858','PTHR10960','PTHR11081','PTHR11371','PTHR11539','PTHR12749','PTHR13966','PTHR14950','PTHR18867',	'PTHR21044','PTHR21227','PTHR21445','PTHR21670','PTHR22748','PTHR22955','PTHR22993','PTHR23016','PTHR23022','PTHR10133','PTHR10139','PTHR10267','PTHR10322','PTHR10670','PTHR10870','PTHR11081','PTHR13710','PTHR18867','PTHR22748']
	interpro_list = ['IPR004586', 'IPR001130', 'IPR011589', 'IPR012022', 'IPR015992', 'IPR012278', 'IPR015991', 'IPR003027', 'IPR003615', 'IPR002711', 'IPR004042', 'IPR007869', 'IPR015147', 'IPR004808', 'IPR000097', 'IPR005094', 'IPR016644', 'IPR005135', 'IPR012296', 'IPR008822', 'IPR016281', 'IPR008947', 'IPR006166', 'IPR011856', 'IPR006677', 'IPR002562', 'IPR013520', 'IPR006055','IPR015361','IPR014956','IPR016202','IPR008185','IPR017482']
	returnVal = -1
	try:
		handler = IPIHandler.IPIHandler(ipi)
	except ValueError:
		returnVal = 0
	else:
		xrefs = handler.getSequenceXRefs()
		check = 0
		for ref in xrefs:
			check = check_domain(interpro_list, ref)
			if check == 0:
				check = check_domain(panther_list, ref)
	#		if check == 0:
	#			check = check_domain(prosite_list, ref)
			if check == 1:
				print ipi
				returnVal = 1
	return returnVal

if __name__ == "__main__":
	try :
		if sys.argv[1] == '-e':
			experiment = sys.argv[2]
			ipi_ids = getIPIList(experiment)
			i = 0
			j = 0
			k = 0
			for ipi_id in ipi_ids:
				i += 1
				is_nuclease = classifyNuclease(ipi_id)
				if is_nuclease == 0:
					j += 1
				elif is_nuclease == 1:
					k += 1
	except IndexError:
		print "Usage: python PredictNucleases.py -e expname"
	print i, j, k
