#Problem Set 2
#Name: Anusika Nijher
#Collaborators: None
#Problem 1!!
#Time 1:30

def test(x):
    d = int((x/20) + 2)
    e = int((x/9) + 2)
    f = int((x/6) + 2)
    for c in range(0,d):
        for b in range(0,e):
            for a in range(0,f):
                nuggets = 6*a+9*b+20*c
                if nuggets == x:
                    print a, "boxes of 6", b, "boxes of 9", c, "boxes of 20"
                    break
                else:
                    pass
for x in range(50, 66):
    print x
    test(x)
    print ' '

#Problem 2!
#Had to find and read online but the answer I found helped me with the
#the rest of the problem set:
#For this type of problem,
#if you can find a string of sequential numbers that is
#as long as the smallest counting unit then you can count
    
#to any subsequent number by adding this smallest counting unit
#a member of this base sequential series. Wow. 

#Problem 3!
#Time 1 hr
possible_list=[];
largest=[];
for x in range(1,100):
    d = int((x/20) + 2)
    e = int((x/9) + 2)
    f = int((x/6) + 2)
    for c in range(0,d):
            for b in range(0,e):
                for a in range(0,f):
                    nuggets = 6*a+9*b+20*c
                    if nuggets == x:
                        if x not in possible_list:
                            possible_list.append(x)
                        else: pass;
                    else: pass;

#print possible_list;
counter = 0;
for x in range(1,100):
    if x not in possible_list:
        largest.append(x)

#print largest;
print 'Largest number of McNuggets that cannot be bought in exact quantity:', max(largest);

#Problem 4!
#way easier when I went back and redid the others using variables to restrict and reduce
#the amount of time it would take the code to run (adding the variables d,e,f)
#Time: 20min
def McNuggets(packages):
    if 1 in packages:
        print "All packages work for:", packages[0], packages[1], packages[2], "!";
        #This is because you could always add a pack of 1 to get to the amount of nuggets you need
        #Also the function takes really long if you don't break at this point
        #It finds all the solutions and it takes forever to load like 10s +
        return 0
    possible_list=[]
    largest=[]
    for x in range(1,201):
        h = packages[0]
        i = packages[1]
        j = packages[2]
        d = int((x/h) + 2)
        e = int((x/i) + 2)
        f = int((x/j) + 2)
        for c in range(0,d):
                for b in range(0,e):
                    for a in range(0,f):
                        nuggets = j*a+i*b+h*c
                        if nuggets == x:
                            if x not in possible_list:
                                possible_list.append(x)
                            else: pass;
                        else: pass
    #print possible_list
    counter = 0
    for x in range(1,201):
        if x not in possible_list:
            largest.append(x)
    #print largest
    if largest == []:
        print "All numbers work for package sizes", packages[0], packages[1], packages[2], "!";
    else:
        print "Given package sizes",packages[0], packages[1], "and", packages[2], "the largest number of McNuggets that cannot be bought in exact quantity is:" , max(largest);

print "answers were restricted to a range of 1 to 200 inclusive"

McNuggets((20,6,9));
McNuggets((12,4,3));
McNuggets((20,25,12));
McNuggets((13, 57, 12));
McNuggets((4,6,10));
McNuggets((1,2,3));
McNuggets((1,5,10));
McNuggets((2,3,5));
McNuggets((2,2,2));
#endnote: is this the cleanest solution?: No
# is it the solution MIT wanted?: Definitely not
# is it really ugly?: Yep!
#but this was made by me. The only help I had was a bit of StackOverflow and whatever
#messed up logic I had in my head.
#I'll probably look back on this mess in a while and laugh
#hopefully at that point I'll be able to redo this in a cleaner solution

