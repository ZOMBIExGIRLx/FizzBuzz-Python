def fizzBuzz():
    
    num = input("Enter a number greater than zero: ")
    num = int(num)
    
    if (num > 0):
        if (num % 3 == 0) and (num % 5 == 0):
            return (f"{num} - FizzBuzz!!")
        elif (num % 3 == 0):
            return (f"{num} - Fizz!!")
        elif (num % 5 == 0):
            return (f"{num} - Buzz!!")
        else:
            return (num)
    else:
        return ("You must enter a number greater than zero!")