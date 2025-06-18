import unittest
import pandas as pd
from src.eda_utils import calculate_headline_length

class TestEDAUtils(unittest.TestCase):
    
    def test_headline_length(self):
        df = pd.DataFrame({
            "headline": ["Stock rises", "Market falls", "Apple hits all-time high"]
        })
        result = calculate_headline_length(df)
        self.assertIn("headline_length", result.columns)
        self.assertEqual(result["headline_length"].tolist(), [11, 12, 26])

if __name__ == '__main__':
    unittest.main()
