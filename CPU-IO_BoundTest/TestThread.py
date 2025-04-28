import threading
import time

# these functions are running on the same thread 
# one by one because because they're all running on the same thread
# concurrently , multitasking

def listen_music(first, last):
    time.sleep(1)
    print(f"ı am listening {first} {last}")

def surfing_internet():
    time.sleep(4)
    print("looking instagram")

def talking():
    time.sleep(20)
    print("talking with my roomate")

"""listen_music()
surfing_internet()
talking()"""
"""chore1 = threading.Thread(target=listen_music ,args=("adele", "waterunderthebridge") )
chore1.start()
chore2 = threading.Thread(target=surfing_internet)
chore2.start()
chore3 = threading.Thread(target=talking)
chore3.start()

print("before join")
chore1.join()  #thread'in bitmesini bekler .join() kullanmazsan diğer thread tamamlanmadan çalışmaya devam eder
chore2.join()
chore3.join()
print("after join")"""
# more efficent version: for loop
tasks = [
    (listen_music, ("adele", "waterunderthebridge")),
    (surfing_internet, ()),
    (talking, ())
]
threads = []
# one thread for each task
for function, args in tasks:
    thread = threading.Thread(target= function, args=args)
    thread.start()
    threads.append(thread)
# wait for finish to whole threads
for thread in threads:
    thread.join()    
      


