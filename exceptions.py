try:
    age = int(input("age: "))
    factor = 10 / age
except (ValueError, ZeroDivisionError) as error:
    print("you did not enter a valid age")
    print(error)
    print(type(error))
else:  # only be executed when no expcetion/not escaping from try block
    print("No exceptions were thrown")
# finally:  # always be executed, can be used to close files, network connections and database connections
#     file1.close()

print("Execution continues")

#####################################################
##Raise exceptions inside your function##


def calculate_factor(age):
    if age <= 0:
        raise ValueError("Age cannot be equal or less than 0.")
    return 10 / age


try:
    calculate_factor(-1)
except ValueError as error:
    print(error)
