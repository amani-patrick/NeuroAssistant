import datetime

class DailyHelper:
    def __init__(self):
        self.journal_entries = []
        self.todo_list = []
        self.reflections = []

    def add_todo(self, task):
        self.todo_list.append({
            "task": task,
            "completed": False,
            "created_at": datetime.datetime.now()
        })

    def complete_todo(self, index):
        if 0 <= index < len(self.todo_list):
            self.todo_list[index]["completed"] = True

    def remove_todo(self, index):
        if 0 <= index < len(self.todo_list):
            self.todo_list.pop(index)

    def add_journal_entry(self, content):
        self.journal_entries.append({
            "content": content,
            "timestamp": datetime.datetime.now()
        })

    def add_reflection(self, thought):
        self.reflections.append({
            "thought": thought,
            "timestamp": datetime.datetime.now()
        })

    def get_daily_summary(self):
        today = datetime.date.today()
        todos_today = [t for t in self.todo_list if t["created_at"].date() == today]
        journals_today = [j for j in self.journal_entries if j["timestamp"].date() == today]
        reflections_today = [r for r in self.reflections if r["timestamp"].date() == today]

        return {
            "todos": todos_today,
            "journals": journals_today,
            "reflections": reflections_today
        }

    def reset_daily(self):
        self.todo_list.clear()
        self.journal_entries.clear()
        self.reflections.clear()
