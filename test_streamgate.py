# test_streamgate.py
"""
Tests for StreamGate module.
"""

import unittest
from streamgate import StreamGate

class TestStreamGate(unittest.TestCase):
    """Test cases for StreamGate class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = StreamGate()
        self.assertIsInstance(instance, StreamGate)
        
    def test_run_method(self):
        """Test the run method."""
        instance = StreamGate()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
