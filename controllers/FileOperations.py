import os
import random
from string import ascii_letters

from flask import current_app


class FileOperations:
    """
    Handles saving of file contents and as a way to hold the file name variable.
    With out the file name variable then we would need to implement some sort of session handling or a database to store
    either user information, the files being encrypted, a hash value for each operation, or some combination of those.
    """
    def __init__(self):
        self._out_file = ''.join(random.choice(ascii_letters) for _ in range(15))
        config = current_app.config
        self._file_path = os.path.join(current_app.root_path, config['FILES_DIRECTORY'])

    def save_redacted(self, redacted_text: str):
        """
        :param redacted_text: redacted text to save in a file.
        :type redacted_text: str
        :return: None
        """
        with open(os.path.join(self._file_path, self._out_file), 'w+') as f:
            f.write(redacted_text)

    @property
    def out_file(self):
        return self._out_file

    @out_file.setter
    def out_file(self, value):
        self._out_file = value


