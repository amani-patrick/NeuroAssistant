import time
from core.brain import NeuralNetwork
from core.memory import Memory
from core.evolution import Evolution
from tasks.context_manager import ContextManager
from tasks.daily_helper import DailyHelper
from tasks.code_assistant import CodeAssistant
from core.utils import logging as log
import config

memory=Memory(config.MEMORY_FILE)
context=ContextManager(100,config.CONTEXT_HISTORY_FILE)
evolution=Evolution(
    population_size=config.POPULATION_SIZE,
    mutation_rate=config.MUTATION_RATE,
    mutation_range= config.MUTATION_RANGE
)
dailyhelper=DailyHelper()
codeAssistant=CodeAssistant(memory)

neuralbrain=NeuralNetwork(config.DEFAULT_LAYER_SHAPE)
if memory.exists("brain_weights"):
    neuralbrain.set_weights(memory.get("brain_weights"))
    log("Brain weights loaded from memory")
else:
    log("Initialized new brain")


def main_loop():
    log("Assistant is running ... \n")
    while True:
        current_context=context.get_context()
        dailyhelper.run(current_context)
        codeAssistant.learn_from_recent_files()
        evolution.evaluate_population(...)
        evolution.evolve()
        context.update_context()
        memory.save()
        time.sleep(config.CHECK_INTERNAL_SECONDS)

        

if __name__ == "__main__":
    try:
        main_loop()

    except Exception as e :
        log("Assistant stoped by user.  ")
