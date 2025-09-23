str="box"
if len(str)<=1:
    result=str
else:
    result=str[-1]+str[1:-1]+str[0]
print(result)
