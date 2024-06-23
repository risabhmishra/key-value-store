from commands.begin_command import BeginCommand
from commands.commit_command import CommitCommand
from commands.get_command import GetCommand
from commands.rollback_command import RollbackCommand
from commands.set_command import SetCommand
from commands.unset_command import UnsetCommand
from store.key_value_store import KeyValueStore


def main():
    """
    Run the CLI application for the key-value store.
    """
    kv_store = KeyValueStore()
    while True:
        try:
            user_input = input().strip()
            if user_input == "":
                continue

            parts = user_input.split()
            command_name = parts[0].upper()

            if command_name == "SET":
                if len(parts) != 3:
                    print("ERROR: SET command requires 2 arguments")
                    continue
                command = SetCommand(parts[1], int(parts[2]))
                kv_store.execute_command(command)
                print("----- Command Processed -----")

            elif command_name == "GET":
                if len(parts) != 2:
                    print("ERROR: GET command requires 1 argument")
                    continue
                command = GetCommand(parts[1])
                result = kv_store.execute_command(command)
                print(result)
                print("----- Command Processed -----")

            elif command_name == "UNSET":
                if len(parts) != 2:
                    print("ERROR: UNSET command requires 1 argument")
                    continue
                command = UnsetCommand(parts[1])
                kv_store.execute_command(command)
                print("----- Command Processed -----")

            elif command_name == "BEGIN":
                command = BeginCommand()
                kv_store.execute_command(command)
                print("----- Command Processed -----")

            elif command_name == "ROLLBACK":
                command = RollbackCommand()
                result = kv_store.execute_command(command)
                if result == "NO TRANSACTION":
                    print(result)
                print("----- Command Processed -----")

            elif command_name == "COMMIT":
                command = CommitCommand()
                result = kv_store.execute_command(command)
                if result == "NO TRANSACTION":
                    print(result)
                print("----- Command Processed -----")

            elif command_name == "END":
                break

            else:
                print("ERROR: Unknown command")

        except EOFError:
            break


if __name__ == "__main__":
    main()
