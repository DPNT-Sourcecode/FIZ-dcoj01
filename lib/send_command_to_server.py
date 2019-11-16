import sys
from tdl.queue.queue_based_implementation_runner import QueueBasedImplementationRunnerBuilder
from tdl.runner.challenge_session import ChallengeSession
from accelerate_runner.lib.solutions.SUM import sum_solution
from accelerate_runner.lib.solutions.HLO import hello_solution
from accelerate_runner.lib.solutions.ARRS import array_sum
from accelerate_runner.lib.solutions.IRNG import int_range
from accelerate_runner.lib.solutions.FIZ import fizz_buzz_solution
from accelerate_runner.lib.solutions.CHK import checkout_solution
from accelerate_runner.lib.solutions.CHL import checklite_solution
from accelerate_runner.lib.solutions.utils import Utils
from accelerate_runner.lib.solutions.user_input_action import get_user_input


"""
  ~~~~~~~~~~ Running the system: ~~~~~~~~~~~~~
 
    From IDE:
       Run this file from the IDE.
 
    From command line:
       PYTHONPATH=lib python lib/send_command_to_server.py
 
    To run your unit tests locally:
       PYTHONPATH=lib python -m pytest -q test/solution_tests/
 
  ~~~~~~~~~~ The workflow ~~~~~~~~~~~~~
 
    By running this file you interact with a challenge server.
    The interaction follows a request-response pattern:
         * You are presented with your current progress and a list of actions.
         * You trigger one of the actions by typing it on the console.
         * After the action feedback is presented, the execution will stop.
 
    +------+-----------------------------------------------------------------------+
    | Step | The usual workflow                                                    |
    +------+-----------------------------------------------------------------------+
    |  1.  | Run this file.                                                        |
    |  2.  | Start a challenge by typing "start".                                  |
    |  3.  | Read the description from the "challenges" folder.                    |
    |  4.  | Locate the file corresponding to your current challenge in:           |
    |      |   ./lib/solutions                                                     |
    |  5.  | Replace the following placeholder exception with your solution:       |
    |      |   raise NotImplementedError()                                         |
    |  6.  | Deploy to production by typing "deploy".                              |
    |  7.  | Observe the output, check for failed requests.                        |
    |  8.  | If passed, go to step 1.                                              |
    +------+-----------------------------------------------------------------------+
 
    You are encouraged to change this project as you please:
         * You can use your preferred libraries.
         * You can use your own test framework.
         * You can change the file structure.
         * Anything really, provided that this file stays runnable.
 
"""

runner = QueueBasedImplementationRunnerBuilder()\
    .set_config(Utils.get_runner_config())\
    .with_solution_for('sum', sum_solution.compute)\
    .with_solution_for('hello', hello_solution.hello)\
    .with_solution_for('array_sum', array_sum.compute)\
    .with_solution_for('int_range', int_range.generate)\
    .with_solution_for('fizz_buzz', fizz_buzz_solution.fizz_buzz)\
    .with_solution_for('checkout', checkout_solution.checkout)\
    .with_solution_for('checklite', checklite_solution.checklite)\
    .create()

ChallengeSession\
    .for_runner(runner)\
    .with_config(Utils.get_config())\
    .with_action_provider(lambda: get_user_input(sys.argv[1:]))\
    .start()
