__all__ = ["str_to_bool"]


def str_to_bool(s: str, fallback: bool = False) -> bool:
    """
    Return whether the given string means true or false.

    :param s: the string to parse
    :param fallback: the default value to return

    :type s: str
    :type fallback: bool

    :return: the resulting bool.
    :rtype bool:
    """
    if s.lower() in ["f", "false", "n", "no", "0"]:
        return False
    return s.lower() in ["t", "true", "y", "yes", "1"] or fallback
