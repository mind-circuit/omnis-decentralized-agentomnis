import unittest
from modules.defi_agents.arbitrage_agent import ArbitrageAgent

class TestArbitrageAgent(unittest.TestCase):
    def setUp(self):
        self.agent = ArbitrageAgent()

    def test_execute(self):
        # This test checks that the method runs without exceptions
        try:
            self.agent.execute()
            result = True
        except:
            result = False
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()
