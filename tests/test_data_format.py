import json
import pytest


def test_text_format(dummy_text):
    result = dummy_text.get()
    assert result == "1: hello"


def test_json_format(dummy_json):
    result = dummy_json.get()
    assert isinstance(result, str)
    assert json.loads(result) == {"id": 1, "msg": "hello"}


def test_csv_format(dummy_csv):
    result = dummy_csv.get(header=True)
    lines = result.strip().split("\n")
    assert lines[0] == "id,msg"
    assert lines[1].startswith("1,hello")
