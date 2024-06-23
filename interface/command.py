from abc import ABC, abstractmethod
from typing import Optional, Union

from store.key_value_store import KeyValueStore


class Command(ABC):
    """
    Abstract base class for all commands.
    """
    @abstractmethod
    def execute(self, store: KeyValueStore) -> Union[None, int, str, Optional[str]]:
        """
        Execute the command.

        Args:
            store (KeyValueStore): The key-value store on which to execute the command.

        Returns:
            Union[None, int, str, Optional[str]]: The result of the command execution, if any.
        """
        pass