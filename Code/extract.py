import urllib.request       # to access the link
import re       # regular expression support

# open source file
with open("raw.txt", 'r') as file:
    data = file.read()

lst = []

for i in data.split('href="'):
    lst.append(i.split('"')[0])

lst.pop(0)

def create_d(j): 
    fp = urllib.request.urlopen(j)
    mybytes = fp.read()

    mystr = mybytes.decode("utf8")
    fp.close()


    val = re.findall(r"<p>.*?</p>", mystr)

    key = re.findall(r'<div class="font-bold uppercase text-sm text-gray-800 woocommerce-product-attributes-item__label">.*?</div>', mystr)

    pure_keys=[]
    pure_val=[]

    for i in key:
        if i[i.find(">")+1:i[1:].find("<")+1] == "Details":
            continue
        else:
            pure_keys.append(i[i.find(">")+1:i[1:].find("<")+1])

    for j in val:
        pure_val.append(j[j.find(">")+1:j[1:].find("<")+1])


    d = {}

    for i in range(len(pure_keys)):
        if i<len(pure_val):
            d[pure_keys[i]] = pure_val[i] 

    return d

# a list of dictionaries with all info
TO_BE_SAVED_LIST = []
for link in lst:
    TO_BE_SAVED_LIST.append({link: create_d(link)})

import pickle
with open("saved.bin", "wb")as file:
    pickle.dump(TO_BE_SAVED_LIST, file)