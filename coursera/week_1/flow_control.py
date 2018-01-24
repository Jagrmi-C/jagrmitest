import random
number = random.randint(0, 101)

while True:
    answer = input("Input your number: ")
    if not answer or answer == 'exit':
        break
    if not answer.isdigit():
        print('Enter the correct number!!!')
        continue
    user_answer = int(answer)
    if user_answer > number:
        print(f"The number is less than {user_answer}")
        continue
    if user_answer < number:
        print(f"The number is greater than {user_answer}")
        continue
    else:
        print('YES!!!')
        break
