from typing import Iterable, Optional

class Account:
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password

class Config:
    def __init__(
            self, 
            accounts: dict[str, Account], 
            debug: bool = False, 
            connectorDrops: Optional[str] = None,
        ) -> None:
        self.accounts = accounts
        self.debug = debug
        self.connectorDrops = connectorDrops
