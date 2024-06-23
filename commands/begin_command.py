from interface.command import Command
from store.key_value_store import KeyValueStore


class BeginCommand(Command):
    """
    Command to begin a new transaction in the key-value store.
    """

    def execute(self, store: KeyValueStore) -> None:
        """
        Execute the begin command on the key-value store.

        Args:
            store (KeyValueStore): The key-value store on which to execute the command.
        """
        store.begin()