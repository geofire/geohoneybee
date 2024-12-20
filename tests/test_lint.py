import pytest
import honeybee.lint as lint


def test_defines_variable():
    assert not lint.defines_variable({"type": ""})
    assert not lint.defines_variable({"type": "note"})
    assert lint.defines_variable({"type": "integer"})


def test_defines_select():
    assert not lint.defines_select({"type": ""})
    assert not lint.defines_select({"type": "integer"})
    assert lint.defines_select({"type": "select_one foo"})
    assert lint.defines_select({"type": "select_multiple foo"})


def test_extract_list_names():
    assert lint.extract_list_names({"type": "integer"}) == tuple()
    assert lint.extract_list_names({"type": "select_one foo"}) == ("foo",)
    assert lint.extract_list_names({"type": "select_one foo or_other"}) == ("foo",)
    assert lint.extract_list_names({"type": "select_one foo bar"}) == ("foo", "bar")


def test_extract_variables():
    assert lint.extract_variables("foo barbaz") == tuple()
    assert lint.extract_variables("foo ${bar}${baz}") == ("bar", "baz")