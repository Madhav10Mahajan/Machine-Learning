# custom exception raise and throw

class Error(Exception):
    pass

class dobException(Error):
    pass 

year=int(input('enter your dob'))
age=2026-year

try:
   if age<=30 and age>=20:
    print('the age is valid so you can apply for the exam')
   else:
    raise dobException
except dobException:
    print('Sorry your age should be greater than equal to 20 and less than equal to 30')