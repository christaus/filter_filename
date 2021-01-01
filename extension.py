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
