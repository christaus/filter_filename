def strip_filename(filename):
    """Strip illegal characters in Windows 10 filenames.

    Keyword arguments:
    filename -- the original filename
    """
    # French version, may vary according to local...
    allowed_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    "0123456789. ()[]-êéèàçï_"
    filename = filename.strip()
    allowed_filename = ""
    for letter in filename:
        for allowed_letter in allowed_characters:
            if letter == allowed_letter:
                allowed_filename = allowed_filename + letter
                continue
    return allowed_filename
