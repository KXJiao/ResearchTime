import time
import string
from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer
from  nltk.tokenize import sent_tokenize
from nltk.stem import PorterStemmer
import re
import math

def addOne(dic,k):
	if k in dic.keys():
		temp=dic[k]
		temp+=1
		dic[k]=temp
	else:
		dic[k]=1

start = time.time()
words=open("subInfo.txt").read()
sents=open("subInfo.txt").readlines()

bioTerms=open("chemTerms.txt").readlines()
bioTerms=[t.strip().lower() for t in bioTerms]
bioPhrases=[term for term in bioTerms if " " in term]
phsWords=[]
for ph in bioPhrases:
	a = re.search(r"\b(?=\w)" + re.escape(ph) + r"\b(?!\w)",words,re.IGNORECASE)
	while a is not None:
		words=words[:a.start()]+words[a.end():]
		phsWords.append(ph)		
		a = re.search(r"\b(?=\w)" + re.escape(ph) + r"\b(?!\w)",words,re.IGNORECASE)

tknzr = TweetTokenizer()
words=tknzr.tokenize(words)
words=words+phsWords
words=[w.lower() for w in words if not w in string.punctuation]
#words = [w[0].lower()+w[1:] if w[0].lower()+w[1:] in model.vocab else w for w in words]
stop_words = set(stopwords.words('english'))
words = [w for w in words if not w in stop_words]
words = [w for w in words if len(w)>1 or w in string.ascii_letters or w in string.digits]
setWords=set(words)
setWords=list(setWords)

### Algorithm ###
keyTerms=[t for t in setWords if t in bioTerms]
freqDic={}
wToStem={}
ps = PorterStemmer()
for t in words:
	stem=ps.stem(t)
	addOne(freqDic,stem)
	wToStem[t]=stem
# calculation for avg. freq.
freqArr=[freqDic[k] for k in freqDic.keys()]
tot=sum(freqArr)
avgFreq=tot/(len(freqArr))
###
# context calculation
#print(keyTerms)
contDic={}
for t in setWords:
	if t in keyTerms:
		contDic[t]=1
	else:
		contDic[t]=.5
# finding the importance of each term
termVal={}
for t in setWords:
	#termVal[t]=(1+contDic[t])*math.pow(avgFreq,4) * 0+ (freqDic[wToStem[t]]-avgFreq)*1  #Vary results by changing factors
	termVal[t]=contDic[t] * 15+ (freqDic[wToStem[t]]-avgFreq)*1
	#termVal[t]=contDic[t]*freqDic[wToStem[t]]
	#print(t+": "+ str(contDic[t]*12)+ " + "+ str(freqDic[wToStem[t]]-avgFreq) + " ("+wToStem[t]+": "+str(freqDic[wToStem[t]])+")")
'''
dicCopy = dict(termVal)
termScoreArr=[]
while dicCopy.keys():
	maxNum=-math.inf
	for i in dicCopy.keys():
		if dicCopy[i]>maxNum:
			maxNum=dicCopy[i]
			corTerm=i
	termScoreArr.append((corTerm,maxNum))
	del dicCopy[corTerm]

print(termScoreArr[:10])
print()
'''
###
#finding important sentences
sentScoreDic={}
sents=[sent_tokenize(s.strip()) for s in sents]
tempSents=[]
for arr in sents:
	tempSents+=arr
sents=tempSents
for sen in sents:
	if sen[-1]=='.' or sen[-1]=='?' or sen[-1]=='!' or sen[-1]=='"':
		sentScore=0
		hitCount=0
		for t in setWords:
			hits=[m.start() for m in re.finditer(r"\b" +re.escape(t)+r"\b", sen, re.IGNORECASE)]
			#sentScore+=len(hits)*termVal[t]
			if len(hits)>0:
				hitCount+=1
				sentScore+=termVal[t]
		if hitCount>0:
			sentScoreDic[sen]=sentScore-(hitCount*2)
		else:
			sentScoreDic[sen]=0

dicCopy = dict(sentScoreDic)
sentScoreArr=[]
while dicCopy.keys():
	maxNum=-math.inf
	for i in dicCopy.keys():
		if dicCopy[i]>maxNum:
			maxNum=dicCopy[i]
			corSent=i
	sentScoreArr.append((corSent,maxNum))
	del dicCopy[corSent]
# output 
numPoints=5
keyPoints=sentScoreArr[:numPoints]
orderedKP=[]
for kp in keyPoints:
	orderedKP.append((sents.index(kp[0]),kp[0]))
orderedKP=sorted(orderedKP)
for i in orderedKP:
	print(i[1])
	print()
# time taken
end=time.time()-start
print("time: "+ str(end))