# print() params ----------------------------
    # multiline strings
multiline_string = """hello my name is kasra
this is my course about learning python"""
print(multiline_string)
    # quotes example in strings and !r symbol
double_single_quotes = "hello my name is 'kasra'"
print(double_single_quotes)
    # next line symbol
next_line_string = "hello my name is kasra\nIm 16 years old."
print(next_line_string)
    # formated string {0}&{1}
name = "kasra"
age = 16
id = 634
print("my name is {0} . Im {1} years old . and my id is {2}".format(name,age,id))

    # other shape of formated strings {arg1}&{arg2}
print("my name is {arg1} . Im {arg2} years old . and my id is {arg3}".format(arg1=name,arg2=age,arg3=id))
    
    # columns in formated strings
username = "kasra"
print("string1 is {string!r}".format(string=username))

# input() params ----------------------------

input_age = int(input("how old are you? :"))
print(type(age))