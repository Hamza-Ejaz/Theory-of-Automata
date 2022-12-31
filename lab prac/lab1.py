import re

#Muhammad Basit Mukhtar - B19102071
matcher = input("Enter any expression for check: ")
lst = [0,0,0,0,0,0]
re1 = re.match(r"\b1*01*01*\b",matcher)
re2 = re.match(r"^0*(1[0]*1[0]*)*$",matcher)
re3 = re.match(r"\b([1]*0[1]*0[1]*)|([0]*1[0]*1[0]*1[0]*)\b",matcher)
re4 = re.match(r"(0*(10*10*)*)|(1*(01*01*)*(01*))",matcher)
re5 = re.match(r"^1*01*0(1+0)$",matcher)
re6 = re.match(r"^[1]*|[1]*0[1]*|[1]*0[1]*0[1]*$",matcher)
#re6 = re.match(r"^([1]*)|([1]*0[1]*)|([1]*0[1]*0[1]*)$",matcher)

if re1:
    lst[0] = 1
if re2:
    lst[1] = 1
if re3:
    lst[2] = 1
if re4:
    lst[3] = 1
if re5:
    lst[4] = 1
if re6:
    lst[5] = 1

for ind,i in enumerate(lst):
    if i == 1:
        print(f"Matched with RE{ind+1}")