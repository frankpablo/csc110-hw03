import pytest
import hw03


@pytest.mark.parametrize("bad_input", ['pizza', '', '1.5', '-1', '1 0'])
def test_1_1_read_five_ints_one_not_int(capsys, monkeypatch, bad_input):
    user_inputs = iter(["6", bad_input])
    monkeypatch.setattr("builtins.input", lambda _: next(user_inputs))
    monkeypatch.setattr(hw03, "grades", [0, 0, 0, 0, 0])
    with pytest.raises(SystemExit):
        hw03.read_five_ints()
    assert capsys.readouterr().out == 'Error in read_five_ints: input string is not for an integer' + "\n"
