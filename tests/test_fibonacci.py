import sys
from src import fibonacci as fb


def test_fibonacci():
    error, sequence = fb.fibonacci(5)
    assert error
    assert sequence == [0, 1, 1, 2, 3]
    print(fb.fibonacci(11))


def test_main(capsys, monkeypatch):
    monkeypatch.setattr(sys, "argv", ["fibonacci.py", 5])
    fb.main()
    output = capsys.readouterr()
    assert output.out == "Fibonacci sequence:\n[0, 1, 1, 2, 3]\n"


# def test_spam(capsys):
#     example()
#     captured = capsys.readouterr()
#     assert captured.out == "foo"
