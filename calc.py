def main():
    "Calculator program"
    x = int(input('Please type the firt value: '))
    y = int(input('Please type the second value: '))

    # TODO: ask user to select 1 operation from "+-*/"
    # then perform based on the operation

    # Perform addition
    result = x + y

    print(f'The result of {x} + {y} is {result}')


if __name__ == '__main__':
    main()
