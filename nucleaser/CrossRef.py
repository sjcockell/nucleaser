import sys
import os
import re

class CrossRef:
	def __init__(self, exp_name, pro_id):
		directory = os.getcwd()
		data_directory = os.path.join(directory, "data")
		self.data_directory = os.path.join(data_directory, exp_name)
		self.protein = pro_id
		
	def getPrositeInfo(self):
		prosite_list = []
		data_file = os.path.join(self.data_directory, "biomart_prosite.txt")
		f = open(data_file, 'r')
		lines = f.readlines()
		p = re.compile(self.protein)
		for line in lines:
			m = p.match(line)
			if m is not None:
				line = line.rstrip()
				tokens = line.partition('\t')
				prosite = tokens[2]
				prosite_list.append(prosite)
		return prosite_list

	def getInterproInfo(self):
		interpro_list = []
		data_file = os.path.join(self.data_directory, "biomart_interpro.txt")
		f = open(data_file, 'r')
		lines = f.readlines()
		p = re.compile(self.protein)
		for line in lines:
			m = p.match(line)
			if m is not None:
				line = line.rstrip()
				tokens = line.partition('\t')
				interpro = tokens[2]
				interpro_list.append(interpro)
		return interpro_list

	def getGOInfo(self):
		go_list = []
		data_file = os.path.join(self.data_directory, "biomart_gomf.txt")
		f = open(data_file, 'r')
		lines = f.readlines()
		p = re.compile(self.protein)
		for line in lines:
			m = p.match(line)
			if m is not None:
				line = line.rstrip()
				tokens = line.partition('\t')
				go = tokens[2]
				go_list.append(go)
		return go_list

