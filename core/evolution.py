import os
import subprocess
import logging

class EvolutionModule:
    def __init__(self, repo_path="."):
        self.repo_path = repo_path
        self.logger = logging.getLogger("EvolutionEngine")

    def check_for_updates(self):
        """Checks the git repository for new 'skill' code."""
        try:
            self.logger.info("Checking for system evolution...")
            # Run git pull to get latest code from your repo
            result = subprocess.run(["git", "pull"], capture_output=True, text=True, cwd=self.repo_path)
            if "Already up to date" in result.stdout:
                return "System is current."
            else:
                return "Evolution applied: New skills/logic detected."
        except Exception as e:
            return f"Evolution error: {e}"