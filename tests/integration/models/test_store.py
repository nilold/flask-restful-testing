from models.item import ItemModel
from tests.base_test import BaseTest
from models.store import StoreModel


class StoreModelIntegrationTest(BaseTest):
    def test_crud(self):
        with self.app_context():
            store = StoreModel("Test Store")

            self.assertIsNone(StoreModel.find_by_name("Test Store"))

            store.save_to_db()

            self.assertIsNotNone(StoreModel.find_by_name("Test Store"))

            store.delete_from_db()

            self.assertIsNone(StoreModel.find_by_name("Test Store"))

    def test_new_store_has_no_item(self):
        with self.app_context():
            store = StoreModel("Test Store")
            store.save_to_db()
            retrieved = StoreModel.find_by_name("Test Store")

        self.assertEqual([], store.items.all())

    def test_json(self):
        store = StoreModel("Test Store")
        expected = {
            "id": None,
            "name": "Test Store",
            "items": []
        }

        self.assertEqual(expected, store.json())

    def test_store_relationship(self):
        with self.app_context():
            store = StoreModel("Test Store")
            store.save_to_db()
            item = ItemModel("My Item", 12, 1)
            item.save_to_db()

            self.assertEqual(store.items.count(), 1)
            self.assertEqual(store.items.first().name, "My Item")

            expected_json = {
                "id": 1,
                "name": "Test Store",
                "items": [
                    {"name": "My Item", "price": 12.0}
                ]
            }

            self.assertDictEqual(expected_json, store.json())
