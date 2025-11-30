from pathlib import Path

possible_paths = [".venv/Scripts", ".venv/bin"]

if __name__ == "__main__":
    for p in possible_paths:
        if Path(p).exists():
            print((Path(p) / "activate").as_posix())
            break
