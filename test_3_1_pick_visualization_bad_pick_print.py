import pytest
import hw03


def test_3_1_pick_visualization_bad_pick_print(capsys, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: '3')
    monkeypatch.setattr(hw03, "grades", [6, 6, 7, 8, 10])
    with pytest.raises(SystemExit):
        hw03.pick_visualization(7.4)
    assert capsys.readouterr().out == "Error in pick_visualization: incorrect option picked\n"
