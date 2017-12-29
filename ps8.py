# 6.00 Problem Set 8
#
# Intelligent Course Advisor
#
# Name: Anusika Nijher
# Collaborators: None


import time
import string

SUBJECT_FILENAME = "subjects.txt"
VALUE, WORK = 0, 1

# Problem 1: Building A Subject Dictionary
# Time: 15min
dec = {}
def loadSubjects(filename):
    inputFile = open(filename)
 
    for line in inputFile:
        line = line.strip()
        parts = line.split(',')
        dec[parts[0]]=(int(parts[-2]),int(parts[-1]))
    return dec

loadSubjects(SUBJECT_FILENAME)

def printSubjects(subjects):
    totalVal, totalWork = 0,0
    if len(subjects) == 0:
        return 'Empty SubjectList'
    res = 'Course\tValue\tWork\n======\t====\t=====\n'
    subNames = subjects.keys()
    subNames.sort()
    for s in subNames:
        val = subjects[s][VALUE]
        work = subjects[s][WORK]
        res = res + s + '\t' + str(val) + '\t' + str(work) + '\n'
        totalVal += val
        totalWork += work
    res = res + '\nTotal Value:\t' + str(totalVal) +'\n'
    res = res + 'Total Work:\t' + str(totalWork) + '\n'
    print res

def cmpValue(subInfo1, subInfo2):
    """
    Returns True if value in (value, work) tuple subInfo1 is GREATER than
    value in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    return  val1 > val2

def cmpWork(subInfo1, subInfo2):
    """
    Returns True if work in (value, work) tuple subInfo1 is LESS than than work
    in (value, work) tuple in subInfo2
    """
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    return  work1 < work2

def cmpRatio(subInfo1, subInfo2):
    """
    Returns True if value/work in (value, work) tuple subInfo1 is 
    GREATER than value/work in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    return float(val1) / work1 > float(val2) / work2

# Problem 2: Subject Selection By Greedy Optimization
# Time: 3 hours
def greedyAdvisor(subjects, maxWork, comparator):
    recc = {}
    class_list = subjects.keys()
    while len(class_list) > 0 and maxWork > 0:
        best_class = class_list[0]
        best_result = subjects[best_class]
        for subject in class_list:
            if comparator(subjects[subject], best_result):
                best_result = subjects[subject]
                best_class = subject
        class_list.remove(best_class)
        if maxWork - best_result[WORK] > -1:
            recc[best_class] = best_result             
            maxWork = maxWork - best_result[WORK]
    printSubjects(recc)
    return recc

def bruteForceAdvisor(subjects, maxWork):
    nameList = subjects.keys()
    tupleList = subjects.values()
    bestSubset, bestSubsetValue = \
            bruteForceAdvisorHelper(tupleList, maxWork, 0, None, None, [], 0, 0)
    outputSubjects = {}
    for i in bestSubset:
        outputSubjects[nameList[i]] = tupleList[i]
    return outputSubjects

def bruteForceAdvisorHelper(subjects, maxWork, i, bestSubset, bestSubsetValue,
                            subset, subsetValue, subsetWork):
    # Hit the end of the list.
    if i >= len(subjects):
        if bestSubset == None or subsetValue > bestSubsetValue:
            # Found a new best.
            return subset[:], subsetValue
        else:
            # Keep the current best.
            return bestSubset, bestSubsetValue
    else:
        s = subjects[i]
        # Try including subjects[i] in the current working subset.
        if subsetWork + s[WORK] <= maxWork:
            subset.append(i)
            bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects,
                    maxWork, i+1, bestSubset, bestSubsetValue, subset,
                    subsetValue + s[VALUE], subsetWork + s[WORK])
            subset.pop()
        bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects,
                maxWork, i+1, bestSubset, bestSubsetValue, subset,
                subsetValue, subsetWork)
        return bestSubset, bestSubsetValue

# Problem 3: Subject Selection By Brute Force
# Time: 15min
def bruteForceTime():
    total_times = {}
    for times in range(1,10):
        start_time = time.time()
        bruteForceAdvisor(dec,times)
        end_time = time.time()
        total_times[times] = round(end_time - start_time, 3)
    print("maxWork\tTime")
    for times in total_times:
        print("{}\t{}".format(times,total_times[times]))

# Problem 4: Subject Selection By Dynamic Programming
# Time: 4 hours

def dpAdvisor(subjects, maxWork):
    m = {}
    recc = {}
    class_list = list(subjects.keys())
    values =[elem[0] for elem in subjects.values()]
    works =[elem[1] for elem in subjects.values()]
    value, recc_list= dpAdvisorHelper(works, values, len(values)-1, maxWork, m)
    for classes in recc_list:
        recc[class_list[classes]] = (values[classes], works[classes])
    return recc
        

def dpAdvisorHelper (w, v, i, aW, m):
    try:
        return m[(i,aW)]
    except KeyError:
        if i == 0:
            if w[i] < aW:
                m[(i,aW)] = v[i], [i]
                return v[i],[i]
            else:
                m[(i,aW)] = 0, []
                return 0,[]
    without_i, without_list = dpAdvisorHelper(w,v,i-1,aW,m)
    if w[i] > aW:
        m[(i,aW)] = without_i, without_list
        return without_i, without_list
    else:
        with_i, with_list = dpAdvisorHelper(w, v, i-1, aW - w[i], m)
        with_i += v[i]
    if with_i > without_i:
        i_value = with_i
        without_list = [i] + with_list
    else:
        i_value = without_i
    m[(i,aW)] = i_value, without_list
    return i_value, without_list
    
# Problem 5: Performance Comparison
# Time: 10 min
def dpTime():
    total_times = {}
    for times in range(1,10):
        start_time = time.time()
        dpAdvisor(dec,times)
        end_time = time.time()
        total_times[times] = round(end_time - start_time, 3)
    print("maxWork\tTime")
    for times in total_times:
        print("{}\t{}".format(times,total_times[times]))

dpTime()
