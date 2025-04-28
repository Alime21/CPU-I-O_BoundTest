import requests

urlss = [
    "https://media.istockphoto.com/id/1325337801/tr/foto%C4%9Fraf/diver-swimming-in-underwater-cave-towards-the-light-at-oceans-surface.jpg?s=612x612&w=is&k=20&c=cJnRj8vGHNyGCPMwbhfB5eO01HeaQMw2NvqJOOeETIM=",
    "https://media.istockphoto.com/id/1301667498/tr/foto%C4%9Fraf/kambur-balina-e%C4%9Flenceli-berrak-mavi-okyanusta-y%C3%BCzme.jpg?s=612x612&w=is&k=20&c=MnvgQ9A-zfxStRW4Til4OMHlCAbN2iGmqmrhMygpJq4=",
    "https://media.istockphoto.com/id/521113609/tr/foto%C4%9Fraf/indonesian.jpg?s=612x612&w=is&k=20&c=jPStw4PCxYd23eVAT2l9yMwuOvdUgpf0Dzh23UMfScg=",
    "https://media.istockphoto.com/id/1166684037/tr/foto%C4%9Fraf/nehir-ve-denizin-su-dalgalar%C4%B1-y%C3%BCksek-gelgit-ve-d%C3%BC%C5%9F%C3%BCk-gelgit-s%C4%B1ras%C4%B1nda-birbiriyle-bulu%C5%9Fuyor.jpg?s=612x612&w=is&k=20&c=_Si0_9euf2OXLQTeDgS6GzF-tT9MD0jOeblpn8P-IEs="
]


for i, url in enumerate(urlss):

        response = requests.get(url)
        if response.status_code == 200:
            filename = f"image_{i}.jpg"
            with open("filename", "wb") as f:
                f.write(response.content)
                print("successfull download") 
        else:
            print(f"{filename} indirilemedi. Kod: {response.status_code}")
    
