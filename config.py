import os


class Config:
    """
    App wide configuration variables and loading of any keys should be done here.
    """

    # Limit the form submission size to effectively limit the file size. We don't want huge files.
    MAX_CONTENT_LENGTH = 1024 * 1024

    # Limit uploads to only txt files.
    UPLOAD_EXTENSIONS = ['.txt']

    # Global for directory location so that files can be moved as needed.
    FILES_DIRECTORY = os.path.join('static', 'files')
