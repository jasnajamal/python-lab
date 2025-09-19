list=(input("enter the integer values for first list:"))
list1=[]
for x in list.split():
    list1.append(int(x))
lst=(input("enter the integer values for first list:"))
list2=[]
for x in lst.split():
    list2.append(int(x))
if len(list1)==len(list2):
    print("list are same")
else:
    print("list are nit same")
if sum(list1)==sum(list2):
    print("sum of list is same")
else:
    print("sum of list is not same")
for i in list1:
    if i in list2:
        print("common value fount:",i)
        break;
else:
    print("no common value fount")

