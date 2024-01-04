def main():
    "Calculator program that can only perform addition!!"
    x = int(input('Please type the firt value: '))
    y = int(input('Please type the second value: '))
    op = input("Please type the operator from '+-*/': ")
    while op not in ['+', '-', '*', '/']:
        print('sorry, invalid operator')
        op = input("Please type the operator from '+-*/': ")

    # TODO: ask user to select 1 operation from "+-*/"
    # then perform based on the operation

    # Perform calculation
    result = eval(f'{x} {op} {y}')


    print(f'The result of {x} {op} {y} is {result}.')


if __name__ == '__main__':
    main()
