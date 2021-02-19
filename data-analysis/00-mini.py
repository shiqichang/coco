#!/Users/changshiqi/.virtualenvs/carrobot_bokeh/bin/python
import PyPDF2
import pyttsx3
import random
import requests
import smtplib
import time
from bs4 import BeautifulSoup
from datetime import datetime
from email.message import EmailMessage
from playsound import playsound


def roll_the_dice():
    """ 1.骰子模拟器 """
    while int(input('Press 1 to roll the dice or 0 to exit:\n')):
        print(random.randint(1, 6))


def rock_paper_scissors():
    """ 2.石头剪刀布游戏 """
    choices = ['Rock', 'Paper', 'Scissors']
    computer = random.choice(choices)
    player = False
    cpu_score = 0
    player_score = 0
    while True:
        player = input('Rock, Paper or Scissors?\n').capitalize()
        # 判断游戏者和电脑的选择
        if player == computer:
            print('Tie!')
        elif player == 'Rock':
            if computer == 'Paper':
                print('You lose...', computer, 'covers', player)
                cpu_score += 1
            else:
                print('You win!', player, 'smashes', computer)
                player_score += 1
        elif player == 'Paper':
            if computer == 'Scissors':
                print('You lose...', computer, 'cut', player)
                cpu_score += 1
            else:
                print('You win!', player, 'covers', computer)
                player_score += 1
        elif player == 'Scissors':
            if computer == 'Rock':
                print('You lose...', computer, 'smashes', player)
                cpu_score += 1
            else:
                print('You win!', player, 'cut', computer)
                player_score += 1
        elif player == 'E':
            print('Final Scores:')
            print(f'CPU:{cpu_score}')
            print(f'Player:{player_score}')
            break
        else:
            print("That's not a valid play. Check your spelling!")
        computer = random.choice(choices)


def generate_password():
    """ 3.随机密码生成器 """
    passlen = int(input('Enter the length of password:\n'))
    s = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?'
    p = ''.join(random.sample(s, passlen))
    print(p)


def generate_sentence():
    """ 4.句子生成器 """
    color = input('Enter a color: ')
    plural_noun = input('Enter a pluarl noun: ')
    celebrity = input('Enter a celebrity: ')
    print('Roses are', color)
    print(plural_noun + ' are blue')
    print('I love', celebrity)


def guess_the_number():
    """ 5.猜数字游戏 """
    number = random.randint(1, 10)
    for _ in range(0, 3):
        user = int(input('Guess the number: '))
        if user == number:
            print('Hurray!!')
            print(f"You guessed the number right it's {number}")
            break
        elif user > number:
            print('You guess is too high.')
        elif user < number:
            print('You guess is too low.')
    else:
        print(f'Nice Try! But the number is {number}')


def generate_story():
    """ 6.故事生成器 """
    when = ['A few years ago', 'Yesterday', 'Last night', 'A long time ago', 'On 20th Jan']
    who = ['a rabbit', 'an elephant', 'a mouse', 'a turtle', 'a cat']
    residence = ['Barcelona', 'India', 'Germany', 'Venice', 'England']
    went = ['cinema', 'university', 'seminar', 'school', 'laundry']
    happened = ['made a log of friends', 'eats a burger', 'found a secret key', 'solved a mistery', 'wrote a book']
    print(random.choice(when) + ', ' + random.choice(who) + ' that lived in ' + 
    random.choice(residence) + ', went to the ' + random.choice(went) + ' and ' + 
    random.choice(happened))


def slice_email_address():
    """ 7.邮件地址切片器 """
    # Get the user's email address
    email = input('What is your email address?: ').strip()
    # Slice out the user name
    user_name = email[:email.index('@')]
    # Slice out the domain name
    domain_name = email[email.index('@')+1:]
    # Format message
    res = f"Your username is '{user_name}' and your domain name is '{domain_name}'"
    # Display the result mesage
    print(res)


