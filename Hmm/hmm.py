def print_without_end_line(text: object):
    """
    Prints something with a space instead of new line
    :param text: The input text
    :return: None
    """
    if text is None:
        text = []
    print(text, end=" ")
