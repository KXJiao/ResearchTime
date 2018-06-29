from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer
import textract
import tkinter as tk
from tkinter import filedialog

def summary(text):
    stopWords = set(stopwords.words("english"))
    words = word_tokenize(text)

    ps = PorterStemmer()

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
    ansArr2=[]
    while sentenceValue.keys():
       maxNum=0
       corSen=""
       for i in sentenceValue.keys():
         if sentenceValue[i]>maxNum:
          maxNum=sentenceValue[i]
          corSen=i
       ansArr.append((corSen,maxNum))
       ansArr2.append(corSen)
       del sentenceValue[corSen]

    #for i in ansArr:
    #    print(i)
    return (ansArr,' '.join(ansArr2))


root = tk.Tk()
root.withdraw()

numFiles = int(input("Enter number of files to compare: "))
files = []
if numFiles > 0:
    for i in range(numFiles):
       files.append(textract.process(filedialog.askopenfilename(title = "File number " + str(i + 1))).decode("utf-8").replace('\n',' '))

fileComp = []
for file in files:
    fileComp.append(summary(file)[1])

for i in summary(' '.join(fileComp))[0]:
    print(i)
