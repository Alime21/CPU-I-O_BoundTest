import threading
import time 

def is_prime(n):
    if n <= 1 :
        return False
    for i in range(2,int(n**0.5)+1):
        if (n % i == 0):
            return False
    return True
def primes_in_range(start, end, result):
    primes_in_eachtuple = []         # append primes to each tuple in ranges
    for num in range(start,end):     # each tuple r[0] is start; r[1] is end
        if is_prime(num):
            primes_in_eachtuple.append(num)  # append: add a single element
    result.extend(primes_in_eachtuple)      # extends: add multiple elements(another list) to a list      
def thread_prime():
    threads = []
    result = []
    ranges = [(1,1000000), (1000000,2000000), (2000000,3000000), (3000000,4000000), (4000000,5000000)]
    
    start_time = time.time()   #time check start
    # start thread for each ranges
    for r in ranges:
        thread = threading.Thread(target=primes_in_range, args=(r[0], r[1],result))
        thread.start()
        threads.append(thread)
    # wait for all threads
    for thread in threads:
        thread.join()    
    end_time = time.time()    
    print(f"primes numbers found with threading: {len(result)} numbers")
    print(f"Threading TOTAL TİME : {end_time - start_time} seconds")
if __name__ == "__main__":    
    thread_prime()    