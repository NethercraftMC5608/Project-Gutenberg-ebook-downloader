import time
import os
import platform
import sys
import numbers
from random_word import RandomWords
import urllib.request
print (sys.argv)
ne = sys.argv
ne.remove(__file__)
r = RandomWords()
provideid = (','.join(ne))
print (provideid)
def has_numbers():
    
    return any(char.isdigit() for char in provideid)
number = 0
numberforcalc = 1
max = 66185
url = "https://www.gutenberg.org/ebooks/"
epub = ".epub.images"
list = []
print("Retrieving ebooks from www.gutenberg.org")
loop = True
if has_numbers() is True:
    print("downloading ID", provideid)
    numberforcalc = 1
    list.clear()
    number = provideid
    result = str(url) + str(number) + str(epub)
    list.append(result)
    loop = False

while loop is True:
   
    
    
    result = str(url) + str(number) + str(epub)
    list.append(result)
    number += 1
    numberforcalc +=1
    number
    
    if number == max:
        print("Retrieved", numberforcalc, "Books, out of the maximum of", max, "As of 31st August 2021")
        time.sleep(3)
        break
print("downloading", numberforcalc, "Books, out of the maximum of", max, "As of 31st August 2021")
time.sleep(1)
print("NOTE, these books are named randomly, just so it doesn't rewrite anything. They still provide title and description in epub reader.")
time.sleep(5)
print(platform.system(), "OS found, defaulting file path.")
filenum = 1
failed = 0
links = list
for link in links:
    link = link.strip()
    name = r.get_random_word()
    eys = str(name) + ".epub"
    filename = eys
    if not os.path.isfile(filename):
        print(filenum, "/", numberforcalc, "completed.", failed, "failed")
        print('Downloading: ' + filename)
        filenum += 1
        try:
            filename = os.path.join(filename)
            
            urllib.request.urlretrieve(link, filename)
        except Exception as inst:
            print(inst)
            print('  Encountered unknown error. Continuing')
            failed += 1
            filenum -= 1
print("Done Operation, Downloaded", filenum, "/", numberforcalc, "Last ID was", number)