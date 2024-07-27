import random

def ending(n):
    end = ('ку', 'ки', 'ок')
    cases = (2, 0, 1, 1, 1, 2)  
    return f'попыт{end[2]}' if n % 100 > 4 and n % 100 < 20 else f'попыт{end[cases[min(n % 10, 5)]]}'

print('Привет, дорогой пользователь!')
print('Давай поиграем в угадай число.')

while True:
    lower_limit = input('Введите нижний предел чисел: ')
    
    if lower_limit.isdigit():
        lower_limit = int(lower_limit)
        
        if lower_limit < 0:
            print('Нижний предел не может быть меньше 0.')
        else:
            break
    
    else:
        print('Введите целое число.')

while True:
    upper_limit = input('Введите верхний предел чисел: ')

    if upper_limit.isdigit():
        upper_limit = int(upper_limit)
        
        if upper_limit <= lower_limit:
            print('Верхний предел не может быть меньше или равен нижнему.')
        else:
            break
    
    else:
        print('Введите целое число.')

random_number = random.randint(lower_limit, upper_limit)
print(f'Компьютер загадал число в диапазоне от {lower_limit} до {upper_limit}. Удачи!')
attempts = 0

user_guess = input(f'Введите ваше предположение: ')
while True:
    attempts += 1
    
    if user_guess.isdigit():
        user_guess = int(user_guess)
        
        if user_guess < lower_limit or user_guess > upper_limit:
            text = 'Ваше число выходит за установленные пределы.'
        elif user_guess == random_number:
            print(f'Поздравляем! Вы угадали число за {attempts} {ending(attempts)}.')
            break
        elif user_guess < random_number:
            text = 'Ваше число меньше загаданного.'
        else:
            text = 'Ваше число больше загаданного.'
    
    else:
        print('Введите целое число.')
    
    user_guess = input(f'{text} Попробуйте ещё раз: ')