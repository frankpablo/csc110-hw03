import hw03  # Import the module here
import sys

# Part 1
# ===========
def test_1_3_read_five_ints_all_good(capsys, monkeypatch):
    # Create a list of input values
    user_inputs = iter(["6","6","7","8","10"])
    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda _: next(user_inputs))
        grades = [0,0,0,0,0] # initialized with five zeros
        hw03.read_five_ints()
    actual = hw03.grades
    expected = [6, 6, 7, 8, 10]
    hint = f"\n\n *** required values after call: \n{expected}\n *** Your actual values: \n{actual}"
    assert expected == actual, hint