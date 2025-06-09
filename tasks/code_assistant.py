import os,re
from collections import defaultdict
from core.brain import NeuralNetwork

class CodeAssistant:
    def __init__(self,brain: NeuralNetwork,code_dir:"workspace",language=None):
        self.brain=brain
        self.code_dir=code_dir
        self.language=language or ["python", "javascript", "java", "c++", "c#", "ruby", "go", "rust","mql5", "php", "swift","kotlin", "typescript", "html", "css","sql", "bash", "perl", "r", "matlab", "lua"]
        self.language_patterns ={
            "python": r"\.py$",
            "javascript": r"\.js$",
            "java": r"\.java$ |\.jsp$",
            "c++": r"\.cpp$|\.h$",
            "c#": r"\.cs$",
            "ruby": r"\.rb$",
            "go": r"\.go$",
            "rust": r"\.rs$",
            "mql5": r"\.mq5$ |\.mqh$",
            "php": r"\.php$",
            "swift": r"\.swift$",
            "kotlin": r"\.kt$|\.kts$",
            "typescript": r"\.ts$|\.tsx$",
            "html": r"\.html?$|\.htm$",
            "css": r"\.css$ |\.scss$|\.less$", 
            "sql": r"\.sql$",
            "bash": r"\.sh$|\.bash$",
            "perl": r"\.pl$|\.pm$",
            "r": r"\.r$|\.R$",
            "matlab": r"\.(m|matlab)$",
            "lua": r"\.lua$"
        }
        self.knowledge_base = defaultdict(list)
        def scan_workspace(self):
            for root, _, files in os.walk(self.code_dir):
                for file in files:
                    for lang, pattern in self.language_patterns.items():
                        if re.search(pattern, file):
                            file_path = os.path.join(root, file)
                            self._learn_from_file(file_path, lang)
        def _learn_from_file(self, file_path, lang):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    patterns = self.extract_patterns(content)
                    self.knowledge_base[lang].extend(patterns)
                    self.NeuralNetwork.learn(f"code::{language}", patterns)
            except Exception as e:
                print(f"[CodeAssistant] Failed to process {file_path}: {e}")
        def extract_patterns(self, content):
            line =[line.strip() for line in content.split("\n") if line.strip()]
            return content[:100]
        def suggest_completion(self,language,context):
            memory= self.NeuralNetwork.get_memory(f"code::{language}")
            suggestions=[line for line in memory if context in line]
            return suggestions[:5]
        def most_used_language(self):
            return sorted (self.knowledge_base.items(), key=lambda x: len(x[1]), reverse=True)[0][0] if self.knowledge_base else None
