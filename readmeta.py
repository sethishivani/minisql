def readmetadata():
	filepath = 'metadata.txt'  
	scheck="<begin_table>"
	echeck="<end_table>"
	sflag=0
	count=0
	mdict={}
	tname=''
	#line.strip()
	with open(filepath) as fp:  
		line = fp.readline()
		while line:
			if(line.strip()==echeck):
				sflag=0
				count=0
			if(line.strip()==scheck):
				sflag=1
				count=0
			if(count==1 and sflag==1):
				tname=line.strip()
				mdict[tname]=[]
			if(count>1 and sflag==1):
				#subd[line.strip()]=[]
				mdict[tname].append(line.strip())
			line = fp.readline()
			count+=1
		#print mdict
		return mdict
	#for x in mdict:
	#	print x
	'''for x in mdict:
		for k in mdict[x]:
			print("%10s"%k),
		print("\n")'''