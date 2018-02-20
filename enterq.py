import sys
import querypro as qp
import populatedata as pd
import maxmin as mm
import dist as d
import project as p
import cartpdt as cp

andlist=[]
orlist=[]
finval=[]
perf="not"
dist=0
dilist=[]
########################################################################################################
###########a function to display selected cols i.e. tab1.a,tab2.b,tab1.c############
def coldisp(data,datattname,dispatt):
	#feilds are data rep list of list having all att, datattname rep att of the data, dispatt rep the att to be disp
	if dist==1:
		counter=0
		for i in data:	
			temp=[]
			for j in dispatt:
				cnt=0
				for k in datattname:
					if j==k:
						temp.append(i[cnt])
					cnt+=1
			dilist.append(temp)
		d.ddata(dilist,dispatt)


	else:
		if perf=="not" :
			if dispatt=='*':
				dispatt=datattname[:]
			cnt=1
			for i in dispatt:
				print i,
				if cnt<len(dispatt):
					print ",",
				cnt+=1
			print ""
			for i in data:	
				x=1	
				for j in dispatt:
					cnt=0
					for k in datattname:
						if j==k:
							print i[cnt],
							if x<len(dispatt):
								print ',',
						cnt+=1
					x+=1
				print ""
		else:
			mm.maxm(data,datattname,dispatt,perf)


########################################################################################################
def andcal(l1,l2):
	finval=[]
	for i in l1:
		if i in l2:
			finval.append(i)
	return finval
########################################################################################################
def orcal(l1,l2):
	finval=[]
	for i in l1:
		finval.append(i)
	for i in l2:	
		if i not in finval:
			finval.append(i)
	return finval
	
####################to convert A to table1.A######################
def attwithtn(condt,tn,data):
	for i in tn:
		for j in data[i]:
			if condt[0]==j:
				condt[0]=i+'.'+j
	return condt
########################################################################################################
##########################################check where condition##############################
def wherecondt(data,datattname,condt,op):
	#data is list of list,datattname is the list of att in data,condt is list condt[1] is attname condt[2] 
	#is value,op is operation to be performed
	res=[]
	loc=0
	#########fetching the location of attribute#########
	for i in datattname:
		if i==condt[0]:
			break
		loc+=1
	if op=="=":
		for i in data:
			if i[loc]==condt[1]:
				res.append(i)
		print res
	elif op=="<=":
		for i in data:
			if i[loc]<=condt[1]:
				res.append(i)
	elif op==">=":
		for i in data:
			if i[loc]>=condt[1]:
				res.append(i)
	elif op=="!=":
		for i in data:
			if i[loc]!=condt[1]:
				res.append(i)
	elif op=="<":
		for i in data:
			if i[loc]<condt[1]:
				res.append(i)
	elif op==">":
		for i in data:
			if i[loc]>condt[1]:
				res.append(i)
	return res

########################################################################################################
##########################################check where condition##############################
def wherejoin(data,datattname,condt,op):
	#data is list of list,datattname is the list of att in data,condt is list condt[1] is attname condt[2] 
	#is value,op is operation to be performed
	res=[]
	loc1=0
	loc2=0
	###############extracting table names################
	#########fetching the location of attribute#########
	for i in datattname:
		if i==condt[0]:
			break
		loc1+=1
	for i in datattname:
		if i==condt[1]:
			break
		loc2+=1
	tlist=[]
	if op=="=":
		for i in data:
			count=0
			tlist=[]
			if i[loc1]==i[loc2] and i not in res:
				for j in i:
					if not count==loc2:
						tlist.append(j)
					count+=1
				res.append(tlist)
	elif op=="<=":
		for i in data:
			if i[loc1]<=i[loc2] and i not in res:
				res.append(i)
	elif op==">=":
		for i in data:
			if i[loc1]>=i[loc2] and i not in res:
				res.append(i)
	elif op=="!=":
		for i in data:
			if i[loc1]!=i[loc2] and i not in res:
				res.append(i)
	elif op=="<":
		for i in data:
			if i[loc1]<i[loc2] and i not in res:
				res.append(i)
	elif op==">":
		for i in data:
			if i[loc1]>i[loc2] and i not in res:
				res.append(i)
	return res

