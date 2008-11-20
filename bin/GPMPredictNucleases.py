import sys
import os
import re
from nucleaser import CrossRef

def getProteinList(name):
	prolist = []
	directory = os.getcwd()
	data_directory = os.path.join(directory, "data")
	data_directory = os.path.join(data_directory, name)
	if os.access(data_directory, os.F_OK):
		data_file = os.path.join(data_directory, 'ensp_list')
		f = open(data_file, 'r')
		prolist = f.readlines()
	else:
		print "Can't find data directory, please try again"
	return prolist

def check_domain(list, ref):
	check = 0
	for domain in list:
		p = re.compile(domain)
		if p.search(ref):
			check = 1
			break
	return check

def classifyNuclease(ensp, cr):
	prosite_list = ['PS00726', 'PS00727', 'PS00728', 'PS00729', 'PS00730', 'PS00731', 'PS00648', 'PS01321', 'PS01070', 'PS00919', 'PS00918', 'PS00764', 'PS01155', 'PS00812', 'PS50819', 'PS51392', 'PS00127', 'PS50879', 'PS01175', 'PS50142', 'PS00517', 'PS01277', 'PS00530', 'PS00531', 'PS50828', 'PS01137', 'PS01090', 'PS01091', 'PS50830', 'PS00841', 'PS00842']
	interpro_list = ['IPR004586', 'IPR001130', 'IPR011589', 'IPR012022', 'IPR015992', 'IPR012278', 'IPR015991', 'IPR003027', 'IPR003615', 'IPR002711', 'IPR004042', 'IPR007869', 'IPR015147', 'IPR004808', 'IPR000097', 'IPR005094', 'IPR016644', 'IPR005135', 'IPR012296', 'IPR008822', 'IPR016281', 'IPR008947', 'IPR006166', 'IPR011856', 'IPR006677', 'IPR002562', 'IPR013520', 'IPR006055','IPR015361','IPR014956','IPR016202','IPR008185','IPR017482']
	go_nuclease = ['GO:0004518']
	go_protease = ['GO:0008233']
	returnVal = -1
	check = 0
	prosite_refs = cr.getPrositeInfo()
	interpro_refs = cr.getInterproInfo()
	go_refs = cr.getGOInfo()
	for ref in prosite_refs:
		if check == 0:
			check = check_domain(prosite_list, ref)
		if check == 1:
			print "PROSITE"
			print ensp
			returnVal = 1
	check = 0
	for ref in interpro_refs:
		if check == 0:
			check =  check_domain(interpro_list, ref)
		if check == 1:
			print "INTERPRO"
			print ensp
			returnVal = 1
	check = 0
	for ref in go_refs:
		if check == 0:
			check =  check_domain(go_nuclease, ref)
		if check == 1:
			print "GO NUCLEASE"
			print ensp
			returnVal = 1
	return returnVal
	check = 0
	for ref in go_refs:
		if check == 0:
			check =  check_domain(go_protease, ref)
		if check == 1:
			print "GO PROTEASE"
			print ensp
			returnVal = 1
	return returnVal

if __name__ == "__main__":
	try :
		if sys.argv[1] == '-e':
			experiment = sys.argv[2]
			i = 0
			j = 0
			k = 0
			ensp_ids = getProteinList(experiment)
			for ensp_id in ensp_ids:
				i += 1
				ensp_id = ensp_id.rstrip()
				cross_refs = CrossRef.CrossRef(experiment, ensp_id)
				is_nuclease = classifyNuclease(ensp_id, cross_refs)
				if is_nuclease == 0:
					j += 1
				elif is_nuclease == 1:
					k += 1
	except IndexError:
		print "Usage: python PredictNucleases.py -e expname"
	print i, j, k
