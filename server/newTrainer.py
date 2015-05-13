import pickle
from learningAlgorithm2 import learnPipe
from learningAlgorithm2 import learnOnlineLearner
from inputReading import scrapeFolder
from inputReading import scrapeMain
from inputReading import scrapeWeb
from inputReading import scrapePDF
from learningAlgorithm2 import normalize_text
    
def do_nothing(v):
    return v

def save_model(cat1,cat2,cat3,ft,lt,f):
    with open(ft+'_'+lt+'_model.p', 'wb') as pickle_file:
        pickle.dump(f(cat1,cat2,cat3,ft,lt), pickle_file)

if __name__ == '__main__':
    print 1
    hS=scrapeFolder("../410project/www.huffingtonpost.com", scrapeMain, do_nothing)
    print 2
    wS=scrapeFolder("../410project/www.w3schools.com", scrapeMain, do_nothing)
    print 3
    wS=wS+scrapeFolder("../410project/pdfTutorial", scrapePDF, do_nothing)
    print 4
    wS=wS+scrapeFolder("../410project/otherTutorial", scrapeWeb, do_nothing)
    print 5
    pS=scrapeFolder("../410project/research",scrapePDF, do_nothing)

    hS=[normalize_text(d) for d in hS]
    wS=[normalize_text(d) for d in wS]
    pS=[normalize_text(d) for d in pS]
    
    for ft in ["tfidf","tf","bw","hashing"]:
        for lt in ["svm","svm_ava","knn"]:
            save_model(hS,wS,pS,ft,lt,learnPipe)
        for lt in ["sgd","multinomial_nb","passive_aggresive","perceptron"]:
            save_model(hS,wS,pS,ft,lt,learnOnlineLearner)
