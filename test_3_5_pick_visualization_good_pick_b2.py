import pytest
import hw03


def test_3_5_pick_visualization_good_pick_b2(capsys, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: '2')
    monkeypatch.setattr(hw03, "grades", [6, 6, 7, 8, 10])
    hw03.pick_visualization(7)
    assert capsys.readouterr().out == 'Annotated grades: \n 6  6 (7)8 10 \n'
