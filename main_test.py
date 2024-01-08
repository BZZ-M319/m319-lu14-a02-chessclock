def test_time_until_function_exists():
    from main import chessclock
    assert callable(chessclock), "The 'chessclock' function is not implemented."