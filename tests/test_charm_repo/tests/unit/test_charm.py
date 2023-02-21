# Copyright 2023 Robert Gildein
# See LICENSE file for licensing details.
#
# Learn more about testing at: https://juju.is/docs/sdk/testing
"""Dummy unit tests."""

import unittest

from ops.model import ActiveStatus
from ops.testing import Harness

from charm import TestCharm


class TestCharmCase(unittest.TestCase):
    """Dummy TestCase."""

    def setUp(self):
        self.harness = Harness(TestCharm)
        self.addCleanup(self.harness.cleanup)
        self.harness.begin()

    def test_init(self):
        """Test charm initialization."""
        self.assertEqual(self.harness.model.unit.status, ActiveStatus())
