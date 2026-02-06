BASE62_ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
BASE = len(BASE62_ALPHABET)


def encode_base62(num: int) -> str:
    """
    Convert a positive integer into a Base62-encoded string.

    Used to generate short, URL-safe identifiers from database IDs.
    """
    if num < 0:
        raise ValueError("Number must be non-negative")

    if num == 0:
        return BASE62_ALPHABET[0]

    encoded = []

    while num > 0:
        remainder = num % BASE
        encoded.append(BASE62_ALPHABET[remainder])
        num //= BASE

    return "".join(reversed(encoded))
