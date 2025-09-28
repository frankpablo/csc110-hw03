import pytest
import hw03  # Import the module here
import sys

# Part 1
# ===========
def test_1_2_read_five_ints_not_in_range(capsys, monkeypatch):
    # Create a list of input values
    user_inputs = iter(["6","17", "6", "6", "6"])
    with monkeypatch.context() as m, pytest.raises(SystemExit) as e:
        m.setattr('builtins.input', lambda _: next(user_inputs))
        grades = [0,0,0,0,0] # initialized with five zeros
        hw03.read_five_ints()
    captured = capsys.readouterr()
    expected = "Error in read_five_ints: input integer outside of range"
    assert expected in captured.out, "Tip: Did you check that the input is int he range?"