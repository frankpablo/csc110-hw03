import hw03  # Import the module here
import sys

# Part 3
# ===========
def test_3_6_pick_visualization_good_pick_c1(capsys, monkeypatch):
    # Create a list of input values
    user_inputs = iter(["1"])
    try:
        with monkeypatch.context() as m:
            m.setattr('builtins.input', lambda _: next(user_inputs))
            hw03.grades = [6, 6, 7, 8, 10]
            hw03.pick_visualization(6)
        captured = capsys.readouterr()
        printout = ""
        if captured.out == "":
            printout = "<Nothing>"
        expected = "The average of [6, 6, 7, 8, 10] is 6"
        hint = f"\n\n *** required printout must have: \n{expected}\n *** Your printout is\n{printout}"
        assert expected in captured.out, hint
    except SystemExit:
        print("\n\n****\n Your Error: pick_visualization() raised exit unexpectedly!")
