import nucleaser.MascotParser as mp

parser = mp.MascotParser("data/mre11/CA-10M IPI-human.htm")
list = parser.getIPICodes()
for item in list:
	print item
