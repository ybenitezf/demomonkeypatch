# -*- coding: utf-8 -*-


def test_demo():
    """test llamamdo al codigo real"""
    from demo import sumaClient

    assert sumaClient(1, 2) == 3


def test_demo2(monkeypatch):
    """test usando un mock del codigo"""
    import demo

    def fakesuma(a, b):
        print("Hey this is a fake !!!!")
        return 4

    monkeypatch.setattr(demo, 'suma', fakesuma)
    # no tiene sentido lo se, pero es para demostrar que sumaClient no
    # llama a suma() sino a fakesuma()
    assert demo.sumaClient(1, 3) == 4


def test_demo3(monkeypatch):
    """Mock elemento del sistema"""
    import os.path

    def fakejoin(*args, **kwargs):
        return '/esto/siempre'

    monkeypatch.setattr(os.path, 'join', fakejoin)
    assert os.path.join('/home', 'yoel') == '/esto/siempre'
