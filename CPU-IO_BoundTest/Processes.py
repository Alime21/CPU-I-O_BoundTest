from multiprocessing import Process, Queue
import requests
import time
import hashlib


all_urls = [
    "https://media.istockphoto.com/id/1325337801/tr/foto%C4%9Fraf/diver-swimming-in-underwater-cave-towards-the-light-at-oceans-surface.jpg?s=612x612&w=is&k=20&c=cJnRj8vGHNyGCPMwbhfB5eO01HeaQMw2NvqJOOeETIM=",
    "https://media.istockphoto.com/id/1301667498/tr/foto%C4%9Fraf/kambur-balina-e%C4%9Flenceli-berrak-mavi-okyanusta-y%C3%BCzme.jpg?s=612x612&w=is&k=20&c=MnvgQ9A-zfxStRW4Til4OMHlCAbN2iGmqmrhMygpJq4=",
    "https://media.istockphoto.com/id/521113609/tr/foto%C4%9Fraf/indonesian.jpg?s=612x612&w=is&k=20&c=jPStw4PCxYd23eVAT2l9yMwuOvdUgpf0Dzh23UMfScg="
    
]

# download img function
def download_img(url):
    response = requests.get(url)
    # hash the url for secure file name
    hashed = hashlib.md5(url.encode()).hexdigest()
    filename = f"image_{hashed}.jpg"
    if response.status_code == 200:
            with open(filename, "wb") as f:
                f.write(response.content)
                print("successfull download") 
    else:
        print(f"{filename} unsuccessfull. Code: {response.status_code}")

if __name__ == "__main__":
    
    start_time = time.time()

    processes = []
    for url in all_urls:
        p = Process(target=download_img, args=(url,))
        p.start()
        processes.append(p)
    
    for p in processes:
        p.join()


    ## time check end
    end_time = time.time()
    print(f"Multiprocessing TOTAL TİME: {end_time - start_time:2f} seconds")
  