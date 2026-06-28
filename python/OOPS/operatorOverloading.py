# operator overloading is changing the default behaviour of an operator
# similar to what we have already seen for methods/function overriding

# mathematical operation for vectors
class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def __add__(self,other):
        return Vector(self.x+other.x,self.y+other.y)
    
    def __sub__(self,other):
        return Vector(self.x-other.x,self.y-other.y)
    
    def __mul__(self,other):
        return Vector(self.x*other.x,self.y*other.y)
    
    def __eq__(self,other):
        return self.x==other.x and self.y==other.y
    
    def __repr__(self):
        return f"Vector({self.x},{self.y})"

# creating vector objects 
v1=Vector(3,4)
v2=Vector(5,6)

print(v1+v2)
print(v1-v2)
print(v1*v2)
print(v1==v2)

# same can be done for complex numbers method overloading 

class ComplexNumber:
    
    def __init__(self,real,img):
        self.real=real
        self.img=img
        
    def __sum__(self,other):
        return ComplexNumber(self.real+other.real,self.img+other.img)
    
    def __sub__(self,other):
        return ComplexNumber(self.real-other.real,self.img-other.img)

    def __mul__(self,other):
        return ComplexNumber(self.real*other.real-self.img*other.img,self.real*other.img+self.img*other.real)

    def __eq__(self,other):
        return self.real==other.real and self.img==other.img

    def __repr__(self):
        return f"ComplexNumber({self.real},{self.img})"