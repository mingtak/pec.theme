# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from pec.theme.testing import PEC_THEME_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that pec.theme is properly installed."""

    layer = PEC_THEME_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if pec.theme is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'pec.theme'))

    def test_browserlayer(self):
        """Test that IPecThemeLayer is registered."""
        from pec.theme.interfaces import (
            IPecThemeLayer)
        from plone.browserlayer import utils
        self.assertIn(IPecThemeLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = PEC_THEME_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['pec.theme'])

    def test_product_uninstalled(self):
        """Test if pec.theme is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'pec.theme'))

    def test_browserlayer_removed(self):
        """Test that IPecThemeLayer is removed."""
        from pec.theme.interfaces import IPecThemeLayer
        from plone.browserlayer import utils
        self.assertNotIn(IPecThemeLayer, utils.registered_layers())
