from collections import Counter

data = ""
with open('2.txt', 'r') as file:
    data = file.read().rstrip()

counter = Counter(data)

print(counter)