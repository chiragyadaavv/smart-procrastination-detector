from main import main


def test_main_runs(capsys):
    main()
    captured = capsys.readouterr()
    assert "Smart Procrastination Detector" in captured.out
    assert "not started automatically" in captured.out
