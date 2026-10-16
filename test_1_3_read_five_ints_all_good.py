import pytest
import hw03


@pytest.mark.parametrize("values", [[6, 6, 7, 8, 10], [10, 0, 7, 1, 6]])
def test_1_3_read_five_ints_all_good(capsys, monkeypatch, values):
    user_inputs = iter(map(str, values))
    monkeypatch.setattr("builtins.input", lambda _: next(user_inputs))
    monkeypatch.setattr(hw03, "grades", [0, 0, 0, 0, 0])
    hw03.read_five_ints()
    assert hw03.grades == values, "Store all five inputs in their original order."
    assert capsys.readouterr().out == "", "Valid grade entry should not print extra messages."