########################################################################################################
#query=sys.argv[1]
proq=qp.pquery(sys.argv[1])
st=str(proq)
#fetches populated dat list
data=pd.tabdata()
############################# no distinct ######################
if not("distinct" in st):
	noatt=proq[1].split(',')
	tabinp=proq[3]
	tn=tabinp.split(',')
	#####################################################################################################
	#############case of multiple tables and single table with single where and without where################
	if len(tn)>1:
		ll=cp.cartesian(data,tn)
	else:
		ll=p.proj(data,noatt,proq[3],"display")
		
		#print ll[1]
	attname=ll[1][:]
	disp=proq[1].split(',')
	if proq[1][:3]=="max" or proq[1][:3]=="min" or proq[1][:3]=="sum" or proq[1][:3]=="avg":
 	#fun to perform:0, attribute:1, table:2
	 	perf=proq[1][:3]
	 	disp=[proq[1][4:-1]]
	if disp[0]=='*':
		disp=attname[:]
	count=0
	for i in disp:
		if(len(i.split('.'))==1):
			for j in attname:
				task=j.split('.')
				if(task[1]==i):
					disp[count]=j
		count+=1
	orflag=0
	andflag=0
	rescount=0
	if(len(proq)>=5):
		multicdt=[]
		reslist=[]
		condt=proq[4][6:]
		if "OR" in condt:
			orflag=1
			multicdt=condt.split("OR")
		elif "AND" in condt:
			andflag=1
			multicdt=condt.split("AND")
		else:
			multicdt.append(condt)
		loop=0
		while loop<len(multicdt):
			if "<=" in multicdt[loop]:
				cdlist=multicdt[loop].split('<=')
				if len(cdlist[0].split("."))==1:
					cdlist=attwithtn(cdlist,tn,data)
				if len(cdlist[0].split("."))==2 and len(cdlist[1].split("."))==2:
					res=wherejoin(ll[0],attname,cdlist,"<=")
				else:
					res=wherecondt(ll[0],attname,cdlist,"<=")
			elif ">=" in multicdt[loop]:
				cdlist=multicdt[loop].split('>=')
				if len(cdlist[0].split("."))==1:
					cdlist=attwithtn(cdlist,tn,data)
				if len(cdlist[0].split("."))==2 and len(cdlist[1].split("."))==2:
					res=wherejoin(ll[0],attname,cdlist,">=")
				else:
					res=wherecondt(ll[0],attname,cdlist,">=")
			elif "!=" in multicdt[loop]:
				cdlist=multicdt[loop].split('!=')
				if len(cdlist[0].split("."))==1:
					cdlist=attwithtn(cdlist,tn,data)
				if len(cdlist[0].split("."))==2 and len(cdlist[1].split("."))==2:
					res=wherejoin(ll[0],attname,cdlist,"!=")
				else:
					res=wherecreslistondt(ll[0],attname,cdlist,"!=")
			elif "<" in multicdt[loop]:
				cdlist=multicdt[loop].split('<')
				if len(cdlist[0].split("."))==1:
					cdlist=attwithtn(cdlist,tn,data)
				if len(cdlist[0].split("."))==2 and len(cdlist[1].split("."))==2:
					res=wherejoin(ll[0],attname,cdlist,"<")
				else:
					res=wherecondt(ll[0],attname,cdlist,"<")
			elif ">" in multicdt[loop]:
				cdlist=condt.split('>')
				if len(cdlist[0].split("."))==1:
					cdlist=attwithtn(cdlist,tn,data)
				if len(cdlist[0].split("."))==2 and len(cdlist[1].split("."))==2:
					res=wherejoin(ll[0],attname,cdlist,">")
				else:
					res=wherecondt(ll[0],attname,cdlist,">")
				#print res
			elif "=" in multicdt[loop]:
				cdlist=multicdt[loop].split('=')
				if len(cdlist[0].split("."))==1:
					cdlist=attwithtn(cdlist,tn,data)
				if len(cdlist[0].split("."))==2 and len(cdlist[1].split("."))==2:
					res=wherejoin(ll[0],attname,cdlist,"=")
				else:
					res=wherecondt(ll[0],attname,cdlist,"=")
			loop+=1
			# print res
			# print "#############################"
			reslist.append(res)
			#print reslist
			rescount+=1
			if rescount==2:
				if orflag==1:
					reslist=orcal(reslist[0],reslist[1])
					orflag=0
				if andflag==1:
					reslist=[andcal(reslist[0],reslist[1])]
					andflag=0
				rescount=1
			res=reslist[0]
			#print res

	else:
		res=ll[0]
	if disp=='*':
		disp=attname[:]
	coldisp(res,attname,disp)
