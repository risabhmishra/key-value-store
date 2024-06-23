# KeyValueStore

KeyValueStore is an in-memory key-value store service similar to Redis, implemented in Python. It supports basic data commands and transactional commands, with thread safety ensured through the use of locks.

## Features

- Set, get, and unset key-value pairs.
- Support for transactions with `BEGIN`, `ROLLBACK`, and `COMMIT` commands.
- Nested transactions support.
- Thread-safe operations.

## Available Commands
- SET name value – Set the variable name to the value value.
- GET name – Print out the value of the variable name, or NULL if that variable is not set.
- UNSET name – Unset the variable name.
- BEGIN – Open a new transaction block. Transactions can be nested.
- ROLLBACK – Undo commands issued in the current transaction, and close it.
- COMMIT – Close all open transactions, permanently applying the changes made in them.

## Example 

`python3 main.py`
```
SET a 10
----- Command Processed -----
GET a 
10
----- Command Processed -----
BEGIN
----- Command Processed -----
SET a 20
----- Command Processed -----
GET a
20
----- Command Processed -----
ROLLBACK
----- Command Processed -----
GET a
10
----- Command Processed -----
COMMIT
NO TRANSACTION
----- Command Processed -----
ROLLBACK
NO TRANSACTION
----- Command Processed -----
END
```

##Running Tests

**To run the tests, use the following command:**

`python3 -m unittest discover -s tests`