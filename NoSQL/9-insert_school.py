#!/usr/bin/env python3
"""9-insert_school.py: inserts a new document in a collection"""

def insert_school(mongo_collection, **kwargs):
    """Insert a document into a PyMongo collection using kwargs"""
    if mongo_collection is None or not kwargs:
        return None
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id