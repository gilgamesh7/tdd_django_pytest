from dataclasses import dataclass


@dataclass
class Company:
    name: str
    stock_symbol: str

    @property
    def describe_company(self)->str:
        return f"{self.name}:{self.stock_symbol}"

