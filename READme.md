HelloPyO3
=========

This repo is a template for setting up a development environment for using PyO3
This includes:
* A basic module layout for ``lib.rs`` that builds a python class
* A make file that installs and tests code
* A github workflow file for executing tests.

External Dependencies
---------------------
* [uv](https://github.com/astral-sh/uv) for python package management and development
* [rust/cargo](https://www.rust-lang.org/tools/install) for rust development
* [make](https://gnuwin32.sourceforge.net/packages/make.htm)

Setting it up
-------------
After cloning the template initialize it with:
```
make init MODULE_NAME=my_module
```

After that, run ``make`` to execute installation and tests.
```
make
```

Use the ``clean`` and ``build`` commands to clear out ephemeral
directories and make build the packages.
```
make clean
make build
```


To Do
-----
* Incorporate an example of versioned documentation.




