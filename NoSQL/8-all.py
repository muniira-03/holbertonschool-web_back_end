#!/usr/bin/env python3
"""8-all.py: lists all documents in a collection"""

def list_all(mongo_collection):
    """Return all documents in a PyMongo collection as a list"""
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())