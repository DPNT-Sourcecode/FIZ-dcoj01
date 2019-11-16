from accelerate_runner.lib.solutions.FIZ import fizz_buzz_solution as fb

class TestFizz_buzz():
    def test_fizz_buzz(self):
       assert (fb.fizz_buzz(3) == 'fizz')
       assert (fb.fizz_buzz(5) == 'buzz')
       assert (fb.fizz_buzz(15) == 'fizz buzz')
       assert (fb.fizz_buzz(35) == 'fizz buzz')
