# arithmetic operators
number=int(input(" input the first number:"))
number2=int(input(" input the second number:"))
print(number+number2)
print(number-number2)
print(number*number2)
print(number/number2)
print(number%number2)
# comparison operator
number3=int(input("Enter First number :"))
number4=int(input("Enter Second number :"))
print(f"{number3} is equal to {number4} : {number3 == number4}")
print(f"{number3} is not equal to {number4} : {number3 != number4}")
print(f"{number3} is greater than {number4}  {number3 > number4}")
print(f"{number3} is less than  {number4}  {number3 < number4}")
print(f"{number3} is less than or equals to  {number4}  {number3 <= number4}")
# logical operator
number5=int(input("Bonyeza Nambari :"))
number6=int(input("Bonyeza ya pili :"))
print(f"{number5} and {number6} both are true : {number5==number6 and number5>number6}")
print(f"{number5} and {number6} one is true: {number5==number5 or number5>number6}")

