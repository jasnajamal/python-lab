 text="this is a simple line this is a text"
words=text.split()
counts={}
for i in words:
    counts[i]=counts.get(i,0)+1
print(counts)
