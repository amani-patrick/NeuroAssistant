import time
from collections  import deque ,defaultdict
class ContextManager:
    def __init__(self,memory_size=1000,time_decay=True):
        self.context_memory=deque(maxlen=memory_size)
        self.tagged_context=defaultdict(list)
        self.time_decay = time_decay

        def push(self ,content ,tags=None):
            timestamp = time.time()
            entry={
                "timestamp": timestamp,
                "content": content,
                "tags": tags or []
            }
            self.context_memory.append(entry)
            for tag in entry["tags"]:
                self.tagged_context[tag].append(entry)
        def recal_recent(self,n=10):
            return list(self.context_memory)[-n:]
        def recall_by_tag(self,tag,n=10):
            return self.tagged_context[tag][-n:] if tag in self.tagged_context else []
        def clear_tag(self,tag):
            if tag in self.tagged_context:
                del self.tagged_context[tag]
        def decay_context(self):
            """Compress  old memories in case they are old"""
            if not self.time_decay:
                return
            current_time = time.time()
            new_context=deque(maxlen=self.context_memory.maxlen)
            for entry in self.context_memory:
                age=current_time-entry["timestamp"]
                if age < 7200:
                    new_context.append(entry)
            self.context_memory = new_context

        def summarize_context(self,tag=None):
            items =self.tagged_context[tag] if tag else self.context_memory
            return "\n ".join([e["content"] for e in items[-5:]])