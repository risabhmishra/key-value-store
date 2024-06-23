from interface.command import Command
from store.key_value_store import KeyValueStore


class SetCommand(Command):
    """
    Command to set a variable in the key-value store.
    """

    def __init__(self, name: str, value: int):
        """
        Initialize the SetCommand.

        Args:
            name (str): The name of the variable to set.
            value (int): The value to set the variable to.
        """
        self.name = name
        self.value = value

    def execute(self, store: KeyValueStore) -> None:
        """
        Execute the set command on the key-value store.

        Args:
            store (KeyValueStore): The key-value store on which to execute the command.
        """
        store.set(self.name, self.value)