# Filename filters for Python

import os


def extension(filename):
    """Return the extension of a filename

    Keyword arguments:
    filename -- the original filename
    """
    # Check if a .something exist in the actual filename
    if filename.rfind(".") == -1:
        return ""
    extension = filename[filename.rfind("."):]
    return extension


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


def strip_filename(filename):
    """Strip illegal characters in Windows 10 filenames.

    Keyword arguments:
    filename -- the original filename
    """
    # French version, may vary according to local...
    allowed_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789. ()[]-éèàçï_"
    filename = filename.strip()
    allowed_filename = ""
    for letter in filename:
        for allowed_letter in allowed_characters:
            if letter == allowed_letter:
                allowed_filename = allowed_filename + letter
                continue
    return allowed_filename


def filter_filename(filename):
    """Suppress illegal characters in Windows 10 filenames.
    Limits length of filename in Windows 10 filenames.
    Return an allowed filename.

    !!! Be careful to extract the directory path before !!!

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

    # Else, we keep the extension if the filename length is above 250 characters long.
    if len(filename) > 250:
        return filename[:250 - len(extension(filename))] + extension(filename)
    return filename
