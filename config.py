import os
from pathlib import Path 

#=================Base Directory=================#
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR=BASE_DIR / "data"
LOG_DIR=BASE_DIR / "logs"
MEMORY_DIR=DATA_DIR / "memory"
CONTEXT_DIR= DATA_DIR / "context"
MODELS_DIR= DATA_DIR / "models"
CACHE_DIR= DATA_DIR / "cache"

#=================Neural Network Settings========#
DEFAULT_LAYER_SHAPE=[10,16,8,4]
MUTATION_RATE=0.1
MUTATION_RANGE=0.1
LEARNING_RATE=0.01
POPULATION_SIZE=100

#=================Daily Routine Triggers=======#

DAILY_ROUTINE_TRIGGERS = {
    "Checking Metatrader before 9AM",
    "Review your trades after market closes",
    "Check your emails and messages",
    "Open VSCode  for coding sessions",
    "Run backtests  weekly"
}

#=================Time Configurations===============#
CHECK_INTERNAL_SECONDS=60*10
TRADE_REMINDER_HOUR=9
CODING_SESSION_HOUR=18
#============Logging Configurations & debugging=======#

DEBUG_MODE=True
LOG_LEVEL="INFO"

#=================Code Assistant=================#

SUPPORTED_LANGUAGES = ["python","javascript","java","c++","mql5"]
CODE_HISTORY_LIMIT=10000

#=================FILE PATHS===================#
CONTEXT_HISTORY_FILE=CONTEXT_DIR / "context.json"
MEMORY_FILE=MEMORY_DIR / "memories.json"
CODE_SNIPPETS_FILE=DATA_DIR / "code_snippets.json"
DAILY_LOG_FILE=LOG_DIR / "daily_log.json"

for path in [DATA_DIR, LOG_DIR, MEMORY_DIR, CONTEXT_DIR, MODELS_DIR, CACHE_DIR]:
    os.makedirs(path, exist_ok=True)