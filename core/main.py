# main.py
import asyncio
import logging
from core.evolution import EvolutionModule
from core.bus import MessageBus  
from core.sentry import SentryModule # 1. Imported as planned

# Setup Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("MahimaAI")

class MahimaExecutive:
    def __init__(self):
        self.bus = MessageBus()
        self.evo = EvolutionModule()
        self.sentry = SentryModule() # 2. Initialize Sentry alongside other core modules
        self.running = True

    async def start(self):
        logger.info("MahimaAI Core Executive initializing...")
        
        # Evolution check runs first
        update_status = self.evo.check_for_updates()
        logger.info(f"Evolution Status: {update_status}")
        
        # 3. Integrated Sentry Check: Monitor environment variables or health anomalies at boot
        status = self.sentry.monitor_environment()
        if "detected" in status.lower(): # .lower() handles variation in case safely
            logger.info(f"Proactive Alert: {status}")
        else:
            logger.info(f"Sentry Diagnostics: {status}")
        
        # TEST EVENT: Let's inject a task into the system bus natively
        await self.bus.publish("hardware_check", {"requester": "boot_sequence"})
        
        # Core Event Loop
        while self.running:
            task = await self.bus.subscribe()
            logger.info(f"MahimaAI Processing Task: {task}")
            
            # Reasoning engine/Skills dynamic lookup will go here
            await asyncio.sleep(1)

    def stop(self):
        self.running = False

if __name__ == "__main__":
    executive = MahimaExecutive()
    try:
        asyncio.run(executive.start())
    except KeyboardInterrupt:
        logger.info("Shutdown initiated.")