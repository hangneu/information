def extract(test):
	result = open(test,'r')
	out = []
	for a in result:
		tem = []
		tem.append(a.split('\n')[0].split(" ")[0]) 
		out.append(tem)
	result.close()
	return out
def ind(result,string):
	b = 0
	for a in result:
		if(a[0] == string):
			return b
		b = b + 1
def in_to_out(text):
	res = extract(text)
	file = open(text,"r")
	for a in file:
		for i in range(1,len(a.split("\n")[0].split(" "))):#for i in range(1,len(a.split("\n")[0].split(" "))-1):
			res[ind(res,a.split("\n")[0].split(" ")[i])].append(a.split("\n")[0].split(" ")[0])
	return res
def in_out_tran(text,outp):
	b = in_to_out(text)
	sed = open(outp,"w")
	for a in b:
		for item in a:
			sed.write(item+" ")
		sed.write("\n")
	sed.close()
text = "test.txt"
outp = "out_test.txt"
in_out_tran(text,outp)