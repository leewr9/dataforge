import json
from pathlib import Path


def test_generate_file(dummy_json):
    filename = dummy_json.get_filename()
    file_path = Path(filename)
    assert file_path.parent.exists()

    with open(filename, "w", encoding="utf-8") as f:
        f.write(dummy_json.get())

    assert file_path.exists()

    with open(filename, encoding="utf-8") as f:
        line = f.readline().strip()
        loaded = json.loads(line)
        assert loaded["id"] == 1
        assert loaded["msg"] == "hello"

    assert filename.endswith(".jsonl")
