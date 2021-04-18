import os


class Config:

    # Limit the form submission size to effectively limit the file size. We don't want huge files.
    MAX_CONTENT_LENGTH = 1024 * 1024

    UPLOAD_EXTENSIONS = ['.txt']
    FILES_DIRECTORY = os.path.join('static', 'files')
