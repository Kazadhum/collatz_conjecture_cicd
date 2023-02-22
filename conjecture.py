def algorhythm():

    start_num = int(input("Select a starting number: \n"))
    
    current_number = start_num

    step_number = 0

    while(current_number) != 1:
        
        if (current_number % 2 == 0):
            is_even = True
            print(f'{current_number} is even!')
        else:
            is_even = False
            print(f'{current_number} is odd!')
        
        if (is_even == True):
            print(f'{current_number} / 2 = {current_number/2}')
            current_number = current_number / 2
        else:
            print(f'{current_number}*3 + 1 = {current_number*3 + 1}')
            current_number = current_number*3 + 1

        step_number = step_number + 1

        print(f'Number of steps: {step_number}')
        print('This project makes use of CI techniques')


if __name__ == '__main__':
    algorhythm()