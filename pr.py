import math
def count(file):
	i = 0
	d = {}
	for a in file:
		i = i + 1
		d[a.split('\n')[0].split(" ")[0]] = 1
	return i,d
def sink_set():
	file_out_link = open("out_test.txt","r")
	sink_set = []
	for a in file_out_link:
		if(len(a.split("\n")[0].split(" ")) <= 2):
			sink_set.append(a[0])
	sink = 0
	for a in sink_set:
		sink = sink + d[a]
	return sink
def sink_num():
	file_out_link = open("out_test.txt","r")
	d = {}
	for a in file_out_link:
		count = 0
		length = len(a.split("\n")[0].split(" "))
		d[a.split("\n")[0].split(" ")[0]] = length - 2
	return d
def perp(d):
	en = 0
	for a in d:
		en += d[a]*math.log(2,d[a])
	per = 2**(en*(-1.0))
	return per
def pr():
	file = open("test.txt",'r')
	(N,d) = count(file)
	file.close()
	for a in d:
		d[a] = 1.0/N
	sink = sink_set()
	time = 0
	present = 9999
	count_1 = 1
	while(time<=4):
		print count_1
		count_1 += 1
		new_d = {}
		pre = present
		out_num = sink_num()
		file_in_link = open("test.txt","r")
		for a in file_in_link:
			new_d[a.split("\n")[0].split(" ")[0]] = (1-0.85)/N
			new_d[a.split("\n")[0].split(" ")[0]] += 0.85*sink/N
			b = a.split("\n")[0].split(" ")[1:]
			for item in b:
				new_d[a.split("\n")[0].split(" ")[0]] += 0.85*d[item]/out_num[item]
		d = new_d
		present = perp(d)
		if(abs(present-pre)<1.0):
			time += 1
	return d
d = pr()
print d