###############################distinct is there############################
if ("distinct" in st):
	dist=1
	noatt=proq[2].split(',')
	tabinp=proq[4]
	tn=tabinp.split(',')
	#####################################################################################################
	#############case of multiple tables and single table with single where and without where################
	if len(tn)>1:
		ll=cp.cartesian(data,tn)
	else:
		ll=p.proj(data,noatt,proq[4],"display")
		
		#print ll[1]
	attname=ll[1][:]
	disp=proq[2].split(',')
	if disp[0]=='*':
		disp=attname[:]
	count=0
	for i in disp:
		if(len(i.split('.'))==1):
			for j in attname:
				task=j.split('.')
				if(task[1]==i):
					disp[count]=j
		count+=1
	orflag=0
	andflag=0
	rescount=0
	if(len(proq)>=6):
		multicdt=[]
		reslist=[]
		condt=proq[5][6:]
		if "OR" in condt:
			orflag=1
			multicdt=condt.split("OR")
		elif "AND" in condt:
			andflag=1
			multicdt=condt.split("AND")
		else:
			multicdt.append(condt)
		loop=0
		while loop<len(multicdt):
			if "<=" in multicdt[loop]:
				cdlist=multicdt[loop].split('<=')
				if len(cdlist[0].split("."))==1:
					cdlist=attwithtn(cdlist,tn,data)
				if len(cdlist[0].split("."))==2 and len(cdlist[1].split("."))==2:
					res=wherejoin(ll[0],attname,cdlist,"<=")
				else:
					res=wherecondt(ll[0],attname,cdlist,"<=")
			elif ">=" in multicdt[loop]:
				cdlist=multicdt[loop].split('>=')
				if len(cdlist[0].split("."))==1:
					cdlist=attwithtn(cdlist,tn,data)
				if len(cdlist[0].split("."))==2 and len(cdlist[1].split("."))==2:
					res=wherejoin(ll[0],attname,cdlist,">=")
				else:
					res=wherecondt(ll[0],attname,cdlist,">=")
			elif "!=" in multicdt[loop]:
				cdlist=multicdt[loop].split('!=')
				if len(cdlist[0].split("."))==1:
					cdlist=attwithtn(cdlist,tn,data)
				if len(cdlist[0].split("."))==2 and len(cdlist[1].split("."))==2:
					res=wherejoin(ll[0],attname,cdlist,"!=")
				else:
					res=wherecreslistondt(ll[0],attname,cdlist,"!=")
			elif "<" in multicdt[loop]:
				cdlist=multicdt[loop].split('<')
				if len(cdlist[0].split("."))==1:
					cdlist=attwithtn(cdlist,tn,data)
				if len(cdlist[0].split("."))==2 and len(cdlist[1].split("."))==2:
					res=wherejoin(ll[0],attname,cdlist,"<")
				else:
					res=wherecondt(ll[0],attname,cdlist,"<")
			elif ">" in multicdt[loop]:
				cdlist=condt.split('>')
				if len(cdlist[0].split("."))==1:
					cdlist=attwithtn(cdlist,tn,data)
				if len(cdlist[0].split("."))==2 and len(cdlist[1].split("."))==2:
					res=wherejoin(ll[0],attname,cdlist,">")
				else:
					res=wherecondt(ll[0],attname,cdlist,">")
				#print res
			elif "=" in multicdt[loop]:
				cdlist=multicdt[loop].split('=')
				if len(cdlist[0].split("."))==1:
					cdlist=attwithtn(cdlist,tn,data)
				if len(cdlist[0].split("."))==2 and len(cdlist[1].split("."))==2:
					res=wherejoin(ll[0],attname,cdlist,"=")
				else:
					res=wherecondt(ll[0],attname,cdlist,"=")
			loop+=1
			# print res
			# print "#############################"
			reslist.append(res)
			#print reslist
			rescount+=1
			if rescount==2:
				if orflag==1:
					reslist=orcal(reslist[0],reslist[1])
					orflag=0
				if andflag==1:
					reslist=[andcal(reslist[0],reslist[1])]
					andflag=0
				rescount=1
			res=reslist[0]
			#print res

	else:
		res=ll[0]
	if disp=='*':
		disp=attname[:]
	coldisp(res,attname,disp)