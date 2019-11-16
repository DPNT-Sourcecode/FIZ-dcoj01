from accelerate_runner.lib.solutions.FIZ import fizz_buzz_solution as fb


class TestFizz_buzz():
    def test_fizz_buzz(self):
        assert (fb.fizz_buzz(3) == 'fizz')
        assert (fb.fizz_buzz(5) == 'buzz')
        assert (fb.fizz_buzz(15) == 'fizz buzz')
        assert (fb.fizz_buzz(999) == 'deluxe')
        assert (fb.fizz_buzz(555) == 'fizz buzz deluxe')
        assert (fb.fizz_buzz(1) == 1)

    def test_check_fizz_buzz_deluxe(self):
        assert (fb.check_fizz_buzz_deluxe(555) == True)
        assert (fb.check_fizz_buzz_deluxe(989) == False)

    def test_check_deluxe(self):
        assert (fb.check_deluxe(999) == True)
        assert (fb.check_deluxe(232) == False)

    def test_check_fizz_buzz(self):
        assert (fb.check_fizz_buzz(15) == True)
        assert (fb.check_fizz_buzz(33) == False)

    def test_check_fizz(self):
        assert (fb.check_fizz(18) == True)
        assert (fb.check_fizz(13) == True)
        assert (fb.check_fizz(22) == False)

    def test_check_fizz_deluxe(self):
        assert (fb.check_fizz_deluxe(33) == True)
        assert (fb.check_fizz(25) == False)

    def test_check_buzz_deluxe(self):
        assert (fb.check_buzz_deluxe(55) == True)
        assert (fb.check_buzz_deluxe(25) == False)

    def test_check_buzz(self):
        assert (fb.check_buzz(10) == True)
        assert (fb.check_buzz(53) == True)
        assert (fb.check_buzz(33) == False)

    def test_check_digit(self):
        assert (fb.check_digit(999) == True)
        assert (fb.check_digit(949) == False)

    def test_check_number(self):
        assert (fb.check_number(335, 3) == True)
        assert (fb.check_number(335, 6) == False)


