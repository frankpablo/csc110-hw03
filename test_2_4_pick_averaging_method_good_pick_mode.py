import pytest
import hw03


def test_2_4_pick_averaging_method_good_pick_mode(capsys, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: 'c')
    monkeypatch.setattr(hw03, "grades", [6, 6, 7, 8, 10])
    actual = hw03.pick_averaging_method()
    assert actual == 6, "Return the calculated mode."
    assert capsys.readouterr().out == "picked: Mode\n"


def test_mode_tie_uses_first_encountered_value(capsys, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "c")
    monkeypatch.setattr(hw03, "grades", [6, 6, 7, 8, 8])
    assert hw03.pick_averaging_method() == 6
    assert capsys.readouterr().out == "picked: Mode\n"
