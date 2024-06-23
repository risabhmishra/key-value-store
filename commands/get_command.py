from typing import Union

from interface.command import Command
from store.key_value_store import KeyValueStore


class GetCommand(Command):
    """
    Command to get a variable from the key-value store.
    """

    def __init__(self, name: str):
        """
        Initialize the GetCommand.

        Args:
            name (str): The name of the variable to get.
        """
        self.name = name

    def execute(self, store: KeyValueStore) -> Union[int, str]:
        """
        Execute the get command on the key-value store.

        Args:
            store (KeyValueStore): The key-value store on which to execute the command.

        Returns:
            Union[int, str]: The value of the variable or "NULL" if not set.
        """
        return store.get(self.name)