import pickle
from learningAlgorithm import ToVS
from learningAlgorithm import learn
from learningAlgorithm import predict
from inputReading import scrapeFolder
from inputReading import scrapeMain
from inputReading import scrapeWeb
from inputReading import scrapePDF

def WordCount(docs):
    words=dict()
    total=0
    for d in docs:
        for w in d.keys():
            if(words.has_key(w)):
                words[w]+=d[w]
            else:
                words[w]=d[w]
            total+=d[w]
    for w in words.keys():
        words[w]=words[w]*1.0/total
    return words

def WordCountM(docSet):
    total=0
    words=dict()
    for docs in docSet:
        for d in docs:
            for w in d.keys():
                if(words.has_key(w)):
                    words[w]+=d[w]
                else:
                    words[w]=d[w]
                total+=d[w]
    for w in words.keys():
        words[w]=words[w]*1.0/total
    return words
    
def SortByDivision(ss,cs):
    items=ss.items()
    return sorted(ss.items(),key=lambda item: (-1.0*item[1]/cs[item[0]], item[0]))

def PrintMostDistinguishingFeatures(ss,cs):
    print("--------------------------")
    for i in range(100):
        print(ss[i][0], ss[i][1],ss[i][1]/cs[ss[i][0]])
    print("--------------------------")

def compareVals(key):
    return hWC[key]/tWC[key],wWC[key]/tWC[key],pWC[key]/tWC[key]
    
    
#print 1
#hS=scrapeFolder("../410project/www.huffingtonpost.com", scrapeMain, ToVS)
#print 2
#wS=scrapeFolder("../410project/www.w3schools.com", scrapeMain, ToVS)
#print 3
#wS=wS+scrapeFolder("../410project/pdfTutorial", scrapePDF, ToVS)
#print 4
#wS=wS+scrapeFolder("../410project/otherTutorial", scrapeWeb, ToVS)
#print 5
#pS=scrapeFolder("../410project/research",scrapePDF, ToVS)
#pickle_file = open('data.p', 'wb')
#pickle.dump([hS, wS, pS], pickle_file)
#pickle_file.close()

if __name__ == '__main__':
    pickle_file = open('data.p', 'rb')
    arr = pickle.load(pickle_file)
    hS = arr[0]
    wS = arr[1]
    pS = arr[2]
    pickle_file.close()

    #print("Scrape - Finished")
    #hWC=WordCount(hS)
    #wWC=WordCount(wS)
    #pWC=WordCount(pS)
    #print("Partial Count - Finished")
    #tWC=WordCountM([hS, wS, pS])
    #print("Finished")
    #hB=SortByDivision(hWC,tWC)
    #wB=SortByDivision(wWC,tWC)
    #pB=SortByDivision(pWC,tWC)
    #print("Huffington:")
    #PrintMostDistinguishingFeatures(hB,tWC)
    #print("W3School:")
    #PrintMostDistinguishingFeatures(wB,tWC)
    #print("Research:")
    #PrintMostDistinguishingFeatures(pB,tWC)

    print 'STARTING MODEL CREATION'
    model_file =  open('svm_model.p', 'wb')
    pickle.dump(learn(hS,wS,pS), model_file)
    model_file.close()
