Hello PyO3
==========

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
1. Copy this repo into a folder with your `package-name`
2. Update the `name` field in the [Cargo.toml](Cargo.toml) and  [pyroject.toml](pyproject.toml) to match `package-name`
3. Update the module name from `pyo3_example` in [src/lib.rs](src/lib.rs) to match `package-name`
4. Run  [startup](startup.bat) to generate the python virtual environment and activate it
5. Run [test](test.bat) to compile the rust binary and run the pytests module, if it passes than everything is setup.
6. For vscode select the virtual environment as your python interpreter `ctrl+shift+p` than `Python: Select Interpreter`

included scripts
----------------
* [startup](startup.bat) syncs your virtual environment and acativates it
* [test](test.bat) 









