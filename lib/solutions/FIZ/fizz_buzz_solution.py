# noinspection PyUnusedLocal
def fizz_buzz(number):
    if 0 < number <= 9999:
        if check_fizz_buzz_deluxe(number):
            return "fizz buzz deluxe"
        elif check_deluxe(number):
            return "deluxe"
        elif check_fiz_buzz(number):
            return "fizz buzz"
        elif check_fizz(number):
            return "fizz"
        elif check_buzz(number):
            return "buzz"
        return number


def check_fizz(number):
    return number % 3 == 0


def check_buzz(number):
    return number % 5 == 0


def check_fiz_buzz(number):
    return (number % 3==0 and number % 5 == 0) or \
           (check_number(number, 3) and check_number(number, 5)) or \
           (check_number(number, 3) and number % 5 == 0) or \
           (check_number(number, 5) and number % 3 == 0)


def check_deluxe(number):
    return number > 10 and check_digit(number)


def check_fizz_buzz_deluxe(number):
    return check_deluxe(number) and check_fiz_buzz(number)


def check_digit(number):
    s = str(number)
    check_number = int(s[0]*len(s))
    return check_number == number


def check_number(number, digit):
    return str(digit) in str(number)










