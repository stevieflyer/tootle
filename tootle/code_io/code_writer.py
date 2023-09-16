import pathlib


class CodeWriter:
    """
    A utility class for writing code to files.

    Now, `CodeWriter` only supports Python code.
    """
    @staticmethod
    def ensure_init_py(directory: pathlib.Path):
        """
        Recursively ensure that each directory level has an __init__.py file.
        """
        if directory.exists() and not directory.is_dir():
            raise ValueError(f"{directory} exists but is not a directory!")

        if not directory.exists():
            directory.mkdir(parents=True, exist_ok=True)

        init_file = directory / '__init__.py'
        if not init_file.exists():
            init_file.touch()

        # Recurse to parent until reaching the root
        parent = directory.parent
        if parent != directory:  # Stop condition for reaching root
            CodeWriter.ensure_init_py(parent)

    @staticmethod
    def write_code(file_path: pathlib.Path, code: str):
        """
        Write code to the given file_path, ensuring directories and __init__.py files exist.
        """
        CodeWriter.ensure_init_py(file_path.parent)

        with open(file_path, "a") as f:
            f.write(code)


__all__ = ['CodeWriter']
