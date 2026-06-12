from core.memory import MemoryVault
from core.skills_loader import SkillsLoader
import logging

class ReasoningEngine:
    def __init__(self):
        self.vault = MemoryVault()
        self.skills = SkillsLoader()
        self.logger = logging.getLogger("ReasoningEngine")

    async def autonomous_task(self, task_description):
        self.logger.info(f"Reasoning: I need to solve: {task_description}")
        
        # 1. Tactic Selection (The "Smarter" part)
        # We look at the task and find a matching skill
        available_skills = self.skills.list_skills()
        
        # Simple heuristic: If the task mentions 'hardware', run 'hardware_check'
        if "hardware" in task_description.lower():
            self.logger.info("Tactic selected: Executing hardware_check skill")
            result = self.skills.execute_skill("hardware_check")
            self.vault.save_memory(f"Task: {task_description} | Result: {result}")
            return result
        
        return "I need more tactical data to choose a skill."