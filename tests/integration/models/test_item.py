from models.store import StoreModel
from tests.base_test import BaseTest
from models.item import ItemModel


class ItemIntegrationTest(BaseTest):
    def test_crud(self):
        with self.app_context():
            StoreModel("Test Store").save_to_db()
            item = ItemModel('test', 19.99, 1)

            self.assertIsNone(ItemModel.find_by_name("test"))

            item.save_to_db()

            self.assertIsNotNone(ItemModel.find_by_name('test'))

            item.delete_from_db()

            self.assertIsNone(ItemModel.find_by_name("test"))

    def test_store_relationship(self):
        with self.app_context():
            store = StoreModel("Test Store")
            item = ItemModel('test', 19.99, 1)

            store.save_to_db()
            item.save_to_db()

            self.assertEqual(item.store.name, "Test Store")
