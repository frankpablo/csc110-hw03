import pytest
import hw03


def test_2_3_pick_averaging_method_good_pick_median(capsys, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: 'b')
    monkeypatch.setattr(hw03, "grades", [6, 6, 7, 8, 10])
    actual = hw03.pick_averaging_method()
    assert actual == 7, "Return the calculated median."
    assert capsys.readouterr().out == "picked: Median\n"
