# Ryan Lugo: RJL 10/27/21

first_string = input("First Word?: ")
second_string = input("Second Word?: ")

if first_string > second_string:
    print(first_string + " is bigger than " + second_string + " in length.")
elif first_string < second_string:
    print(second_string + " is bigger than " + first_string + " in length.")
elif first_string == second_string:
    print(first_string + " is equal to " + second_string + " in length.")
else:
    print("Error.")
