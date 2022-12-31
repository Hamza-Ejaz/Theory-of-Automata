# enter regex for mobile number
# enter regex for email address
# .edu .com .org .net

import re

inp = input("Enter: ")
r = re.match('^([+]923)[0-9]{9}$',inp)
r1=re.match(r"([a-zA-Z0-9]+[.-_])*[A-Za-z0-9]+@[a-zA-Z0-9-]+(\.[com|edu|net|org])+",inp)
if r1:
     print("Valid Email!")
elif r:
    print("Valid Phone Number")
else:
    print("not valid")