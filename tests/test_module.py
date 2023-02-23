from goodstuff import module


def test_module():
    s = module.Example(name="a", uuid=2, content={})
    assert s.content == {}
    assert s.name == "a"


def test_fail():
    assert False
