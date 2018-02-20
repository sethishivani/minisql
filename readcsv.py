import csv
def readfilecsv(fname):
	#filename="table1.csv"
	fields=[]
	rows=[]
	with open(fname,'r') as csvfile:
		csvreader=csv.reader(csvfile)
		for row in csvreader:
			rows.append(row)
		#print rows
		#print("total no. of rows:%d"%(csvreader.line_num))
	return rows
	'''for row in rows:
		for col in row:
			print("%10s"%col),
		print("\n")'''

#readfilecsv("table2.csv")