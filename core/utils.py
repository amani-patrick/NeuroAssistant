import os
import json
import random
import datetime
import logging
from pathlib import Path

# Logging setup
logging.basicConfig(
    format='[%(levelname)s] %(asctime)s: %(message)s',
    level=logging.INFO
)

def timestamp():
    return datetime.datetime.now().isoformat()

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)

def load_json(path, default=None):
    if os.path.exists(path):
        with open(path, 'r') as f:
            return json.load(f)
    return default if default is not None else {}

def save_json(path, data):
    ensure_dir(os.path.dirname(path))
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)

def get_random_id(length=8):
    return ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=length))

def readable_time(seconds):
    return str(datetime.timedelta(seconds=round(seconds)))

class Timer:
    def __init__(self):
        self.start_time = None

    def start(self):
        self.start_time = datetime.datetime.now()

    def stop(self):
        if self.start_time is None:
            return 0
        delta = datetime.datetime.now() - self.start_time
        return delta.total_seconds()

class SimpleCache:
    def __init__(self, max_items=100):
        self.cache = {}
        self.max_items = max_items

    def set(self, key, value):
        if len(self.cache) >= self.max_items:
            self.cache.pop(next(iter(self.cache)))
        self.cache[key] = value

    def get(self, key, default=None):
        return self.cache.get(key, default)

    def has(self, key):
        return key in self.cache

    def clear(self):
        self.cache = {}

class TextCleaner:
    @staticmethod
    def clean(text):
        return ' '.join(text.strip().lower().split())

    @staticmethod
    def tokenize(text):
        return text.lower().split()
