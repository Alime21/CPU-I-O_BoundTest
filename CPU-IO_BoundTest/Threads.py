import threading
import requests
import time


all_urls = [
    "https://media.istockphoto.com/id/1325337801/tr/foto%C4%9Fraf/diver-swimming-in-underwater-cave-towards-the-light-at-oceans-surface.jpg?s=612x612&w=is&k=20&c=cJnRj8vGHNyGCPMwbhfB5eO01HeaQMw2NvqJOOeETIM=",
    "https://media.istockphoto.com/id/1301667498/tr/foto%C4%9Fraf/kambur-balina-e%C4%9Flenceli-berrak-mavi-okyanusta-y%C3%BCzme.jpg?s=612x612&w=is&k=20&c=MnvgQ9A-zfxStRW4Til4OMHlCAbN2iGmqmrhMygpJq4=",
    "https://media.istockphoto.com/id/521113609/tr/foto%C4%9Fraf/indonesian.jpg?s=612x612&w=is&k=20&c=jPStw4PCxYd23eVAT2l9yMwuOvdUgpf0Dzh23UMfScg="
    
]

# download img function
def download_img(url):
    response = requests.get(url)
    filename = f"image_{url}.jpg"
    if response.status_code == 200:
            with open("filename", "wb") as f:
                f.write(response.content)
                print("successfull download") 
    else:
        print(f"{filename} unsuccessfull. Code: {response.status_code}")

if __name__ == "__main__":

    ## time check start
    start_time = time.time()

    threads = []
    # start thread for each url
    for url in all_urls:
        thread = threading.Thread(target=download_img, args=(url, ))    # target=fonksiyonumuz args=fonksiyonun parametresi
        thread.start()
        threads.append(thread)
    # wait for all threads
    for thread in threads:
        thread.join()

    ## time check end
    end_time = time.time()
    print(f"Threading TOTAL TİME: {end_time - start_time:2f} seconds")

