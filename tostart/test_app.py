from django.apps import apps
from django.test import TestCase
from .apps import TostartConfig

class TestToStartConfig(TestCase):
    def test_app(self):
        self.assertEqual("tostart", TostartConfig.name)
                #won't work 
        #self.assertEqual("tostart", apps.get_app_config("tostart"))