#!/usr/bin/env python3
"""Advanced type annotated function"""
from typing import TypeVar, Mapping, Any, Union, Optional

T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    if key in dct:
        return dct[key]
    else:
        return default
