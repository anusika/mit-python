import time
start_time = time.time()
name = raw_input('What is your name?: ')
end_time = time.time()
total_time = end_time - start_time
print 'It took %0.2f to enter your name' % total_time
