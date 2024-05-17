import os.path
import zipfile
archive = zipfile.ZipFile(r'channel.zip', 'r')
filename = "90052.txt"
comments = []
while os.path.exists("channel/"+filename):
    with open("channel/"+filename) as file:
        data = file.read().rstrip()
        comments.append(archive.getinfo(filename).comment.decode("utf-8"))
        index = str(''.join(filter(str.isdigit, data)))
        print(index)
    filename = index+".txt"

print("".join(comments))