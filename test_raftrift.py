# test_raftrift.py
"""
Tests for RaftRift module.
"""

import unittest
from raftrift import RaftRift

class TestRaftRift(unittest.TestCase):
    """Test cases for RaftRift class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = RaftRift()
        self.assertIsInstance(instance, RaftRift)
        
    def test_run_method(self):
        """Test the run method."""
        instance = RaftRift()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
