#Problem Set 1
#Name: Anusika Nijher
#Collaborators: None

#Problem 1!
#Time 45min
from math import sqrt
from math import log
count = 1
n = 1
while count < 1000:
    n += 2
    for k in range(2, int(sqrt(n)+1)):
        if n%k == 0:
            break
    else:
            count += 1;
print  'the 1000th prime is', n, " " 
        
#Problem 2!
#Time 30min
def prime_it(n):
    ori_n = n;
    total = 0.0;
    for n in range(n,1,-1):
        for k in range(2, int(sqrt(n)+1)):
            if n%k == 0:
                break
        else:
                total += log(n);
                
    print 'the sum of the prime logs for', ori_n, 'is', total;            
    print 'the ratio is:',total/ori_n;
    print '';
  
prime_it(5);
prime_it(10);
prime_it(50);
prime_it(100);
prime_it(500);
prime_it(1000);
prime_it(5000);
prime_it(100000);
prime_it(1000000);
print 'wow the ratio approches 1!!!!'
