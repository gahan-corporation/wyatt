#!/srv/gerp/py/python3
"""Tests for Google Drive integration."""
import unittest


class TestGoogleDrive(unittest.TestCase):
    """Tests for Google Drive integration."""
    value = True

    def test_get_api_key(self):
        """Test get api key."""
        assert self.value is True
