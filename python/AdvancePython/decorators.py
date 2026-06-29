## function copy 
## closures 
## decorators

def welcome():
    return "welcome to advanced python course"

welcome()

wel=welcome # we can treat functions as variable and so assign to a different variable
print(wel())

# closures same as in js function + lexical scope
# the inner function first looks for the varibale inside it, if not found there then it looks for the variable outside its scope 
# this is called chain of scope, it keeps on looking in its lexical parent 
z='mahajan'
def outerfunction():
    msg='welcome'
    print(z)
    def innerfunction():
        print('welcome to the advance python course', msg,y,z)
    
    y='madhav'
    return innerfunction

x=outerfunction()
x()

# decorators

def main(func):
    
    def innerfunction():
        print('inside the inner function')
        func()
        print('leaving the inner function')
    
    innerfunction()
    

def hello():
    print('hello world')
    
main(hello)

# now can we get the same output as above without calling the main function
@main # we arent modifying the code of the main function just adding the function which needs to be passed inside the main function
def hello():
    print('hello world')