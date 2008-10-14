import sys
import os
import re

class MascotParser:
	def __init__(self, file):
		fh = open(file, 'r')
		self.lines = fh.readlines()
		fh.close()
	
	def getIPICodes(self, pre_codes):
		ipi_list = []
		p = re.compile("<a href=\"\#Hit\d+\">(IPI\d+)</a>")
		for line in self.lines:
			m = p.search(line)
			if m:
				ipi_code = m.group(1)
				check = 0
				for code in ipi_list:
					if code == ipi_code:
						check = 1
				if check == 0:
					for code in pre_codes:
						if code == ipi_code:
							check = 1
				if check == 0:
					ipi_list.append(ipi_code)
		return ipi_list


