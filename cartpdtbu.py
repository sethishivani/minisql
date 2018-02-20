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
	temp=[]
	res=[]
	count=0
	index=1
	for i in tn:
		for x in data[i]:
			attlist.append(x)
		temp.append(rowlist(data[i]))
		count+=1
		if(count==2):
			count=1
			for i in temp[0]:
				for j in temp[1]:
					res.append(i+j)
	for i in res:
		print i
			
