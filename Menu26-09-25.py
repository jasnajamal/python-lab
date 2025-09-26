while True:
    print("\nMenu:")
    print("1.word occurrence count:")
    print("2.character frequency count:")
    print("3.display factor of a number:")
    print("4.Exit:")
    choice=input("input your choice(1-4):")
    if choice=='1':
        text=input("enter text:")
        words=text.split()
        freq={}
        for word in words:
            word=word.lower()
            if word in freq:
                freq[word]+=1
            else:
                freq[word]=1
        print("character frequency:")
        for word,count in freq.items():
            print(f"{word}:{count}")
    elif choice=='2':
        text=input("enter text:")
        freq={}
        for char in text:
            if char.isalnum():
                char=char.lower()
                if char in freq:
                    freq[char]+=1
                else:
                    freq[char]=1
        print("character frequency:")
        for char,count in freq.items():
            print(f"{char}:{count}")
    elif choice=='3':
        num_str=input("enter a number:")
        if num_str.isdigit():
            num=int(num_str)
            factors=[]
            for i in range(1,num+1):
                if num%i==0:
                    factors.append(i)
            print(f"factors of {num}:{factors}")
        else:
            print("please enter a valid integer")
    elif choice=='4':
        print("exiting the progrm")
        break
    else:
        print("invalid choice please select from(1-4)")


        
    
