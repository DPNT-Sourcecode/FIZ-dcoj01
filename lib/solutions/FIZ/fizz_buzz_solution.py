# noinspection PyUnusedLocal
def fizz_buzz(number):
    if number > 0 and number <=9999:
        if number % 3 == 0 and number % 5 == 0:
            return 'fizz buzz'
        elif number % 3 == 0:
            return 'fizz'
        elif number % 5 == 0:
            return 'buzz'
        return number


