from models.item import ItemModel
from tests.unit.unit_base_test import UnitBaseTest


class ItemModelTest(UnitBaseTest):
    def test_create_item(self):
        name = 'item_1'
        price = 12.34
        item = ItemModel(name=name, price=price, store_id=1)

        self.assertEqual(name, item.name)
        self.assertEqual(price, item.price)

    def test_item_json(self):
        name = 'item_1'
        price = 12.34
        item = ItemModel(name=name, price=price, store_id=1)
        expected_json = {'name': name, 'price': price}

        self.assertEqual(expected_json, item.json())


