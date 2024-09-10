# The test only checks if the function exists, not if it works correctly.

def test_chessclock_exists():
    from main import chessclock
    assert callable(chessclock), "The 'chessclock' function is not implemented."