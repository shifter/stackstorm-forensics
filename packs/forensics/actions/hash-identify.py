#!/usr/bin/python

from lib.hashtag import identify_hash
from st2actions.runners.pythonrunner import Action

__all__ = [
    'HashIdentifyAction',
]


class HashIdentifyAction(Action):
    def run(self, hash):
        return ", ".join(identify_hash(hash)[:3])
