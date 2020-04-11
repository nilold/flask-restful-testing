from models.item import ItemModel
from tests.base_test import BaseTest
from models.store import StoreModel


class StoreSystemTest(BaseTest):
    def test_create_store(self):
        with self.app() as client:
            with self.app_context():
                response = client.post("/store/new-store")

                self.assertEqual(201, response.status_code)
                self.assertIsNotNone(StoreModel.find_by_name("new-store"))

    def test_delete_store(self):
        with self.app() as client:
            with self.app_context():
                StoreModel("store").save_to_db()
                self.assertIsNotNone(StoreModel.find_by_name("store"))

                response = client.delete("/store/store")
                self.assertEqual(200, response.status_code)
                self.assertIsNone(StoreModel.find_by_name("store"))

    def test_find_store(self):
        with self.app() as client:
            with self.app_context():
                StoreModel("store").save_to_db()
                response = client.get("/store/store")

                self.assertEqual(200, response.status_code)
                self.assertIsNotNone(response)
                self.assertEqual("store", response.json["name"])
                self.assertEqual([], response.json["items"])

    def test_store_find_with_items(self):
        with self.app() as client:
            with self.app_context():
                store = StoreModel("store")
                item = ItemModel(name="item_1", price=23.90, store_id=1)
                item_2 = ItemModel(name="item_2", price=23.90, store_id=1)
                store.items.append(item)
                store.items.append(item_2)
                item.save_to_db()
                item_2.save_to_db()
                store.save_to_db()

                response = client.get("/store/store")

                self.assertEqual(200, response.status_code)
                self.assertIsNotNone(response)
                self.assertEqual("store", response.json["name"])
                self.assertEqual(2, len(response.json["items"]))
                self.assertEqual("item_1", response.json["items"][0]["name"])
                self.assertEqual("item_2", response.json["items"][1]["name"])

    def test_store_not_found(self):
        with self.app() as client:
            with self.app_context():
                StoreModel("stor").save_to_db()
                response = client.get("/store/store")

                self.assertEqual(404, response.status_code)

    def test_creating_duplicate_store(self):
        with self.app() as client:
            with self.app_context():
                client.post("/store/new-store")
                response = client.post("/store/new-store")

                self.assertEqual(400, response.status_code)

    def test_store_list(self):
        with self.app() as client:
            with self.app_context():
                StoreModel("store_1").save_to_db()
                StoreModel("store_2").save_to_db()
                StoreModel("store_3").save_to_db()
                StoreModel("store_4").save_to_db()

                response = client.get("/stores")

                self.assertEqual(200, response.status_code)
                self.assertIn("stores", response.json.keys())
                self.assertEqual(4, len(response.json["stores"]))

    def test_store_list_with_items(self):
        with self.app() as client:
            with self.app_context():
                s1 = StoreModel("store_1")
                s2 = StoreModel("store_2")
                s1.items.append(ItemModel("item_1", 1, 1))
                s1.items.append(ItemModel("item_2", 1, 1))
                s2.items.append(ItemModel("item_3", 1, 2))
                s2.items.append(ItemModel("item_4", 2, 2))
                s1.save_to_db()
                s2.save_to_db()

                response = client.get("/stores")

                self.assertEqual(200, response.status_code)
                self.assertIn("stores", response.json.keys())
                self.assertEqual(2, len(response.json["stores"]))
                self.assertEqual("item_1", response.json["stores"][0]["items"][0]["name"])
                self.assertEqual("item_2", response.json["stores"][0]["items"][1]["name"])
                self.assertEqual("item_3", response.json["stores"][1]["items"][0]["name"])
                self.assertEqual("item_4", response.json["stores"][1]["items"][1]["name"])
