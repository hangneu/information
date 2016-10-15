import math
def count(file):
	i = 0
	d = {}
	for a in file:
		i = i + 1
		d[a.split('\n')[0].split(" ")[0]] = 1
	return i,d
def sink_set(out_link):
	file_out_link = open(out_link,"r")
	sink_set = []
	for a in file_out_link:
		if(len(a.split("\n")[0].split(" ")) <= 2):
			sink_set.append(a[0])
	sink = 0
	for a in sink_set:
		sink = sink + d[a]
	return sink
def sink_num(out_link):
	file_out_link = open(out_link,"r")
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
def pr(in_link,out_link):
	file = open(in_link,'r')
	(N,d) = count(file)
	file.close()
	for a in d:
		d[a] = 1.0/N
	sink = sink_set(out_link)
	time = 0
	present = 9999
	count_1 = 1
	while(time<=4):
		print count_1
		count_1 += 1
		new_d = {}
		pre = present
		out_num = sink_num(out_link)
		file_in_link = open(in_link,"r")
		for a in file_in_link:
			new_d[a.split("\n")[0].split(" ")[0]] = (1-0.85)/N
			new_d[a.split("\n")[0].split(" ")[0]] += 0.85*sink/N
			b = a.split("\n")[0].split(" ")
			if (in_link!="test.txt"):
				b = b[1:len(b)-1]
			else:
				b = b[1:]
			for item in b:
				new_d[a.split("\n")[0].split(" ")[0]] += 0.85*d[item]/out_num[item]
		d = new_d
		present = perp(d)
		if(abs(present-pre)<1.0):
			time += 1
	return d
in_link = "test.txt"
out_link = "out_test.txt"
in_1000 = "ass_first.txt"
out_1000 = "out_link_1000.txt"
d = pr(in_1000,out_1000)
# d = pr(in_link,out_link)
dict1 = sorted(d.iteritems(),key=lambda d:d[1],reverse = True)
for item in dict1:
	print item














