import random

number = random.randint(0, 100)

guess = -1
num_guesses = 0

while guess != number:

    guess_str = input("猜數字 0~100：")
    
    guess = int(guess_str)
    
    num_guesses +=1
    
    if guess < number:
        print("太小了!")
        
    elif guess > number:
        print("太大了!")
        
print(f"你共猜了 {num_guesses} 次! 答案是"+ f'{number}')