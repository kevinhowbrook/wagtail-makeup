from django.test import TestCase, override_settings
from ..settings import WagtailMakeUpSettings

class MakeupTest(TestCase):

    def test_settings_missing(self):
        wagtail_makeup_settings = WagtailMakeUpSettings()
        self.assertEqual(wagtail_makeup_settings.CLIENT_ID, None)
        self.assertEqual(wagtail_makeup_settings.CLIENT_SECRET, None)

    @override_settings(WAGTAIL_UNSPLASH={'CLIENT_ID': 1234,'CLIENT_SECRET': 'shh'})
    def test_settings_defined(self):
        settings = WagtailMakeUpSettings()
        self.assertEqual(settings.CLIENT_ID, 1234)
        self.assertEqual(settings.CLIENT_SECRET, 'shh')

    # Test settings are defined, if not show a warning

    # Test image file is replaced

