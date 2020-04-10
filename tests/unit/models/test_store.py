from models.store import StoreModel
from tests.unit.unit_base_test import UnitBaseTest


class TestStore(UnitBaseTest):
    def test_create_store(self):
        store = StoreModel("test")
        self.assertEqual("test", store.name)
