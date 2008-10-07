import os
import sys
import re
from Bio import SeqIO

class IPIHandler:
	def strip_html(self):
		ifh = open(self.seq_file, 'r')
		lines = ifh.readlines()
		ifh.close()
		ofh = open(self.seq_file, 'w')
		for line in lines:
			subline = re.sub(r'<[^>]*?>', '', line)
			ofh.write(subline)
	
	def __init__(self, ipi_code=None):
		url = "http://srs.ebi.ac.uk/srsbin/cgi-bin/wgetz?-e+[IPI-acc:"+ipi_code+"]+-vn+2"
		os.system('wget -o wget-log --output-document=seq/'+ipi_code+'.seq '+url)
		self.seq_file = 'seq/'+ipi_code+'.seq'
		self.strip_html()
		handle = open('seq/'+ipi_code+'.seq')
		self.record = SeqIO.read(handle, 'swiss')

	def getSequence(self):
		return self.record.seq

	def getSequenceID(self):
		return self.record.id

	def getSequenceLength(self):
		return len(self.record.seq)
