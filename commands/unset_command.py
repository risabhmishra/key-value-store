from interface.command import Command
from store.key_value_store import KeyValueStore


class UnsetCommand(Command):
    """
    Command to unset a variable in the key-value store.
    """

    def __init__(self, name: str):
        """
        Initialize the UnsetCommand.

        Args:
            name (str): The name of the variable to unset.
        """
        self.name = name

    def execute(self, store: KeyValueStore) -> None:
        """
        Execute the unset command on the key-value store.

        Args:
            store (KeyValueStore): The key-value store on which to execute the command.
        """
        store.unset(self.name)