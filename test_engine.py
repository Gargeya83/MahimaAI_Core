import asyncio
from core.engine import ReasoningEngine
from core.skills_loader import SkillsLoader

async def run_test():
    engine = ReasoningEngine()
    result = await engine.process_task("Setup GPS hardware module for motorbike navigation.")
    print(f"MahimaAI Thought Process: {result}")

if __name__ == "__main__":
    asyncio.run(run_test())
    
    loader = SkillsLoader()
print(loader.execute_skill("hardware_check"))