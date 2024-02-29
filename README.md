<p align="center">
<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQJWZ8OBsdHkGHMhS5j0rRravqyOooa6Kzbqw&usqp=CAU" alt="thumbnail">
</p>


# holbertonschool-AirBnB_clone

The console will be the backend to the larger Airbnb clone projcet. In this project we have built a base data model which has the ability to save objects in memory via a JSON file.

## Table of Contents

- [Dependencies](#dependencies)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Bugs](#bugs)
- [Authors](#authors)

## Dependencies

```bash
Ubuntu 20.04 LTS
python3 (version 3.8.5)
```

## Getting Started

To start using the AirBnB Clone, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/tingru0515/holbertonschool-AirBnB_clone
```

2. Navigate to the project directory:

```bash
cd holbertonschool-AirBnB_clone
```

## Usage
The project provides a command interpreter for interacting with the data model. You can use it in interactive or non-interactive mode.

### Interactive Mode

To start the command interpreter in interactive mode, run one of the following commands:

```bash
./comsole.py
```

### non-interactive mode

To start the command interpreter in non interactive mode, run one of the following commands:

```bash
$ echo "<command>" | ./console.py
```

You can use the following commands:

| Command   | Description                                        |
| --------- | -------------------------------------------------- |
| `create`  | Creates a new instance of a class                  |
| `show`    | Prints the instance with the class name and ID     |
| `destroy` | Deletes an instance based on the class name and ID |
| `all`     | Prints all instances                               |
| `update`  | Updates an instance with an attribute              |
| `help`    | Displays a list of available commands              |
| `quit`    | Exits the command interpreter                      |

### Example

to create user

```
$ ./console.py
(hbnb) create User
```

to show all objects

```
$ ./console.py
(hbnb) all
```

## Bugs

Report bugs on the [GitHub Issues](https://github.com/tingru0515/holbertonschool-AirBnB_clone/issues) page.

## Authors

[Tingru Liu](https://github.com/tingru0515).<br>
[Nobuhiro Funahashi](https://github.com/Goaty-yagi).
