from django.test import TestCase
from .views import Menu
from .serializers import MenuItemSerializer
from decimal import Decimal
class MenuViewTest(TestCase):
    def setUp(self):
        self.menu_item = Menu.objects.create(title='Pizza', price=15.00, inventory=5)
        self.serialized_item = MenuItemSerializer(self.menu_item)
    def test_get_all(self):
        data = self.serialized_item.data 
        expected = {'id': 2, 'title': 'Pizza', 'price': 15.00, 'inventory': 5}
        self.assertEqual(expected['id'], data['id'])
        self.assertEqual(expected['title'], data['title'])
        self.assertEqual(expected['price'], Decimal(data['price']))
        self.assertEqual(expected['inventory'], data['inventory'])
