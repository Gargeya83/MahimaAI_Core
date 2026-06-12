# main.py
import asyncio
import logging
from core.evolution import EvolutionModule
from core.bus import MessageBus  # Integrated as planned
from core.evolution import EvolutionModule

# 1. Setup Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("MahimaAI")

class MahimaExecutive:
    def __init__(self):
        self.bus = MessageBus()
        self.evo = EvolutionModule()
        self.running = True

    async def start(self):
        logger.info("MahimaAI Core Executive initializing...")
        
        # 2. Inserted the New Update Code here (Runs once at boot)
        update_status = self.evo.check_for_updates()
        logger.info(f"Evolution Status: {update_status}")
        
        # 3. Resume the existing event loop
        while self.running:
            task = await self.bus.subscribe()
            logger.info(f"MahimaAI Processing Task: {task}")
            # Reasoning engine will be called here
            await asyncio.sleep(1)

    def stop(self):
        self.running = False

if __name__ == "__main__":
    executive = MahimaExecutive()
    try:
        asyncio.run(executive.start())
    except KeyboardInterrupt:
        logger.info("Shutdown initiated.")s