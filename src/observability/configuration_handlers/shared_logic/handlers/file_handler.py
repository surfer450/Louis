class FileHandler:
    """
    A utility class for handling file operations, including reading from and writing to files.

    This class provides static methods to read the content of a file and write content to a file.
    It is designed to simplify basic file handling operations and handle common file I/O tasks.
    """

    @staticmethod
    def read_file(file_path: str) -> str:
        """
        Reads the content of a file and returns it as a string.

        Args:
            file_path (str): The path to the file to be read.

        Returns:
            str: The content of the file.
        """
        with open(file_path, "r") as file:
            return file.read()

    @staticmethod
    def write_file(file_path: str, content: str) -> None:
        """
        Writes the provided content to a file.

        Args:
            file_path (str): The path to the file where content will be written.
            content (str): The content to write into the file.
        """
        with open(file_path, "w") as file:
            file.write(content)
