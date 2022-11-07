Poetry is a tool for dependency management and packaging in Python. It allows you to declare the libraries your project depends on and it will manage (install/update) them for you.

1. Install Poetry
--------------------------
pip install --user poetry
--------------------------

2. Create a new project
---------------------
poetry new my-project
---------------------

This will create a my-project directory:

 my-project
 ├── pyproject.toml
 ├── README.rst
 ├── poetry_demo
 │   └── __init__.py
 └── tests
     ├── __init__.py
     └── test_poetry_demo.py

The pyproject.toml file will orchestrate your project and its dependencies:

 [tool.poetry]
 name = "my-project"
 version = "0.1.0"
 description = ""
 authors = ["your name <your@mail.com>"]

 [tool.poetry.dependencies]
 python = "*"

 [tool.poetry.dev-dependencies]
 pytest = "^3.4"


3. Packages

To add dependencies to your project, you can specify them in the tool.poetry.dependencies section:
--------------------------
[tool.poetry.dependencies]
pendulum = "^1.4"
--------------------------


Also, instead of modifying the pyproject.toml file by hand, you can use the add command and it will automatically find a suitable version constraint.
---------------------
$ poetry add pendulum
---------------------
To install the dependencies listed in the pyproject.toml:

--------------
poetry install
--------------

To remove dependencies:
----------------------
poetry remove pendulum
----------------------
1. Install Poetry
--------------------------
pip install --user poetry
--------------------------

2. Create a new project
---------------------
poetry new my-project
---------------------

This will create a my-project directory:Poetry is a tool for dependency management and packaging in Python. It allows you to declare the libraries your project depends on and it will manage (install/update) them for you.

1. Install Poetry
--------------------------
pip install --user poetry
--------------------------

2. Create a new project
---------------------
poetry new my-project
---------------------

This will create a my-project directory:

 my-project
 ├── pyproject.toml
 ├── README.rst
 ├── poetry_demo
 │   └── __init__.py
 └── tests
     ├── __init__.py
     └── test_poetry_demo.py

The pyproject.toml file will orchestrate your project and its dependencies:

 [tool.poetry]
 name = "my-project"
 version = "0.1.0"
 description = ""
 authors = ["your name <your@mail.com>"]

 [tool.poetry.dependencies]
 python = "*"

 [tool.poetry.dev-dependencies]
 pytest = "^3.4"


3. Packages

To add dependencies to your project, you can specify them in the tool.poetry.dependencies section:
--------------------------
[tool.poetry.dependencies]
pendulum = "^1.4"
--------------------------


Also, instead of modifying the pyproject.toml file by hand, you can use the add command and it will automatically find a suitable version constraint.
---------------------
$ poetry add pendulum
---------------------
To install the dependencies listed in the pyproject.toml:

--------------
poetry install
--------------

To remove dependencies:Poetry is a tool for dependency management and packaging in Python. It allows you to declare the libraries your project depends on and it will manage (install/update) them for you.

1. Install Poetry
--------------------------
pip install --user poetry
--------------------------

2. Create a new project
---------------------
poetry new my-project
---------------------

This will create a my-project directory:

 my-project
 ├── pyproject.toml
 ├── README.rst
 ├── poetry_demo
 │   └── __init__.py
 └── tests
     ├── __init__.py
     └── test_poetry_demo.py

The pyproject.toml file will orchestrate your project and its dependencies:

 [tool.poetry]
 name = "my-project"
 version = "0.1.0"
 description = ""
 authors = ["your name <your@mail.com>"]

 [tool.poetry.dependencies]
 python = "*"

 [tool.poetry.dev-dependencies]
 pytest = "^3.4"


3. Packages

To add dependencies to your project, you can specify them in the tool.poetry.dependencies section:
--------------------------
[tool.poetry.dependencies]
pendulum = "^1.4"
--------------------------


Also, instead of modifying the pyproject.toml file by hand, you can use the add command and it will automatically find a suitable version constraint.
---------------------
$ poetry add pendulum
---------------------
To install the dependencies listed in the pyproject.toml:

--------------
poetry install
--------------

To remove dependencies:
----------------------
poetry remove pendulum
----------------------
----------------------
poetry remove pendulum
----------------------

 my-project
 ├── pyproject.toml
 ├── README.rst
 ├── poetry_demo
 │   └── __init__.pyPoetry is a tool for dependency management and packaging in Python. It allows you to declare the libraries your project depends on and it will manage (install/update) them for you.

1. Install Poetry
--------------------------
pip install --user poetry
--------------------------

2. Create a new project
---------------------
poetry new my-project
---------------------

This will create a my-project directory:

 my-project
 ├── pyproject.toml
 ├── README.rst
 ├── poetry_demo
 │   └── __init__.py
 └── tests
     ├── __init__.py
     └── test_poetry_demo.py

The pyproject.toml file will orchestrate your project and its dependencies:

 [tool.poetry]
 name = "my-project"
 version = "0.1.0"
 description = ""
 authors = ["your name <your@mail.com>"]

 [tool.poetry.dependencies]
 python = "*"

 [tool.poetry.dev-dependencies]
 pytest = "^3.4"


3. Packages

To add dependencies to your project, you can specify them in the tool.poetry.dependencies section:
--------------------------
[tool.poetry.dependencies]
pendulum = "^1.4"
--------------------------


Also, instead of modifying the pyproject.toml file by hand, you can use the add command and it will automatically find a suitable version constraint.
---------------------
$ poetry add pendulum
---------------------
To install the dependencies listed in the pyproject.toml:

--------------
poetry install
--------------

To remove dependencies:
----------------------
poetry remove pendulum
----------------------
 └── tests
     ├── __init__.py
     └── test_poetry_demo.py

The pyproject.toml file will orchestrate your project and its dependencies:

 [tool.poetry]
 name = "my-project"
 version = "0.1.0"
 description = ""
 authors = ["your name <your@mail.com>"]

 [tool.poetry.dependencies]
 python = "*"

 [tool.poetry.dev-dependencies]
 pytest = "^3.4"


3. Packages

To add dependencies to your project, you can specify them in the tool.poetry.dependencies section:
--------------------------
[tool.poetry.dependencies]
pendulum = "^1.4"
--------------------------


Also, instead of modifying the pyproject.toml file by hand, you can use the add command and it will automatically find a suitable version constraint.
---------------------
$ poetry add pendulum
---------------------
To install the dependencies listed in the pyproject.toml:

--------------
poetry install
--------------

To remove dependencies:
----------------------
poetry remove pendulum
----------------------
