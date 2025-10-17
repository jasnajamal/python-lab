def reverse(num):
    rev_num = 0
    while num > 0:
        rev_num = rev_num * 10 + num % 10
        num = num // 10
    return rev_num
def main():
    while True:
        num = input("Enter a number with at least 4 digits: ")
        if num.isdigit() and len(num) >= 4:
            number = int(num)
            break
        else:
            print("invalid input")
    rev_num = reverse(number)
    print(f"Original number: {number}")
    print(f"Reversed number: {rev_num}")
main()





