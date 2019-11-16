# noinspection PyUnusedLocal
def fizz_buzz(number):
    if 0 < number <= 9999:
        if number % 3 == 0 and number % 5 == 0:
            return 'fizz buzz'
        elif check_number(number, 3) and check_number(number, 5):
            return 'fizz buzz'
        elif check_number(number, 3) and number % 5 == 0:
            return 'fizz buzz'
        elif check_number(number, 5) and number % 3 == 0:
            return 'fizz buzz'
        elif number % 3 == 0 or check_number(number, 3):
            return 'fizz'
        elif number % 5 == 0 or check_number(number, 5):
            return 'buzz'
        return number



def check_fizz(number)
    




def check_number(number, digit):
    return str(digit) in str(number)





