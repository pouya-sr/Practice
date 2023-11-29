
import string
import random
import os

settings={
    'upper':True,
    'lower':True,
    'symbol':True,
    'number':True,
    'spase' :False,
    'lenght':8
}

def get_user_len(option,default):
    while True:
        user_input=input(' enter passwords len (default is 8 enter for default or enter a number):')
        if user_input=='':
            return default
        if user_input.isdigit():
            if 10>=int(user_input)>=4:
              return int(user_input)
            print('invalid input')
            print('you shoud enter a bumber between 4 and 10')
        else:
            print('INVALID')
            print('try again.')

def user_yes_no(option,default):
    while True:
        User_input=input(f'Include {option} (default is {default}) (y for yes n for no enter for default)  : ')
        if User_input=='':
            return default
        if User_input in ['y','n']:
            return User_input=='y'
        print('INVALID , TRY AGAIN')

def get_setting_user(settings):
    for option , default in settings.items():
        if option!='lenght':
            user_choice=user_yes_no(option,default)
            settings[option]=user_choice
        else:
            user_password_len=get_user_len(option,default)
            settings[option]=user_password_len

def choice_ai():
    get_setting_user(settings)
    # choice=list(filter(lambda x :setting[x],['upper','lower','symbol','number','spase']))
    b=[]
    for i in range(settings['lenght']):
        if settings.values():
            lower_case=random.choice(string.ascii_lowercase)
            upper_case=random.choice(string.ascii_uppercase)
            symbols=random.choice(string.punctuation)
            numbers=random.choice(string.digits)
            spase=' '
            items=[lower_case,upper_case,symbols,numbers]
            a=random.choice(items)
            b.append(a)
        elif settings['lenght']:
            pass
        else:
            pass
    return b

def password_loop():
    while True:
        words=choice_ai()
        passwords=''.join(words)
        print('-'*15)
        print(f"The password generated  =  {passwords} ")  
        while True:
            want_another=input('If you want another password enter here (n=no y=ye enter= yes):') 
            if want_another in['y','','n']:
                if want_another==['n']:
                    return
                break
            else:
                print('INVALID')
                print('try again')

def run():
    os.system('cls')
    password_loop()

run()