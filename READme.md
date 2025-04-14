HelloPyO3
=========

This repo is a template for setting up a development environment for using PyO3, a crate for making python Packages in
Rust (this template was made for Windows, I have not used it in Linux or Mac).

external dependencies
---------------------
You will have to install these yourself
* [vscode](https://code.visualstudio.com/download) for an IDE that supports Rust and Python
* [uv](https://github.com/astral-sh/uv) for python package management
* [rust/cargo](https://www.rust-lang.org/tools/install) for running rust code

setting it up
-------------
1. Copy this repo into a folder with your `project-name`.
2. update the `project-name` and `lib.nam` field in the [Cargo.toml](Cargo.toml) with your `project-name`.
3. Upate `project.name` in [pyroject.toml](pyproject.toml) to match `project-name`.
4. Update the module name from `pyo3_example` in [src/lib.rs](src/lib.rs) to match `project-name`.
5. Update the import path in [pytests/test_env.py](pytests/test_env.py) to match `project-name`.
6. Update the `project` at the top of [docs/source/conf.py](docs/source/conf.py).
7. Run  [startup](startup.bat) to generate the python virtual environment and activate it.
8. Run [test](test.bat) to compile the rust binary and run the pytests module, if it passes than the environment is setup.
9. Run [document](document.bat) to build documentation.
10. For vscode select the virtual environment as your python interpreter `ctrl+shift+p` than `Python: Select Interpreter`.

Scripts and CLI cheetsheet
--------------------------
Everything here is run from the root directory
* `startup` syncs your virtual environment and activates it.
* `test` compiles rust binaries and runs pytests.
* `make clean` cleans up the docs/build directory, useful to run before building documentation after major changes.
* `make html` to build documentation.









