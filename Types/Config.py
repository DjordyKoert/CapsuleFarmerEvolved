from dataclasses import dataclass
from typing import Optional

@dataclass
class Account:
    username: str
    password: str

@dataclass
class Config:
    accounts: dict[str, Account]
    debug: bool
    connectorDrops: Optional[str]
