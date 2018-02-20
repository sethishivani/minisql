def proj(data,noatt,table,fun):
	#############displaying attributes without where i.e we display a,b,c not tab1.a,tab2.b,tab1.c
	if(noatt[0]=='*'):
		noatt=[]
		for i in data[table]:
			noatt.append(table+'.'+i)
	#rep attributes of table we need#
	attlist=[]
	for i in data[table]:
		attlist.append(table+'.'+i)
	#making list of list of table from dict structure#
	for i in data[table]:
		it=len(data[table][i])
	tlist=[]
	mlist=[]
	for i in range (it):
		tlist=[]
		for j in data[table]:
			tlist.append(data[table][j][i])
		mlist.append(tlist)
	#print mlist
	tlist=[]
	tlist.append(mlist)
	tlist.append(attlist)
	#print tlist[1]
	return tlist



	'''num=len(data[table])
	#all attributes in that table
	if(noatt[0]=='*'):
		noatt=[]
		for i in data[table]:
			noatt.append(i)
	req={}
	aname=set([])
	#adding attribute name to a set
	for i in noatt:
		aname.add(i.strip())

	#print aname
	for i in data[table]:
		#print i
		if i in aname:
			#print "yes"
			req[i]=(data[table][i])
	#print req
	#print "\ni am here\n"
	cnt=1
	for i in req:
		if i in aname:
			print table,".",i,
			if cnt<len(aname):
				print ",",
		cnt+=1
	print ""
	#print req
	#print noatt
	it=len(req[noatt[(int)(0)]])
	#print it
	if fun=="display":
		for i in range (it):
			j=0
			for x in req:
				print req[x][i],
				if j<len(noatt)-1:
					print ",",
				j+=1
			print ""
	else:
		return req'''