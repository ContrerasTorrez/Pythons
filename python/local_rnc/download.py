import requests
from clint.textui import progress
def download(url):
    try:
        r = requests.get(url, stream=True)
        with open("content/RNC.zip", "wb") as mizip:
            total_length = int(r.headers.get('content-length'))
            for ch in progress.bar(r.iter_content(chunk_size = 25200), expected_size=(total_length/1024) + 1):
                if ch:
                    mizip.write(ch)        
    except Exception as err:
        print("im sorry , your download not completed . ERROR : ")
