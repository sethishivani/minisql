import readcsv as rc
import readmeta as rm
def tabdata():
	md=rm.readmetadata()
	data={}
	for tn in md:
		#tn:table name
		#print tn
		rows=rc.readfilecsv(tn+".csv")
		ll=[]
		#made a list of list to read attribute wise list
		for row in rows:
			count =0
			for col in row:
				if(len(ll)<=count):
					ll.append([])
				ll[count].append(col)
				count+=1
		#print ll
		subd={}
		count=0
		for field in md[tn]:
			subd[field]=ll[count]
			count+=1
		data[tn]=subd
	#print("\n\n")
	return data


