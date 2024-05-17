import pickle

with open('banner.p', 'rb') as f:

    banner = pickle.load(f) # deserialize using load()
    print(banner)

print(type(banner))

for row in banner:
    result = ""
    for pair in row:
        result += pair[0]*pair[1]
    print(result)