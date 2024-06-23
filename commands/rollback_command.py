from typing import Optional

from interface.command import Command
from store.key_value_store import KeyValueStore


class RollbackCommand(Command):
    """
    Command to rollback the most recent transaction in the key-value store.
    """

    def execute(self, store: KeyValueStore) -> Optional[str]:
        """
        Execute the rollback command on the key-value store.

        Args:
            store (KeyValueStore): The key-value store on which to execute the command.

        Returns:
            Optional[str]: "NO TRANSACTION" if no transaction is in progress, else None.
        """
        return store.rollback()