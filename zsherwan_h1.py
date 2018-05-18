#!/usr/bin/python3.5
# Author - Zanyar Sherwani
import math

def prime_factors(n):
    primes = []
    occurences= 0
    primeNum = n
    # add all 2's to the list of primes
    while n%2==0:
        n = n/2
        primes.append(2)
    
    tmpN = n
    # appends n if it is equal to 3, 5, or 7
    if n < 9 and n > 1:
        primes.append(n)
        return primes
    
    # i obviously must start from 3 since at this point n%2 != 0
    # i is checked for less than (n^1/2) + 1, because any factor 
    # greater than that in magnitude has been discovered 
    # example: sqrt(27) + 1 = 6, althought 9 is a factor and > 6 it 
    # has already been discovered because 3 < 6 and 3 * 9 = 27
    # i is incremented by 2 because tmpN will never be even
    for i in range(3, int(math.sqrt(n))+1, 2):
        # while tmpN (or n) is divisible by  i, check for prime factors
        # of i 
        while tmpN%i == 0:
            primeNum = getPrime(i)
            # checks for occurences of the prime Factor by taking the
            # log base primeNum of tmpN: primeNum^occurences = tmpN
            occurences = log(primeNum, tmpN, tmpN/i)
            # updates the list of primes to be returned
            primes = addPrimes(primes, occurences, primeNum)
            primeNum = tmpN/i
            tmpN=tmpN/i
            
        if i == int(math.sqrt(n)) and primeNum != 1:
            primes.append(primeNum)
  
    return primes

# just a function to update the list
def addPrimes(lst, n, num):
    for i in range(0, n, 1):
        lst.append(num)
    return lst 

# returns the log base n
def log(base, n, quotient):
    tmp = 1
    i = 0
    while tmp < n:
        tmp = tmp*base*quotient
        if tmp <= n:
            i = i+1
    return i

# returns the prime factors of n
def getPrime(n):
    for i in range(3, int(math.sqrt(n))+1, 2):
        if n%i == 0:
            return getPrime(n/i)
        elif i == int(math.sqrt(n)):
            return n

    return int(n)


def coprime(a, b):
    aFactors = []
    bFactors = []
    # gets all factors of a and b
    aFactors = getFactors(a)
    bFactors = getFactors(b)
    for i in range(0, len(aFactors), 1):
        for j in range(0, len(bFactors), 1):
            if aFactors[i] == bFactors[j]:
                return False

    return True

# returns all factors of a number n, except one
def getFactors(n):
    factors = []
    for i in range (2, int(math.sqrt(n))+1, 1):
        if n%i == 0:
            factors.append(i)
            factors.append(n/i)

    return factors


def max_new(xs, olds):
    if len(xs) == 0:
        return None
    # initializes maxNum to the first element
    maxNum = xs[0]

    for i in range(1, len(xs), 1):
        if xs[i] > maxNum:
            # checks if the element is contained in olds
            dup = checkDuplicate(xs[i], olds)
            if dup == False:
                maxNum = xs[i]
    # let's do one final check!            
    dup = checkDuplicate(maxNum, olds)
    if dup == False:
        return maxNum
 
# iterates thru a list lst, and returns true if it contains
# the element n
def checkDuplicate(n, lst):
    for i in range(0, len(lst), 1):
        if n == lst[i]:
            return True

    return False

def powerset(xs):
    # initializes the power set to 2^n
    pwrSet = [[] for i in range (twoexponential(len(xs)))]
    newSet =[]
    # ctr will be used to index the pwrSet list
    ctr = len(xs)+1
    # k represents the number of elements in a subset 
    k = 2
    z = 0
    # cdr represent the index of the very next index an element
    # should be inserted
    cdr = 1
    # initializes the power set with all subsets of one element
    # and the null set 
    for i in range (1, len(xs)+1, 1):
        pwrSet[i].append(xs[i-1])
        
    # increments i to 2^n + -n + -1, because there are n+1 elements
    # in the pwrSet list 
    for i in range(0, twoexponential(len(xs))-len(xs)-1, 1):
        pwrSet[ctr].append(xs[z])
        newSet = populate(pwrSet, xs, k, cdr)
        cdr = cdr+1
        for y in range(0, len(newSet), 1):
            pwrSet[ctr].append(newSet[y])
        if pwrSet[ctr][len(pwrSet[ctr])-1] == xs[len(xs)-1] and pwrSet[ctr][0] != xs[0]:
            z= 0
            k = k+1
            cdr= z+1
        elif pwrSet[ctr][len(pwrSet[ctr])-1] == xs[len(xs)-1] and z < len(xs)-1:
            z = z+1
            cdr = z+1  
        ctr = ctr +1
        
    return pwrSet    

# populates a new list called newSet
# k is the number of elements to populate
# for example when k is two, the list will
# contain list of 2 element subsets
def populate(pwr, xs, k, cdr):
    newSet =[]
    
    for i in range(1,k,1):
        if cdr < len(xs):
            newSet.append(xs[cdr])
        cdr = cdr+1
    return newSet

# returns 2^n
def twoexponential(n):
    product = 1
    for i in range (0,n, 1):
        product = 2*product
    return product


# self explanatory
def zip_with(f, xs, ys):
    length = 0
    newList = []
    # checks for python's version of nullity 
    if xs == None or ys == None:
        return []
    # uses the length of the shortest list
    if len(xs) > len(ys):
        length = len(ys)
    else:
        length=len(xs)

    for i in range (0,length, 1):
        newList.append(f(xs[i], ys[i]))
    return newList

# self explanatory
def pass_fail(f, xs):
    passLst= []
    failLst =[]
    for i in range(0,len(xs), 1):
        if f(xs[i]) == True:
            passLst.append(xs[i])
        else:
            failLst.append(xs[i])
    return (passLst, failLst)


def trib(n):
    # initializes the tribonacci list with 1, 1, 1
    tribList =[1, 1, 1]

    # appends and element which is the sum of it's 3 
    # 3 predecessors
    for i in range(3, n+3,1):
        tribList.append(tribList[i-3] + tribList[i-2] + tribList[i-1])
    return tribList[n]

# o(n^3) !!!
def matrix_product(xss, yss):
    lengthOfY = 0
    ans = 0
    # checks to see of number of columns
    # in xss == number of rows in yss
    if len(xss[0]) != len(yss):
        return None
    
    # will hold the matrix product   
    product = []
    # holds the rows of the new matrix
    row = []
    # outer loop, loops for the number of rows in xss
    # since new matrix will have rows equal to number of
    # rows in xss
    for k in range(0, len(xss), 1):
        # new matrix will have columns == to columns of yss
        for j in range(len(yss[0])):
            # must multiply everything in the same row of xss
            # with everything in the same column of yss
            for i in range(len(xss[0])):
                   ans = ans + xss[k][i]*yss[i][j]
            row.append(ans)           
            ans=0            
        product.append(row)
        row = []
    return product


