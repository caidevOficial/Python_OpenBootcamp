
for i in range(2):
    my_variable = input('Enter something: ')
    print(
        '###################################################',
        f'In the {i+1}° attempt you entered: {my_variable}',
        f'The type of my_variable is: {type(my_variable)}',
        '###################################################',
        sep='\n'    
    )
