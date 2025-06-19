#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@summary: A module for a high level console interface.

@author: Frank Brehm
@contact: frank@brehm-online.com
@copyright: © 2025 by Frank Brehm, Berlin
"""
from __future__ import absolute_import

# Standard library modules
import sys
from dataclasses import dataclass, field
from typing import (
    TYPE_CHECKING,
)

# Own modules
from ._null_file import NULL_FILE

__version__ = '0.1.0'


# =============================================================================
class NoChange:
    """A class making no changes."""

    pass


NO_CHANGE = NoChange()

# =============================================================================
try:
    _STDIN_FILENO = sys.__stdin__.fileno()  # type: ignore[union-attr]
except Exception:
    _STDIN_FILENO = 0

try:
    _STDOUT_FILENO = sys.__stdout__.fileno()  # type: ignore[union-attr]
except Exception:
    _STDOUT_FILENO = 1

try:
    _STDERR_FILENO = sys.__stderr__.fileno()  # type: ignore[union-attr]
except Exception:
    _STDERR_FILENO = 2

_STD_STREAMS = (_STDIN_FILENO, _STDOUT_FILENO, _STDERR_FILENO)
_STD_STREAMS_OUTPUT = (_STDOUT_FILENO, _STDERR_FILENO)


# vim: ts=4 et list
