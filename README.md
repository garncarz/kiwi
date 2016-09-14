# Kiwi

This is an implementation of a simple flight segments (itineraries) finder, as specified in [task.md](task.md).


## Installation

Needed: Python 3.5

1. `virtualenv3 virtualenv`
2. Make sure `virtualenv/bin` is in `PATH`.
3. `pip install -r requirements.txt`
4. Create `flights/settings_local.py` if customized settings are needed.


## Use

Run `cat input.csv | ./find_combinations.py`.


## Testing

Run `./test.sh`.
Test coverage is located under the `htmlcov` directory then.
