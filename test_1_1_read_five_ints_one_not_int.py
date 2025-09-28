import pytest
import hw03  # Import the module here
import sys

# Part 1
# ===========
def test_1_1_read_five_ints_one_not_int(capsys, monkeypatch):
    # Create a list of input values
    user_inputs = iter(["6","pizza", "", "", ""])
    # monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    with monkeypatch.context() as m, pytest.raises(SystemExit) as e:
        m.setattr('builtins.input', lambda _: next(user_inputs))
        grades = [0,0,0,0,0] # initialized with five zeros
        hw03.read_five_ints()
    captured = capsys.readouterr()
    expected = "Error in read_five_ints: input string is not for an integer"
    assert expected in captured.out, "Tip: Did you check the input value is an int?"
