import random
import hangman_stages
words = ['apple','banana','orange']
select_words = random.choice(words) #apple
print(select_words)
space=[]
lives = 6
for i in select_words:
     space += '_'
print(space)

game_over = False
while not  game_over:
     guessed_letter = input("guess a letter").lower() # p
     for position in range(len(select_words)): # 0 1 2 3 4
          letter = select_words[position]
          if letter == guessed_letter:
               space[position] = guessed_letter
     print(space)
     if guessed_letter not in select_words:
          lives -=1
          if lives == 0:
               game_over = True
               print('you lose')
     if  '_' not in space:
          game_over = True
          print('you win')
     print(hangman_stages.stages[lives])







