print('...Game Started...\n')
started=False
stopped=False
instruction=input('> ')
while(1):
    if(instruction=='Start' or instruction=='start'):
        if(started):
            print('Car is already started..\n')
        else:
            started=True
            print('Car started...\n')
            
    elif(instruction=='Stop' or instruction=='stop'):
        if(stopped):
            print('Hey car is stopped!! what are you doing?\n')
        else:
            stopped=True
            print('Car stopped...\n')
            
    elif(instruction=='Help' or instruction=='help'):
        print('''Start-> To start the Car..\n
Stop-> To stop the Car...\n
Quit-> To exit from the game..!!\n''')
        
    elif(instruction== 'Quit' or instruction == 'quit'):
        print('Leaving game...\n')
        break
    else:
        print('Not a valid Input. Type Help to get Assistance..\n')
    instruction=input()
    


    
    