# tests/conftest.py
import pytest
from data.base import BaseData


class DummyData(BaseData):
    name = "dummy"

    def generate(self):
        self._data = {"id": 1, "msg": "hello"}

    def get_data(self):
        return self._data

    def to_text(self):
        return f'{self._data["id"]}: {self._data["msg"]}'


@pytest.fixture
def dummy_text():
    return DummyData(data_type="text")


@pytest.fixture
def dummy_json(tmp_path):
    output_file = tmp_path / "dummy_json"
    return DummyData(data_type="json", output=str(output_file))


@pytest.fixture
def dummy_csv():
    return DummyData(data_type="csv")
