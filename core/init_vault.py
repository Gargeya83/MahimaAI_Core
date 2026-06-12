import os
from core.memory import MemoryVault

# Create the data directory if it doesn't exist
if not os.path.exists("data"):
    os.makedirs("data")

# Initialize the vault - this will create your 'secret.key' and 'memory.db'
vault = MemoryVault()

print("Vault Initialized successfully.")
print("Security Key generated and saved to data/secret.key")
print("Memory Database created at data/memory.db")