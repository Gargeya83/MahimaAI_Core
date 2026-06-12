import asyncio
from core.engine import ReasoningEngine
from core.skills_loader import SkillsLoader

async def run_test():
    # 1. Start the cognitive "Thinking" process
    engine = ReasoningEngine()
    result = await engine.process_task("Setup GPS hardware module for motorbike navigation.")
    print(f"MahimaAI Thought Process: {result}\n")
    
    # 2. Trigger the physical "Execution" skill
    print("Triggering hardware execution layer...")
    loader = SkillsLoader()
    skill_result = loader.execute_skill("hardware_check")
    print(f"Hardware Execution Result: {skill_result}")

if __name__ == "__main__":
    asyncio.run(run_test())