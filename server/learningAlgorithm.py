SpaceDimensions=["abstract","try","use","#oneCharacter","research","learn","you",
                 '#"',"comparison","#_","conclusion","computer","algorithm","see",
                 "internet","web","code","tool","api","software","server"]
def MapToEvalVS(bag):
    v=[]
    total=0
    for w in bag:
        total+=bag[w];
    for w in SpaceDimensions:
        if(bag.has_key(w) and total!=0):
            v.append(bag[w]*1.0/total)
        else:
            v.append(0)
    return v;
