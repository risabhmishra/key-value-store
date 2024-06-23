from typing import Optional

from interface.command import Command
from store.key_value_store import KeyValueStore


class CommitCommand(Command):
    """
    Command to commit all transactions in the key-value store.
    """

    def execute(self, store: KeyValueStore) -> Optional[str]:
        """
        Execute the commit command on the key-value store.

        Args:
            store (KeyValueStore): The key-value store on which to execute the command.

        Returns:
            Optional[str]: "NO TRANSACTION" if no transaction is in progress, else None.
        """
        return store.commit()