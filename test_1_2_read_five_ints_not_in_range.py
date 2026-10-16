import pytest
import hw03


@pytest.mark.parametrize("bad_input", ["11", "17"])
def test_1_2_read_five_ints_not_in_range(capsys, monkeypatch, bad_input):
    user_inputs = iter(["6", bad_input])
    monkeypatch.setattr("builtins.input", lambda _: next(user_inputs))
    monkeypatch.setattr(hw03, "grades", [0, 0, 0, 0, 0])
    with pytest.raises(SystemExit):
        hw03.read_five_ints()
    assert capsys.readouterr().out == 'Error in read_five_ints: input integer outside of range' + "\n"
