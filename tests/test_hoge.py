from sandbox import hoge


def test_func_a():
    assert hoge.func_a() == 'a'


def test_func_b():
    assert hoge.func_b(1) == 2
