answer = []
# line = "abAAAcAAAcd"
with open("3.txt") as file:
    for line in file:
        for i,char in enumerate(line[3:len(line)-3]):
            if char.islower():
                if (line[i+3-3].isupper() and line[i+3-2].isupper() and 
                    line[i+3-1].isupper() and line[i+3+1].isupper() and
                    line[i+3+2].isupper() and line[i+3+3].isupper() and
                    (i==0 or line[i+3-4].islower()) and 
                    (i==len(line)-3-4 or line[i+3+4].islower())):
                    answer.append(char)
        

print(answer)