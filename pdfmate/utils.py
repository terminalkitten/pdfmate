from collections.abc import Iterable

import six


def is_iterable(arg) -> bool:
    return (
        isinstance(arg, Iterable)
        and not isinstance(arg, six.string_types)  # not string
        and not hasattr(arg, 'read')  # not file
    )
