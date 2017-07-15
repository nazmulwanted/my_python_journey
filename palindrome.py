def palindrome_finder(my_string):
    new_string=''
    j=len(my_string)-1
    for i in range(0,len(my_string)):
        new_string += my_string[j]
        j-=1
    if new_string == my_string:
        print("Entered word is a palindrome.")
    else:
        print("Entered word is not a palindrome.")
palindrome_finder("mathama")
