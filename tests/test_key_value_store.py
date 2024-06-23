import unittest

from commands.begin_command import BeginCommand
from commands.commit_command import CommitCommand
from commands.get_command import GetCommand
from commands.rollback_command import RollbackCommand
from commands.set_command import SetCommand
from commands.unset_command import UnsetCommand
from store.key_value_store import KeyValueStore


class TestKeyValueStore(unittest.TestCase):
    """
    Unit tests for the KeyValueStore and command classes.
    """

    def setUp(self):
        """
        Set up the test environment by initializing a KeyValueStore instance.
        """
        self.kv_store = KeyValueStore()

    def test_set_get(self):
        """
        Test setting a value and then getting it.
        """
        set_command = SetCommand("a", 10)
        get_command = GetCommand("a")
        self.kv_store.execute_command(set_command)
        result = self.kv_store.execute_command(get_command)
        self.assertEqual(result, 10)

    def test_unset(self):
        """
        Test unsetting a value and then getting it.
        """
        set_command = SetCommand("a", 10)
        unset_command = UnsetCommand("a")
        get_command = GetCommand("a")
        self.kv_store.execute_command(set_command)
        self.kv_store.execute_command(unset_command)
        result = self.kv_store.execute_command(get_command)
        self.assertEqual(result, "NULL")

    def test_transaction_commit(self):
        """
        Test committing a transaction.
        """
        begin_command = BeginCommand()
        set_command = SetCommand("a", 10)
        commit_command = CommitCommand()
        get_command = GetCommand("a")

        self.kv_store.execute_command(begin_command)
        self.kv_store.execute_command(set_command)
        self.kv_store.execute_command(commit_command)
        result = self.kv_store.execute_command(get_command)
        self.assertEqual(result, 10)

    def test_transaction_rollback(self):
        """
        Test rolling back a transaction.
        """
        begin_command = BeginCommand()
        set_command1 = SetCommand("a", 10)
        set_command2 = SetCommand("a", 20)
        rollback_command = RollbackCommand()
        get_command = GetCommand("a")

        self.kv_store.execute_command(begin_command)
        self.kv_store.execute_command(set_command1)
        self.kv_store.execute_command(begin_command)
        self.kv_store.execute_command(set_command2)
        self.kv_store.execute_command(rollback_command)
        result = self.kv_store.execute_command(get_command)
        self.assertEqual(result, 10)
        self.kv_store.execute_command(rollback_command)
        result = self.kv_store.execute_command(get_command)
        self.assertEqual(result, "NULL")

    def test_nested_transactions_commit(self):
        """
        Test committing nested transactions.
        """
        begin_command = BeginCommand()
        set_command1 = SetCommand("a", 10)
        set_command2 = SetCommand("a", 20)
        commit_command = CommitCommand()
        get_command = GetCommand("a")

        self.kv_store.execute_command(begin_command)
        self.kv_store.execute_command(set_command1)
        self.kv_store.execute_command(begin_command)
        self.kv_store.execute_command(set_command2)
        self.kv_store.execute_command(commit_command)
        result = self.kv_store.execute_command(get_command)
        self.assertEqual(result, 20)

    def test_no_transaction_rollback(self):
        """
        Test rolling back when no transaction is active.
        """
        rollback_command = RollbackCommand()
        result = self.kv_store.execute_command(rollback_command)
        self.assertEqual(result, "NO TRANSACTION")

    def test_no_transaction_commit(self):
        """
        Test committing when no transaction is active.
        """
        commit_command = CommitCommand()
        result = self.kv_store.execute_command(commit_command)
        self.assertEqual(result, "NO TRANSACTION")


if __name__ == '__main__':
    unittest.main()
