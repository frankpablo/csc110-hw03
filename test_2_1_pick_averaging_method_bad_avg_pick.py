import pytest
import hw03


def test_2_1_pick_averaging_method_bad_avg_pick(capsys, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: 's')
    monkeypatch.setattr(hw03, "grades", [6, 6, 7, 8, 10])
    with pytest.raises(SystemExit):
        hw03.pick_averaging_method()
    assert capsys.readouterr().out == "Error in pick_averaging_method: incorrect option picked\n"
