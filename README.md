## Development

All commands are run at root directory.

### Local Development

1. Set up environment (code below works with a bash/zsh shell on a POSIX platform). See [python docs](https://docs.python.org/3/library/venv.html) for information how to activate the environment with other shells and platforms.

```sh
source ./bin/activate
```

2. Run the program

```sh
python3 main.py
```

### Running Tests

1. Run tests

```sh
python3 -m unittest singly_linked_list_tests.py 
```