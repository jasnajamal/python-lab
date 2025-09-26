names=["anu","meena","rani","anand"]
count=0
for i in range(len(names)):
    name=names[i]
    for j in range(len(name)):
        if name[j]=='a':
            count+=1
print("total no.of a:",count)
