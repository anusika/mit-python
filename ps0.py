#Problem Set 0
#Name: Anusika Nijher
#Collaborators: None
#Time: 15 min
x= True

while(x):
    x = False
    first_name = str(raw_input('Enter your first name:'))
    last_name = str(raw_input ('Enter your last name:'))
    print first_name,last_name
    repeat = str(raw_input('Do you want to do this again? Y/N:'))
    if(repeat == 'Y'):
        x = True
    else:
        x = False

