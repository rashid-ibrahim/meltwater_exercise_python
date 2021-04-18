import os

from flask import current_app


class FileOperations:
    def __init__(self):
        self._out_file = 'redacted.txt'
        config = current_app.config
        self._file_path = os.path.join(current_app.root_path, config['FILES_DIRECTORY'])

    def save_redacted(self, redacted_text: str):
        with open(os.path.join(self._file_path, self._out_file), 'w+') as f:
            f.write(redacted_text)

    @property
    def out_file(self):
        return self._out_file

    @out_file.setter
    def out_file(self, value):
        self._out_file = value


