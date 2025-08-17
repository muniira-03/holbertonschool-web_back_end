#!/usr/bin/env python3
"""10-update_topics.py: updates the topics of a school document"""

def update_topics(mongo_collection, name, topics):
    """
    Update all topics of a school document based on the name.

    Args:
        mongo_collection: PyMongo collection object
        name (str): the school name to update
        topics (list of str): list of topics to set
    """
    if mongo_collection is None or name is None or topics is None:
        return

    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
