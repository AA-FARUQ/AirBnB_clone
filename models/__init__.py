#!/usr/bin/python3
"""
__init__ dunder method for the models directory
"""
from models.engine.file_storage import FileStorage

# Initialize FileStorage instance
storage_instance = FileStorage()

# Reload data from storage
storage_instance.reload()
