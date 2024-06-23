import threading
from typing import Dict, List, Optional, Union


class KeyValueStore:
    """
    An in-memory key-value store with transaction support and thread safety.
    """

    def __init__(self):
        """
        Initialize the KeyValueStore with an empty store and transaction list.
        Also, initialize a lock for thread safety.
        """
        self.store: Dict[str, int] = {}
        self.transactions: List[Dict[str, Optional[int]]] = []
        self.lock = threading.Lock()

    def set(self, name: str, value: int) -> None:
        """
        Set the variable `name` to the value `value`.

        Args:
            name (str): The name of the variable.
            value (int): The value to set the variable to.
        """
        with self.lock:
            if self.transactions:
                self.transactions[-1][name] = value
            else:
                self.store[name] = value

    def get(self, name: str) -> Union[int, str]:
        """
        Get the value of the variable `name`.

        Args:
            name (str): The name of the variable.

        Returns:
            Union[int, str]: The value of the variable or "NULL" if not set.
        """
        with self.lock:
            if self.transactions:
                for txn in reversed(self.transactions):
                    if name in txn:
                        return txn[name]
            return self.store.get(name, "NULL")

    def unset(self, name: str) -> None:
        """
        Unset the variable `name`.

        Args:
            name (str): The name of the variable.
        """
        with self.lock:
            if self.transactions:
                self.transactions[-1][name] = None
            else:
                self.store.pop(name, None)

    def begin(self) -> None:
        """
        Begin a new transaction.
        """
        with self.lock:
            self.transactions.append({})

    def rollback(self) -> Optional[str]:
        """
        Rollback the most recent transaction.

        Returns:
            Optional[str]: "NO TRANSACTION" if no transaction is in progress, else None.
        """
        with self.lock:
            if not self.transactions:
                return "NO TRANSACTION"
            self.transactions.pop()

    def commit(self) -> Optional[str]:
        """
        Commit all transactions.

        Returns:
            Optional[str]: "NO TRANSACTION" if no transaction is in progress, else None.
        """
        with self.lock:
            if not self.transactions:
                return "NO TRANSACTION"

            while self.transactions:
                txn = self.transactions.pop(0)
                for name, value in txn.items():
                    if value is None:
                        self.store.pop(name, None)
                    else:
                        self.store[name] = value

    def execute_command(self, command) -> Union[None, int, str, Optional[str]]:
        """
        Execute a command on the key-value store.

        Args:
            command (Command): The command to execute.

        Returns:
            Union[None, int, str, Optional[str]]: The result of the command execution, if any.
        """
        return command.execute(self)
