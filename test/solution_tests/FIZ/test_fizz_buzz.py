from unittest import TestCase
from accelerate_runner.lib.solutions.FIZ import fizz_buzz_solution as fb

class TestFizz_buzz(TestCase):
    assert(fb.fizz_buzz(3) == 'fizz')



