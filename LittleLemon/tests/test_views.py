from django.test import TestCase, RequestFactory

from restaurant.views import MenuItemView
from restaurant.models import Menu

class MenuItemViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.menu_item = Menu.objects.create(title="Tiramisu", price=9, inventory=77)

    def test_get(self):
        request = self.factory.get('restaurant/menu')

        request.menu_item = self.menu_item

        response = MenuItemView.as_view()(request)
        self.assertEqual(response.status_code, 401)