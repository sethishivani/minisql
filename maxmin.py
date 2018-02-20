import populatedata as pd
def maxm(data,datattname,dispatt,perf):
	#feilds are data rep list of list having all att, datattname rep att of the data, dispatt rep the att to be disp
	loc=0
	for i in datattname:
		if i==dispatt[0]:
			break
		loc+=1 
	if("max"==perf):
		maxx=(float)(data[0][loc])
		for i in data:
			if(maxx<(float)(i[loc])):
				maxx=(float)(i[loc])
		print float("{0:.2f}".format(maxx))
	elif("min"==perf):
		minn=(float)(data[0][loc])
		for i in data:
			if(minn>(float)(i[loc])):
				minn=(float)(i[loc])
		print float("{0:.2f}".format(minn))
	elif("avg"==perf):
		av=0.0
		cnt=0.0
		for i in data:
			av+=(float)(i[loc])
			cnt+=1
		av=av/cnt
		print float("{0:.2f}".format(av))
	elif("sum"==perf):
		sm=0
		for i in data:
			sm+=(float)(i[loc])
		print float("{0:.2f}".format(sm))
	else:
		print "undefined aggregate function"
