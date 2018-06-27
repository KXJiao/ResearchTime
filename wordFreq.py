from nltk.tag import pos_tag
file=open("subInfo.txt").read().lower().split()
nFile=[]
for word in file:
	cleanWord = ""
	for char in word:
		if char in '!,.?":()[];0123456789':
			char = ""
		cleanWord += char
	if cleanWord !="":
		nFile.append(cleanWord)

tagArr=pos_tag(nFile)
ansDic={}
ansArr=[]
def add(dic,k):
	if k in dic.keys():
		temp=dic[k]
		temp+=1
		dic[k]=temp
	else:
		dic[k]=1

for dup in tagArr:
	if dup[1]=="NN":
		add(ansDic,dup[0])

while ansDic.keys():
	maxNum=0
	corWord=""
	for i in ansDic.keys():
		if ansDic[i]>maxNum:
			maxNum=ansDic[i]
			corWord=i
	ansArr.append((corWord,maxNum))
	del ansDic[corWord]

for i in ansArr:
	print(i)