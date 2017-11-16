# Problem Set 4
# Name: Anusika Nijher
# Collaborators: None


#Problem 1
#Time 20 min

def nestEggFixed(salary, save, growthRate, years):
    savingsRecord=[];
    same = (salary * save * 0.01)
    growthRate = (growthRate * 0.01 + 1)
    for y in range(years):
        if(y == 0):
            savingsRecord.append(same)
        else:
            total = savingsRecord[y-1] * growthRate + same
            savingsRecord.append(total)
    return savingsRecord

#Problem 2
#Time 15min

def nestEggVariable(salary, save, growthRates):
    savingsRecord=[]
    same = (salary * save * 0.01)
    for x in range(len(growthRates)):
        growthRate = (growthRates[x] * 0.01 + 1)
        if(x == 0):
            savingsRecord.append(same)
        else:
            total = savingsRecord[x-1] * growthRate + same
            savingsRecord.append(total)
    return savingsRecord


#Problem 3
#Time: 5 min

def postRetirement(savings, growthRates, expenses):
    savingsRecord = []
    for x in range(len(growthRates)):
        growthRate = (growthRates[x] * 0.01 + 1)
        if ( x == 0):
            savingsRecord.append(savings * growthRate - expenses)
        else:
            total = savingsRecord[x-1] * growthRate - expenses
            savingsRecord.append(total)
    return savingsRecord

#Problem 4
#Time 20min

def findMaxExpenses(salary, save, preRetireGrowthRates, postRetireGrowthRates, epsilon):
    moneySave = nestEggVariable(salary,save,preRetireGrowthRates)
    print "you have saved", moneySave[-1], "before Retirement"
    high = moneySave[-1]
    remaining = 2 * epsilon
    low = 0
    mid = (high + low)/2
           
    while(abs(remaining) > epsilon):
        remaining = (postRetirement(moneySave[-1], postRetireGrowthRates, mid)[-1])
        print "guessing:" ,mid, "result:", remaining
        
        if (remaining > 0.0):
            low = mid
        else:
            high = mid
            
        mid = (high + low)/2
    print "you should spend", mid

findMaxExpenses(10000,10,[3,4,5,0,3],[10,5,0,5,1],0.01)
