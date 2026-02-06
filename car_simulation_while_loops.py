print('...Game Started...\n')
instruction=input('''Start-To start the Car..\n
Stop-To stop the Car...\n
Quit-To exit from the game..!!\n''')


while(1):
    if(instruction=='Start' or instruction=='start'):
        print('Car started...\n')
    elif(instruction=='Stop' or instruction=='stop'):
        print('Car stopped...\n')
    elif(instruction=='Help' or instruction=='help'):
        print('''Start-To start the Car..\n
Stop-To stop the Car...\n
Quit-To exit from the game..!!\n''')
    elif(instruction== 'Quit' or instruction == 'quit'):
        print('Leaving game...\n')
        break
    else:
        print('Not a valid Input. Type Help to get Assistance..\n')
    instruction=input()
    


    
    