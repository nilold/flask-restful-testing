from tests.base_test import BaseTest
from models.item import ItemModel
from models.store import StoreModel
import json


class ItemSystemTest(BaseTest):
    def setUp(self):
        super().setUp()
        with self.app_context():
            StoreModel("store_1").save_to_db()

    def test_create_item(self):
        with self.app() as client:
            with self.app_context():
                response = client.post("/item/item_1", data={"name": "item_1", "price": 12.99, "store_id": 1})
                self.assertEqual(201, response.status_code)
                self.assertIsNotNone(ItemModel.find_by_name("item_1"))

    def test_get_item_no_auth(self):
        with self.app() as client:
            with self.app_context():
                response = client.get("/item/item_1")
                self.assertEqual(401, response.status_code)

    def test_get_item_with_auth(self):
        with self.app() as client:
            with self.app_context():
                ItemModel("item_1", 12.99, 1).save_to_db()
                client.post("/register", data={"username": "abc", "password": "abc"})
                auth_resp = client.post(
                    "/auth",
                    data=json.dumps({"username": "abc", "password": "abc"}),
                    headers={"Content-Type": "application/json"})
                access_token = auth_resp.json['access_token']
                response = client.get("/item/item_1", headers={"Authorization": f"JWT {access_token}"})

                self.assertEqual(200, response.status_code)
                self.assertIsNotNone(ItemModel.find_by_name("item_1"))

    def test_get_item_with_auth_not_found(self):
        with self.app() as client:
            with self.app_context():
                client.post("/register", data={"username": "abc", "password": "abc"})
                auth_resp = client.post(
                    "/auth",
                    data=json.dumps({"username": "abc", "password": "abc"}),
                    headers={"Content-Type": "application/json"})
                access_token = auth_resp.json['access_token']
                response = client.get("/item/item_1", headers={"Authorization": f"JWT {access_token}"})

                self.assertEqual(404, response.status_code)
                self.assertIsNone(ItemModel.find_by_name("item_1"))

    def test_delete_item(self):
        with self.app() as client:
            with self.app_context():
                ItemModel("item_1", 12.99, 1).save_to_db()
                response = client.delete("/item/item_1")
                self.assertEqual(200, response.status_code)
                self.assertIsNone(ItemModel.find_by_name("item_1"))

    def test_modifying_item(self):
        with self.app() as client:
            with self.app_context():
                ItemModel("item_1", 12.99, 1).save_to_db()
                response = client.put("/item/item_1", data={"name": "item_1", "price": 1.99, "store_id": 1})
                self.assertEqual(200, response.status_code)
                item = ItemModel.find_by_name("item_1")
                self.assertIsNotNone(item)
                self.assertEqual("item_1", item.name)
                self.assertEqual(1.99, item.price)
                self.assertEqual(1, item.store_id)

    def test_put_with_inexistent_item(self):
        with self.app() as client:
            with self.app_context():
                response = client.put("/item/item_1", data={"name": "item_1", "price": 1.99, "store_id": 1})
                self.assertEqual(200, response.status_code)
                item = ItemModel.find_by_name("item_1")
                self.assertIsNotNone(item)
                self.assertEqual("item_1", item.name)
                self.assertEqual(1.99, item.price)
                self.assertEqual(1, item.store_id)

    def list_items(self):
        with self.app() as client:
            with self.app_context():
                ItemModel("item_1", 12.99, 1).save_to_db()
                ItemModel("item_2", 12.99, 1).save_to_db()
                response = client.get("/items")

                self.assertEqual(200, response.status_code)
                self.assertEqual(2, len(response.json["items"]))
                self.assertEqual("item_1", response.json["items"][0]["name"])
                self.assertEqual("item_2", response.json["items"][1]["name"])
