#!/usr/bin/python3
"""Defines a Python class-to-JSON function."""
import sys


def class_to_json(obj):
    """Return the dictionary represntation of a simple data structure."""
    return obj.__dict__