def send_email_auto():
    """ 8.自动发送邮件 """
    email = EmailMessage()  # Creating a object for EmailMessage
    email['from'] = 'xyz name'  # Person who is sending
    email['to'] = 'xyz id'  # Who we are sending
    email['subject'] = 'xyz subject'  # Subject of email
    email.set_content('Xyz content of email')  # Content of email
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        # Sending request to server
        smtp.ehlo()  # Server object
    smtp.starttls()  # Used to send data between server and client
    smtp.login('EmailID', 'Password')  # Login id and password of gmail
    smtp.send_message(email)  # Sending email
    print('email send')  # Printing success message


def word_adventure():
    """ 9.文字冒险游戏 """
    name = str(input('Enter Your Name:\n'))
    print(f'{name} you are stuck in a forest. Your task is to get out from the forest without dieing.')
    print('You are walking threw forest and suddenly a wolf comes in your way. Now your have two options.')
    print('1.Run 2.Climb The Nearest Tree')
    user = int(input('Choose one option 1 or 2: '))
    if user == 1:
        print('You Died!!')
    elif user == 2:
        print('You Survived!!')
    else:
        print('Incorrect Input.')


def hangman():
    """ 10.Hangman """
    name = input('What is your name? ')
    print('Hello, ' + name, 'Time to play hangman!')
    time.sleep(1)
    print('Start guessing...\n')
    time.sleep(0.5)
    # A List Of Secret Words
    words = ['python', 'programming', 'treasure', 'creative', 'medium', 'horror']
    word = random.choice(words)
    guesses = ''
    turns = 5
    while turns > 0:
        failed = 0
        for char in word:
            if char in guesses:
                print(char, end='')
            else:
                print('_', end='')
                failed += 1
        if failed == 0:
            print('\nYou Won!')
            break
        guess = input('\nGuess a character: ')
        guesses += guess
        if guess not in word:
            turns -= 1
            print('\nWrong!')
            print('\nYou have', turns, 'more guesses.')
            if turns == 0:
                print('\nYou Lose!')


def clock():
    """ 11.闹钟⏰ """
    alarm_time = input('Enter the time of alarm to be set:HH:MM:SS PP\n')
    alarm_hour = alarm_time[0:2]
    alarm_minute = alarm_time[3:5]
    alarm_seconds = alarm_time[6:8]
    alarm_period = alarm_time[9:11].upper()
    print('Setting up alarm...')
    while True:
        now = datetime.now()
        current_hour = now.strftime('%I')
        current_minute = now.strftime('%M')
        current_seconds = now.strftime('%S')
        current_period = now.strftime('%p')
        if alarm_period == current_period:
            if alarm_hour == current_hour:
                if alarm_minute == current_minute:
                    if alarm_seconds == current_seconds:
                        print('Wake Up!')
                        playsound('audio.mp3')  # download the alarm sound from link
                        break


def audio_books():
    """ 12.有声读物 """
    pdf_reader = PyPDF2.PdfFileReader(open('file.pdf'), 'rb')
    speaker = pyttsx3.init()
    for page_num in range(pdf_reader.numPages):
        text = pdf_reader.getPage(page_num).extractText()
        speaker.say(text)
        speaker.runAndWait()
    speaker.stop()


def weather():
    """ 13.天气应用 """
    print('Enter the city name:')
    city = input()
    city += ' weather'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    city = city.replace(' ', '+')
    res = requests.get(f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
    print('Searching in google......\n')
    soup = BeautifulSoup(res.text, 'html.parser')
    print(soup)
    location = soup.select('#wob_loc')[0].getText().strip()
    time = soup.select('#wob_dts')[0].getText().strip()
    info = soup.select('#wob_dc')[0].getText().strip()
    weather = soup.select('#wob_tm')[0].getText().strip()
    print(location)
    print(time)
    print(info)
    print(weather + '°C')


if __name__ == '__main__':
    # roll_the_dice()
    # rock_paper_scissors()
    # generate_password()
    # generate_sentence()
    # guess_the_number()
    # generate_story()
    # slice_email_address()
    # send_email_auto()
    # word_adventure()
    # hangman()
    # clock()
    # audio_books()
    weather()
