import hw03  # Import the module here
import sys

# Part 2
# ===========
def test_2_2_pick_averaging_method_good_pick_mean(capsys, monkeypatch):
    # Create a list of input values
    user_inputs = iter(["a"])
    try:
        with monkeypatch.context() as m:
            m.setattr('builtins.input', lambda _: next(user_inputs))
            hw03.grades = [6, 6, 7, 8, 10]
            hw03.pick_averaging_method()
        captured = capsys.readouterr()
        printout = ""
        if captured.out == "":
            printout = "<Nothing>"
        expected = "picked: Mean"
        hint = f"\n\n *** required printout must have: \n{expected}\n *** Your printout is\n{printout}"
        assert expected in captured.out, hint
    except SystemExit:
        print("\n\n****\n Your Error: pick_averaging_method() raised exit unexpectedly!")
        assert False