def ulta_palta(my_string):
    length_string=len(my_string)
    new_string=''
    for i in range(0,length_string,2):
        if i > length_string:
            break
        elif i == length_string -1:
            new_string += my_string[i]
        else:
            j= i+1
            new_string += my_string[j]
            new_string += my_string[i]
    print(new_string)

ulta_palta("BANGLADESH")
