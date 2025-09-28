import pytest
import hw03  # Import the module here
import sys

# Part 3
# ===========
def test_3_1_pick_visualization_bad_pick_print(capsys, monkeypatch):
    # Create a list of input values
    user_inputs = iter(["3"])
    with monkeypatch.context() as m, pytest.raises(SystemExit) as e:
        m.setattr('builtins.input', lambda _: next(user_inputs))
        hw03.grades = [6, 6, 7, 8, 10]
        hw03.pick_visualization(7.4)
    captured = capsys.readouterr()
    printout = ""
    if captured.out == "":
        printout = "<Nothing>"
    expected = "Error in pick_visualization: incorrect option picked"
    hint = f"\n\n *** required printout must have: \n{expected}\n *** Your printout is\n{printout}"
    assert expected in captured.out, hint