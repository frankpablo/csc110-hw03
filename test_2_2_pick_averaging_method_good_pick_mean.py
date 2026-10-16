import pytest
import hw03


def test_2_2_pick_averaging_method_good_pick_mean(capsys, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: 'a')
    monkeypatch.setattr(hw03, "grades", [6, 6, 7, 8, 10])
    actual = hw03.pick_averaging_method()
    assert actual == pytest.approx(7.4), "Return the calculated mean."
    assert capsys.readouterr().out == "picked: Mean\n"
