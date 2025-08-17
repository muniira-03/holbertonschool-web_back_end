#!/usr/bin/env python3
"""11-schools_by_topic.py: list schools having a specific topic"""

def schools_by_topic(mongo_collection, topic):
    """
    Return the list of schools having a specific topic.

    Args:
        mongo_collection: PyMongo collection object
        topic (str): topic to search for

    Returns:
        list: list of school documents containing the topic
    """
    if mongo_collection is None or topic is None:
        return []

    return list(mongo_collection.find({"topics": topic}))
