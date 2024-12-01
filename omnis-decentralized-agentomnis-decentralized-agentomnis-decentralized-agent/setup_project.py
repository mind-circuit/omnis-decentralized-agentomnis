import os

# Define the project structure
project_name = "omnis_decentralized_agent"
directories = [
    "config",
    "modules",
    "modules/defi_agents",
    "models",
    "scripts",
    "tests"
]
files = {
    "README.md": "# Omnis Decentralized Financial Agent\n\n**Omnis** is an advanced AI agent that commands a network of DeFi sub-agents for arbitrage, liquidity management, and predictive modeling...",
    "LICENSE": "MIT License",
    ".gitignore": "__pycache__/\n*.pyc\n.env",
    "requirements.txt": "openai\nrequests\nnumpy\npandas\nscikit-learn\nweb3",
    "main.py": """from modules.defi_agents.arbitrage_agent import ArbitrageAgent
from modules.defi_agents.liquidity_manager import LiquidityManager
from modules.trading_executor import TradingExecutor

class Omnis:
    def __init__(self):
        self.arbitrage_agent = ArbitrageAgent()
        self.liquidity_manager = LiquidityManager()
        self.trading_executor = TradingExecutor()
        self.active = True

    def start(self):
        print("OMNIS SYSTEM INITIALIZED... READY FOR COMMANDS.\\n")
        while self.active:
            user_input = input("OMNIS > ").strip().upper()
            self.process_input(user_input)

    def process_input(self, command):
        if command == "RUN ARBITRAGE":
            self.arbitrage_agent.execute()
        elif command == "MANAGE LIQUIDITY":
            self.liquidity_manager.manage()
        elif command == "EXECUTE TRADE":
            self.trading_executor.execute_trade()
        elif command == "EXIT":
            print("SHUTTING DOWN...")
            self.active = False
        else:
            print("INVALID COMMAND. REFER TO COMMAND LIST.")

if __name__ == "__main__":
    omnis = Omnis()
    omnis.start()"""
}

# Create the project structure
if not os.path.exists(project_name):
    os.mkdir(project_name)

for directory in directories:
    path = os.path.join(project_name, directory)
    if not os.path.exists(path):
        os.makedirs(path)

for filename, content in files.items():
    file_path = os.path.join(project_name, filename)
    with open(file_path, 'w') as f:
        f.write(content)

# Creating Python files in modules/defi_agents directory
defi_agents_files = {
    "arbitrage_agent.py": """import requests

class ArbitrageAgent:
    def __init__(self):
        pass

    def execute(self):
        print("EXECUTING ARBITRAGE STRATEGY...")
        try:
            response = requests.get('https://api.coinmarketcap.com/data-api/v3/topsearch/rank')
            if response.status_code == 200:
                data = response.json()
                print("ARBITRAGE DATA:", data)
            else:
                print("FAILED TO FETCH MARKET DATA.")
        except Exception as e:
            print(f"ERROR DURING ARBITRAGE EXECUTION: {e}")""",

    "liquidity_manager.py": """class LiquidityManager:
    def __init__(self):
        pass

    def manage(self):
        print("MANAGING LIQUIDITY...")"""
}

for filename, content in defi_agents_files.items():
    file_path = os.path.join(project_name, "modules", "defi_agents", filename)
    with open(file_path, 'w') as f:
        f.write(content)

# Print completion message
print(f"Project '{project_name}' has been set up with the necessary directories and files.")
