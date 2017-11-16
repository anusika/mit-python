#Problem Set 3
#Name: Anusika Nijher
#Collaborators: None
#Problem 1!!
#Time 1:15
from string import *

def countSubStringMatch(target,key):
    assert len(key) < len(target)
    count = 0;
    start = 0;
    while(start > -1):
        start = find(target,key,start)
        if(start == -1):
            break;
        else:
            print "the index",key, "starts at is:", find(target,key,start);
            start = start + len(key);
            count = count + 1;
    return count


##print countSubStringMatch("ilovecakeilovecake", "cake");
##print countSubStringMatch("atgacatgcacaagtatgcat", "cake");
##print countSubStringMatch("atgacatgcacaagtatgcat", "a");

def countSubStringMatchRecursive(target, key):
    assert len(key) < len(target)
    count = 0;
    start = 0;
    start = find(target,key,start)
    if(start!=-1):
        count = count + 1
        start = start + len(key)
        count += countSubStringMatchRecursive(target[start:], key)
    return count

                                              
##print countSubStringMatchRecursive("ilovecakeilovecake", "cake");
##print countSubStringMatchRecursive("atgacatgcacaagtatgcat", "cake");
##print countSubStringMatchRecursive("atgacatgcacaagtatgcat", "a");
##print countSubStringMatchRecursive("atgacatgcacaagtatgcat", "agt");

#Problem 2
#Time: 10min

def subStringMatchExact(target,key):
    assert len(key) < len(target)
    awesome_tuple = () 
    start = 0 
    while (find(target, key, start) >= 0):
            start = find(target, key, start)
            awesome_tuple = awesome_tuple + (start, )
            start = start + 1
    return awesome_tuple 

##print subStringMatchExact("ilovecakeilovecake", "cake")
##print subStringMatchExact("atgacatgcacaagtatgcat", "cake")   
##print subStringMatchExact("atgacatgcacaagtatgcat", "a")
##print subStringMatchExact("atgacatgcacaagtatgcat", "at")
##print subStringMatchExact("atgacatgcacaagtatgcat", "atg")
##print subStringMatchExact("atgacatgcacaagtatgcat", "atgca") 
##print subStringMatchExact("atgaatgcatggatgtaaatgcag", "a")
##print subStringMatchExact("atgaatgcatggatgtaaatgcag", "at")
##print subStringMatchExact("atgaatgcatggatgtaaatgcag", "atg")
##print subStringMatchExact("atgaatgcatggatgtaaatgcag", "atgca")

#Problem 3
#Time: 45 min
#Honestly Messed up calling function and took me about 10 min to figure that out
#Put key where target should have been. 

def constrainedMatchPair (firstMatch,secondMatch, m):
    answer = ()
    for n in firstMatch:
            for k in secondMatch:
                    if n + m + 1 == k:
                            answer = answer + (n,)
    return answer
    
def subStringMatchOneSub(key,target):
    assert len(key) < len(target)
    answers ={}
    possible=[]
    allAnswers = ()
    for miss in range(0,len(key)):
        key1 = key[:miss]
        key2 = key[miss+1:]
        match1 = subStringMatchExact(target,key1)
        match2 = subStringMatchExact(target,key2)
        filtered = constrainedMatchPair(match1,match2,len(key1))
        allAnswers = allAnswers + filtered
    for i in allAnswers:
        if i not in possible:
            possible.append(i)
    for i in possible:
            answers.update({i:target[i:i +len(key)]})
    return answers

##print subStringMatchOneSub("atgca","atgaatgcatggatgtaaatgcag")
##print subStringMatchOneSub("atg","atgaatgcatggatgtaaatgcag")
##print subStringMatchOneSub("atgc","atgaatgcatggatgtaaatgcag")
##print subStringMatchOneSub("cake","atgaatgcatggatgtaaatgcag")
##print subStringMatchOneSub("cake","cakecale")

#Problem 4
#Time 10min
def subStringMatchExactlyOneSub(key,target):
    assert len(key) < len(target)
    print key
    print target
    no_repeats = {}
    answers = subStringMatchOneSub(key,target)
    for a in answers:
        if(answers[a] != key):
            no_repeats.update({a:answers[a]})
    return no_repeats

##print subStringMatchExactlyOneSub("cake","cakecale")
##print subStringMatchExactlyOneSub("atgca","atgaatgcatggatgtaaatgcag")
##print subStringMatchExactlyOneSub("atg","atgaatgcatggatgtaaatgcag")
##print subStringMatchExactlyOneSub("atgc","atgaatgcatggatgtaaatgcag")
##print subStringMatchExactlyOneSub("cake","atgaatgcatggatgtaaatgcag")
