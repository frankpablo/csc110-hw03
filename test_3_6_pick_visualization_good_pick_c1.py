import pytest
import hw03


def test_3_6_pick_visualization_good_pick_c1(capsys, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: '1')
    monkeypatch.setattr(hw03, "grades", [6, 6, 7, 8, 10])
    hw03.pick_visualization(6)
    assert capsys.readouterr().out == 'The average of [6, 6, 7, 8, 10] is 6\n'
