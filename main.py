import random
import sys
from termcolor import colored
import vlc

p = vlc.MediaPlayer("./sound.mp3")
p.audio_set_volume(60)
p.play()


def rainbow_text(x):
    pos = 0
    color_list = ['red', 'green', 'blue', 'yellow', 'white', 'magenta']
    ret = ""
    for i in range(len(x)):
        if pos > len(color_list) - 1:
            pos = 0
        ret += colored(x[i], color_list[pos])
        pos += 1
    return ret


words_five = [x.replace('\n', '') for x in open('./words.txt', 'r+').readlines() if len(x.replace('\n', '')) == 5]


print("WORDLE")
print("Type a 5 letter word:\n")
play_again = ""

while play_again != "q":
    word = random.choice(words_five).lower()

    for attempt in range(1, 7):
        guess = input().lower()

        sys.stdout.write('\x1b[1A')
        sys.stdout.write('\x1b[2K')

        for i in range(min(len(guess), 5)):
            if guess[i] == word[i]:
                print(colored(guess[i], 'green'), end="")
            elif guess[i] in word:
                print(colored(guess[i], 'yellow'), end="")
            else:
                print(guess[i], end="")
        print()

        if guess == word:
            plural = 'es' if attempt > 1 else ''
            print(f"{colored(f'Congrats! You got the wordle in {attempt}', 'cyan')} {rainbow_text(f'guess{plural}')}")
            p.stop()
            v = vlc.MediaPlayer("./win.mp3")
            v.audio_set_volume(75)
            v.play()
            break

        elif attempt == 6:
            print(f"Sorry the wordle was.. {colored(word, 'red')}")
    play_again = input("Type q to exit.")