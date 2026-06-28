# exception handling in python similar to other languages cpp,js
# allows us to handle errors gracefully without breaking the code/stopping the main execution 
# try catch finally block 

# exceptions are events that disrupt the normal flow of the code
# division by zero
# file not found
# value error - invalid value
# type error

# a=b, b is not defined NameError

try:
    a=b
except NameError as error:
    print(error)

# result=1/0 zeroDivisionError

try:
    result=1/0
except ZeroDivisionError as error:
    print(error)

try:
    result=1/0
    a=b
except ZeroDivisionError as er:
    print(er)
    print('pls enter denominator greater than zero')
except Exception as er1:
    print(er1)
    print('the variable is not defined')

try:
    num=int(input('enter your number'))
    result=10/num
except ValueError:
    print('the number is invalid')
except ZeroDivisionError:
    print('the denominator cant be 0')
except Exception as error:
    print(error)

# try, except and else block

try:
    num=int(input('enter your number'))
    result=10/num
except ValueError:
    print('the number is invalid')
except ZeroDivisionError:
    print('the denominator cant be 0')
else:
    print('the result is: ',result) # this line gets executed only if no error is caught
    
# if it goes in the try block and is sucessfully then the else block gets executed

# try,except, else and finally block
try:
    num=int(input('enter your number'))
    result=10/num
except ValueError:
    print('the number is invalid')
except ZeroDivisionError:
    print('the denominator cant be 0')
else:
    print('the result is: ',result)
finally:
    print('execution is complete, this gets executed irrespective of error is caught or not') # gets executed everytime

# else gets executed only if its successfully executed
# finally gets executed everytime irrespective of error or not

# file and exception handling
try:
    file=open('example1','r')
    content=file.read()
    print(content)
    a=b
except FileNotFoundError:
    print('the file is not found')
except Exception as e:
    print('Error:', e)
finally:
    if 'file' in locals() and not file.closed: # checking if the file is defined in the local scope or not
       file.close() # closing the file in finally block to ensure that the file is closed irrespective of error or not
    print('file is closed')