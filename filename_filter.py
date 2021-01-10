# Filename filters for Python

from extension import extension
from remove_directory_path import remove_directory_path
from strip_filename import strip_filename


def filter_filename(filename):
    """Suppress illegal characters in Windows 10 filenames.
    Limits length of filename in Windows 10 filenames.
    Return an allowed filename.

    Keyword arguments:
    filename -- the original filename
    """
    # Remove os path
    filename = remove_directory_path(filename)

    # Remove illegal characters
    filename = strip_filename(filename)

    # If the extension length is above 249 characters long, we truncate it.
    if len(extension(filename)) > 249:
        return filename[:250]

    # Else, we keep the extension if the filename length is above
    # 250 characters long.
    if len(filename) > 250:
        return filename[:250 - len(extension(filename))] + extension(filename)
    return filename
