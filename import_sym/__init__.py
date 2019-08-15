from idautils import *
from idaapi import *
from idc import *

def load_file(filename):
	direct = os.getcwd()
	os.path.exists(direct)
	file = ""
	try:
		file = open(direct+"/"+filename, "r")
	except Exception as e:
		#sys.exit("ERROR: Failed to find Aarch64.reg file");
		print e
		return None
	return file

def import_symbols(filename):
	symFile = load_file(filename)
	for line in symFile:
		splitLine = line.rstrip().split(":")
		name = splitLine[1]
		addr = splitLine[0]
		if not name[0:6] == "_func_":
			print "%X" % int(addr, 16),":",name
			MakeName(int(addr, 16), name)
	autoanalyse()
	print 'Done'