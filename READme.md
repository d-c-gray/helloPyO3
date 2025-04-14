Hello PyO3
==========

This repo is a template for setting up a development environment for using PyO3, a crate for making python Packages in
Rust (this template was made for Windows, I have not used it in Linux or Mac).

This template includes a setup for 

External dependencies
---------------------
* [vscode](https://code.visualstudio.com/download) for an IDE that supports Rust and Python
* [uv](https://github.com/astral-sh/uv) for python package management

Setting up environment
----------------------
1. Copy this repo into a folder with your `package-name`
2. Update the `name` field in the [Cargo.toml](Cargo.toml) and  [pyroject.toml](pyproject.toml) to match `package-name`
3. Update the module name from `pyo3_example` in [src/lib.rs](src/lib.rs) to match `package-name`
4. Run  [env-setup](env-setup.bat) to generate the python virtual environment and activate it
5. Run [test](test.bat) to compile the rust binary and run the pytests module, if it passes than everything is setup.

CLI Cheat Sheet
---------------








