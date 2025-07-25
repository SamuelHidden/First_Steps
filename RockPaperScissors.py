import random
import time
game=['rock', 'paper', 'scissors']
AI_score=0
player_score=0
while True:
    player_choise = input('rock , paper or scissors:').lower()
    AI_choise = random.choice(game)
    if player_choise=="rock" or player_choise=="paper" or player_choise=='scissors':
      if AI_choise==player_choise:
               for i in range(3,0,-1):
                    print(i)
                    time.sleep(1)
               print(' AI have chosen ' + AI_choise.upper(), 'and you have chosen ' + player_choise.upper())
               print('draw')
               print('Ai score is   :   ' + str(AI_score))
               print('your score is   :   ' + str(player_score))
               print('-----------------------------')
               YesOrNo = input("Play again?").lower()
               if YesOrNo != 'yes':
                   break
               continue
      elif AI_choise=="rock" and player_choise=='scissors' or AI_choise=="paper" and player_choise=='rock' or AI_choise=='scissors' and player_choise=='paper':
                for i in range(3,0,-1):
                      print(i)
                      time.sleep(1)
                print('Sadenly  AI have chosen ' + AI_choise.upper(), 'and your choiсe is  ' + player_choise.upper())
                print('You lose this battle, but not the war!')
                AI_score += 1
                print('Ai score is  :   ' + str(AI_score))
                print('your score is   :  ' + str(player_score))
                print('-----------------------------')
                YesOrNo = input("Play again?").lower()
                if YesOrNo != 'yes':
                    break
                continue
      else:
          for i in range(3, 0, -1):
              print(i)
              time.sleep(1)
          print('NO WAY  AI have chosen ' + AI_choise.upper(), 'and your chose is ' + player_choise.upper())
          print('Flowless victory bro!')
          player_score+=1
          print('Ai score is   :   ' + str(AI_score))
          print('your score is  :    ' + str(player_score))
          print('-----------------------------')
          YesOrNo = input("Play again?").lower()
          if YesOrNo != 'yes':
              break
          continue
    elif player_choise not in game:
           print("ERROR 228 wrong input ,only rock , paper , scissors")
           continue
