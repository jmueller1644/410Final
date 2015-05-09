import re
from cStringIO import StringIO
from stemming.porter2 import stem
import string
from sklearn import svm

ByUs=["abstract","try","use","#oneCharacter","research","learn","you",
                 '#"',"comparison","#_","conclusion","computer","algorithm","see",
                 "internet","web","code","tool","api","software","server"]


def ToVS(text):
    VS=dict()
    text=text.lower();
    
    VS["#!"]=len(re.findall("!",text))
    VS["#?"]=len(re.findall("\\?",text))
    VS["#()"]=len(re.findall("\\(|\\)",text))
    VS["#numbers"]=len(re.findall("\\d+",text))
    VS["##"]=len(re.findall("#",text))
    VS["#{}"]=len(re.findall("\\{|\\}",text))
    VS["#[]"]=len(re.findall("\\[|\\]",text))
    VS["#comparison"]=len(re.findall("<|>|=",text))
    VS['#"']=len(re.findall('"',text))
    VS['#math']=len(re.findall('\\+|\\-|\\*|\\/',text))
    VS['#_']=len(re.findall('_',text))
    VS['#oneCharacter']=0
    for c in string.punctuation:
        if c!="-" and c!="_":
            text=text.replace(c," ");
        else:
            text=text.replace(c,"");
    text=stem(re.sub("[\\s|\\d]+"," ",text));
    text=filter(lambda x: x in string.printable, text)
    for word in text.split(" "):
        if word!="":
            if len(word)==1:
                VS["#oneCharacter"]+=1
            elif VS.has_key(word):
                VS[word]+=1;
            else:
                VS[word]=1;
    return VS;

def MapToEvalVS(bag):
    v=[]
    total=0
    for w in bag:
        total+=bag[w];
    for w in ByUs:
        if(bag.has_key(w) and total!=0):
            v.append(bag[w]*1.0/total)
        else:
            v.append(0)
    return v;

def learn(cat1,cat2,cat3):
    X = []
    Y = []
    for d in cat1:
        X.append(MapToEvalVS(d));
        Y.append(0)
    for d in cat1:
        X.append(MapToEvalVS(d));
        Y.append(1)
    for d in cat3:
        X.append(MapToEvalVS(d));
        Y.append(2)
    clf = svm.SVC()
    clf.fit(X, Y)
    return clf

def predict(learner,doc):
    return learner.predict(MapToEvalVS(ToVS(doc)))
