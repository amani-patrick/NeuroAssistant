import json 
import os
from datetime import datetime
class Memory:
    def __init__(self, filePath="data/assistant_memory.json"):
        self.filePath = filePath
        self.data={
            "tasks": [],
            "conversations": [],
            "reminders": [],
            "notes": [],
            "preferences": {},
            "activity_log": []
        }
        self.load()
    def load(self):
        try:
            if os.path.exists(self.filePath):
                with open(self.filePath, "r") as f:
                    self.data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            print(f"[Memory] Failed to load memory from {self.filePath}. Starting with empty memory.")
    def save(self):
        os.makedirs(os.path.dirname(self.filePath), exist_ok=True)
        with open(self.filePath, "w") as f:
            json.dump(self.data, f, default=str, indent=4)
    def log_task(self,task):
        self.data["tasks"].append({
            "task": task,
            "timestamp": datetime.now().isoformat()
        })
        self.save()
    def log_conversation(self, conversation):
        self.data["conversations"].append({
            "conversation": conversation,
            "timestamp": datetime.now().isoformat()
        })
    def log_reminder(self, reminder):
        self.data["reminders"].append({
            "reminder": reminder,
            "timestamp": datetime.now().isoformat()
        })
        self.save() 
    def log_note(self, note):
        self.data["notes"].append({
            "note": note,
            "timestamp": datetime.now().isoformat()
        })
        self.save()
    def set_preference(self, key, value):
        self.data["preferences"][key] = value
        self.save()
    def log_snippet(self,code,language):
        self.data["activity_log"].append({
            "code": code,
            "language": language,
            "timestamp": datetime.now().isoformat()
        })
        self.save()
    def get_preferences(self):
        return self.data["preferences"]
    def get_tasks(self):
        return self.data["tasks"]
    def add_reminder(self, reminder):
        self.data["reminders"].append({
            "reminder": reminder,
            "timestamp": datetime.now().isoformat()
        })
        self.save()
    def get_reminders(self):
        return self.data["reminders"]
    def add_conversation(self, conversation):
        self.data["conversations"].append({
            "conversation": conversation,
            "timestamp": datetime.now().isoformat()
        })
        self.save()
    def get_conversations(self):
        return self.data["conversations"]
    def add_note(self, note):
        self.data["notes"].append({
            "note": note,
            "timestamp": datetime.now().isoformat()
        })
        self.save()
    def get_notes(self):
        return self.data["notes"]
    def get_activity_log(self):
        return self.data["activity_log"]