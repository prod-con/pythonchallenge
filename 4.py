import requests

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
index = "63579"
r = requests.get(url+index)
print(r.text)
print(int(''.join(filter(str.isdigit, r.text))))
print(url + str(''.join(filter(str.isdigit, r.text))))

for i in range(400):
    r = requests.get(url+index)
    index = str(''.join(filter(str.isdigit, r.text)))
    print(i, index)

#print(index)