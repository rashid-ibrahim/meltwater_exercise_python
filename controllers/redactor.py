import re


def redact(secret_words: str, clear_text: str):
    """

    :param secret_words: Words to be redacted from the text.
    :type secret_words: str
    :param clear_text: Raw plain text before obfuscation.
    :type clear_text: str

    """

    DELIMITERS = '[, .]+'
    secret_words = re.split(DELIMITERS, secret_words)
    # Remove any left over empty strings
    secret_words = list(filter(None, secret_words))
    SUBSTITUTE = 'XXXXXXXX'

    for word in secret_words:
        clear_text = clear_text.replace(word, SUBSTITUTE)

    return clear_text
