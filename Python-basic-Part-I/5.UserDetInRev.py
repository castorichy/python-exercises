def myReverse(string) -> int:
    rev = ""
    i = 1
    for n in string:
        rev = n + rev
        if i < len(string):
            rev = " " + rev
        i += 1
    return rev

fname = input("First name: ")
lname = input("Last name: ")

print(myReverse(fname))
print(myReverse(lname))
