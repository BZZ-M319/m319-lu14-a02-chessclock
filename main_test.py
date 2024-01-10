def test_chessclock_exists():
    from main import chessclock
    assert callable(chessclock), "The 'chessclock' function is not implemented."