# main.py
import asyncio
import logging
from core.evolution import EvolutionModule
from core.bus import MessageBus  
from core.sentry import SentryModule 
from core.engine import ReasoningEngine # Ensure your engine module is imported

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("MahimaAI")

class MahimaExecutive:
    def __init__(self):
        self.bus = MessageBus()
        self.evo = EvolutionModule()
        self.sentry = SentryModule()
        self.engine = ReasoningEngine() # Initialize the thinking engine
        self.running = True

    async def start(self):
        logger.info("MahimaAI System Online. Core Executive initializing...")
        
        # 1. Boot-time Evolution Check
        update_status = self.evo.check_for_updates()
        logger.info(f"Evolution Status: {update_status}")
        
        # 2. Main Executive Loop
        while self.running:
            # --- PHASE A: Proactive Perimeter Sentry Check ---
            alert = self.sentry.monitor_environment()
            if "detected" in alert.lower():
                logger.warning(f"MahimaAI ALERT: {alert}")
                # Autonomous interception: She pulls context and reasons without waiting
                await self.engine.autonomous_task(alert)
            
            # --- PHASE B: Asynchronous Task Queue Check ---
            # Using asyncio.wait_for prevents the loop from locking up indefinitely
            try:
                task = await asyncio.wait_for(self.bus.subscribe(), timeout=1.0)
                logger.info(f"MahimaAI Processing Inbound Bus Task: {task}")
                # Hand off task payload to the engine here if necessary
            except asyncio.TimeoutError:
                # No tasks on the bus this cycle; moving forward smoothly
                pass
            
            # Throttle the loop heartbeat to preserve system resources
            await asyncio.sleep(5)

    def stop(self):
        self.running = False

if __name__ == "__main__":
    executive = MahimaExecutive()
    try:
        asyncio.run(executive.start())
    except KeyboardInterrupt:
        logger.info("Shutdown initiated.")