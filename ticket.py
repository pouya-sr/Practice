import os
os.system('cls')

num_of_chairs=int(input(' Enter number of chairs you have : '))
exist_chairs=open('soled.txt','w')
exist_chairs.close()
chairs=[]
user_chair=[]
for i in range(num_of_chairs):
    nums=1
    nums+=i
    chairs.append(nums)
soled=open('soled.txt', 'r') 
soled_chairs=bool(soled.read())


def wellcome():
    print('Hi   wellcome ')
    print(f' we have  {num_of_chairs}  chairs')
    print(chairs)

def user_chioce():
    while True:
        a=input(' Please enter the number of chair you want (for exit type e) : ')
        try:
            while int(a)<=len(chairs):
                user_chair.append(int(a))
                break
            if int(a)>len(chairs):
                print("Invalid entry")
        except:
            if a=='e':
                break
    print('You chioce is :')
    print(f'{user_chair}')
    q=input("Do you want to change it ? ('Y'for yes , 'N' for no , 'D' for delete)")
    if q=='y':
        user_chioce()
    elif q=='d':
        while True:
            w=input('which one do want to delete?(write the number or E for exit : ')
            try:
                user_chair.pop(int(w)-1)
                print(user_chair)
            except:
                if w=='e':
                    break
        print(f'your finial list is  {user_chair}')

def new_list():
    for i in user_chair:
        chairs[int(i)-1]=0
    print('Tank you ',f"you chose {user_chair}")
    print('the lefted list is : ')
    print(chairs)

def run():
    wellcome()
    user_chioce()
    new_list()

run()

new_soled=user_chair
old_soled=soled_chairs
a=open('soled.txt','w')
a.write(str(new_soled))
a.write(str(old_soled))