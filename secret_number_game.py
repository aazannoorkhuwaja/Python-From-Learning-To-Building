secret_num=17
guess_count=0
guess_limit=3
while(guess_count<guess_limit):
    num=int(input('Guess:'))
    if(num==secret_num):
        print('Thats correct number!!\nCongrats.. you Won!!!')
        break
    else:
        print('Game ended you lost!')
    guess_count+=1