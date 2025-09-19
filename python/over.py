                                                                                                                                                                            nums=input("enter inegers seperate by space:")
display=nums.split()
for i in range(len(display)):
    if int(display[i])>100:
        display[i]="over"
print(display)
      
