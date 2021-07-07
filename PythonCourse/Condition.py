# minimum Age ......................................

# if, elif-> else if, else

#################################
#    : اگر سن کمتر از 18 بود   #
#      اتفاق مورد نظر          #
#    : در غیر این صورت         #
#      اتفاق مورد نظر          #
#################################

age = int(input("How many is your age ? \n"))

if age < 18:
    print("Permision denied !\nAGE ERROR !\n")
elif age == 18:
    print("Permision allowed !\n")
else:
    print("Your are too old !\n")
