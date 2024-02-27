#!/usr/bin/python3
"""Defines the engine package."""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
