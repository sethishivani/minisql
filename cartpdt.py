def rowlist(tab):
	it=0
	for i in tab:
		it=len(tab[i])
	disl=[]
	for i in range (it):
		temp=[]
		for x in tab:
			temp.append(tab[x][i])
		disl.append(temp)
	return disl


def cartesian(data,tn):
	attlist=[]
	tbattlist=[]
	temp=[]
	res=[]
	count=0
	index=1
	for i in tn:
		for x in data[i]:
			tbattlist.append(i+'.'+x)
			attlist.append(x)
		temp.append(rowlist(data[i]))
		count+=1
		if(count==2):
			count=1
			for i in temp[0]:
				for j in temp[1]:
					res.append(i+j)
			temp=[]
			temp=[res]
			res=[]
	#print attlist
	#for i in temp[0]:
		#print i
	#temp.append(tbattlist)
	#print temp[0]
	res.append(temp[0])
	res.append(tbattlist)
	#print res[0] is list of list (row)
	#print res[1] is list of attributes
	return res
