import time
import os
import platform
from random_word import RandomWords
import urllib.request

r = RandomWords()
number = 1
max = 66186
url = "https://www.gutenberg.org/ebooks/"
epub = ".epub.images"
list = []
print("Retrieving ebooks from www.gutenberg.org")
while True:
    result = str(url) + str(number) + str(epub)
    number += 1
    
    list.append(result)
    if number == max:
        print("Retrieved", number, "Books, out of the maximum of", max, "As of 31st August 2021")
        time.sleep(3)
        break
OSPICK = 0
print("downloading", number, "Books, out of the maximum of", max, "As of 31st August 2021")
time.sleep(1)
print("NOTE, these books are named randomly, just so it doesn't rewrite anything. They still provide title and description in epub reader.")
time.sleep(5)
print(platform.system(), "OS found, defaulting file path.")
platform = platform.system()

if platform is "Windows":
    OSPICK = "C:\\ebooks"
if platform is "Darwin":
    OSPICK = "~/ebooks"
if platform is "Linux":
    OSPICK = "~/ebooks"
dir = OSPICK
filenum = 1
failed = 0
if not os.path.exists(OSPICK):
    os.makedirs(OSPICK)
links = list
for link in links:
    link = link.strip()
    name = r.get_random_word()
    eys = str(name) + ".epub"
    filename = os.path.join(str(dir), eys)

    if not os.path.isfile(filename):
        print(filenum, "/", number, "completed.", failed, "failed")
        print('Downloading: ' + filename)
        filenum += 1
        try:
            filename = os.path.join('/home/demo/Downloads', name)
            
            urllib.request.urlretrieve(link, filename)
        except Exception as inst:
            print(inst)
            print('  Encountered unknown error. Continuing')
            failed += 1
            filenum -= 1