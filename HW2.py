# program to reverse a given number
number=int(input("Enter the Number:"))
reverse=0
while number>0:
    reminder=number%10
    reverse=(reverse*10)+reminder
    number=number//10
print("reverse number is:",reverse)
