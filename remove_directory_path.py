import os


def remove_directory_path(filename):
    """Remove the directory path from a path
    Return the filename

    Keyword arguments:
    filename -- the original filename / path
    """
    # Check the last os separator in the actual filename
    if filename.rfind(os.sep) == -1:
        return filename
    filename = filename[filename.rfind(os.sep):]
    return filename
