import  random

print('''H A N G M A N
''')

status = ''
while status != 'exit':
    status = input('Type "play" to play the game, "exit" to quit:')
    if status == 'play':
        words_list = ['python', 'java', 'kotlin', 'javascript']
        right_word =  random.choice(words_list)
        hidden_word = '-' * len(right_word)

        attempt = 8
        letters = []
        while attempt > 0:
            print('\n' + hidden_word)
            letter = input("Input a letter:")
            if len(letter) != 1:
                print('You should input a single letter')
            elif not letter.islower():
                print('It is not an ASCII lowercase letter')

            elif letter in letters:
                print('You already typed this letter')
            elif letter in right_word:
                for i in range(len(right_word)):
                    if letter == right_word[i]:
                        hidden_word = hidden_word[:i] + letter + hidden_word[i +1:]
            else:
                print('No such letter in the word')
                attempt -= 1
            letters.append(letter)


if '-' in hidden_word:
    print('You are hanged!')
else:
    print('''You guessed the word!
You survived!''')

