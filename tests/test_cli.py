from bat_pst2mbox.cli import main


def test_not_implemented_exits_nonzero(capsys):
    assert main([]) == 2
    assert "not implemented" in capsys.readouterr().err
