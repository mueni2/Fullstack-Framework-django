from django.test import TestCase
from .models import Item


class TestModels(TestCase):

    def test_done_default_to_fales(self):
        item = Item.objects.create(name='Test Todo Item')
        self.assertFalse(item.done)

    def test_item_string_method_name(self):
        item = Item.objects.create(name='Test Todo Item')
        self.assertEqual(str(item), 'Test Todo Item')