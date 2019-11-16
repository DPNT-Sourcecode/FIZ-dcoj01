# noinspection PyUnusedLocal
def fizz_buzz(number):
    if number == range(1, 9999):
        if number % 3 == 0 and number % 5 == 0:
            return 'fizz buzz'
        elif number % 3 == 0:
            return 'fizz'
        elif number % 5 == 0:
            return 'buzz'
        return number

fizz_buzz(3)