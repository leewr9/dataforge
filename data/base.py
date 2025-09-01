from abc import ABC, abstractmethod
from typing import Any
import json
import pandas as pd


class BaseData(ABC):
    @abstractmethod
    def generate(self) -> None:
        pass

    @abstractmethod
    def get_data(self) -> dict:
        pass

    @abstractmethod
    def to_text(self) -> str:
        pass

    def to_json(self) -> str:
        return json.dumps(self.get_data())

    def to_csv(self, header=False) -> str:
        df = pd.DataFrame([self.get_data()])
        return df.to_csv(index=False, header=header, lineterminator="\n")

    def get(self, header=False) -> Any:
        self.generate()
        if self.data_type == "text":
            return self.to_text().strip()
        elif self.data_type == "json":
            return self.to_json().strip()
        elif self.data_type == "csv":
            return self.to_csv(header).strip()
        raise ValueError(f"Unsupported data type: {self.data_type}")

    def get_filename(self) -> str:
        if not self.name:
            raise ValueError("Data name is not defined.")

        if self.data_type == "text":
            return f"{self.name}.log"
        elif self.data_type == "json":
            return f"{self.name}.jsonl"
        elif self.data_type == "csv":
            return f"{self.name}.csv"

        return f"{self.name}.txt"
