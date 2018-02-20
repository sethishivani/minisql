def ddata(l,dispatt):
	#l is list of list
	tdic={}
	op=[]
	for i in l:
		if tdic.has_key(str(i))==False:
			tdic[str(i)]=1;
			op.append(i)
	it=len(l[0])
	cnt=1
	for i in dispatt:
		print i,
		if cnt<it:
			print ",",
		cnt+=1
	print ""
	for i in op:
		cnt=1
		for j in i:
			print j,
			if cnt<it:
				print ",",
			cnt+=1
		print ""