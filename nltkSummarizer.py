from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer
import textract
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

ps = PorterStemmer()
#text=open("subInfo.txt").read()
t = filedialog.askopenfilename()
text = textract.process(t).decode("utf-8")

stopWords = set(stopwords.words("english"))
words = word_tokenize(text)

freqTable = dict()
for word in words:
    word = word.lower()
    word=ps.stem(word)
    if word in stopWords:
        continue
    if word in freqTable:
        freqTable[word] += 1
    else:
        freqTable[word] = 1

sentences = sent_tokenize(text)
totAvg=0
#print(sentences)
sentenceValue = dict()
for sentence in sentences:
	senWords=word_tokenize(sentence)
	for i in range(len(senWords)):
		senWords[i]=senWords[i].lower()
		senWords[i]=ps.stem(senWords[i])
	counter=0
	while counter < len(senWords):
		if senWords[counter] in stopWords:
			senWords=senWords[:counter]+senWords[counter+1:]
		else:
			counter+=1
	sentenceValue[sentence]=0
	for w in senWords:
		sentenceValue[sentence]+=freqTable[w]
	sentenceValue[sentence]=sentenceValue[sentence]/len(senWords)
	totAvg+=sentenceValue[sentence]

ansArr=[]
while sentenceValue.keys():
	maxNum=0
	corSen=""
	for i in sentenceValue.keys():
		if sentenceValue[i]>maxNum:
			maxNum=sentenceValue[i]
			corSen=i
	ansArr.append((corSen,maxNum))
	del sentenceValue[corSen]

for i in ansArr:
	print(i)
