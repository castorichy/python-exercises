
def mySplit(string) -> list:
    splited = []
    rev = ""
    for n in string:
        if n == ",":
            splited.append(rev)
            rev = ""
            continue
        else:
            if n != " ":
                rev += n
    return splited

numbers= input("""
\tEnter a comma seperated Values
>>> """)

splited_numbers = mySplit(numbers)
print("List: ", splited_numbers)
print("Tuple: ",tuple(splited_numbers))
print("set: ", set(splited_numbers))
