#!/usr/bin/python3
"""model create test class Place"""
import unittest
import os
import models
from models.place import Place
from datetime import datetime
from time import sleep


class TestPlace(unittest.TestCase):
    """class test Place"""
    def setUP(self):
        """creeate opj State test"""
        self.place = Place()

    def test_not_args(self):
        self.assertEqual(Place, type(Place()))

    def test_city_id_attribute(self):
        pl = Place()
        self.assertEqual(str, type(Place.city_id))
        self.assertIn("city_id", dir(pl))
        self.assertNotIn("city_id", pl.__dict__)

    def test_user_id_attribute(self):
        pl = Place()
        self.assertEqual(str, type(Place.user_id))
        self.assertIn("user_id", dir(pl))
        self.assertNotIn("user_id", pl.__dict__)

    def test_name_attribute(self):
        pl = Place()
        self.assertEqual(str, type(Place.name))
        self.assertIn("name", dir(pl))
        self.assertNotIn("name", pl.__dict__)

    def test_description_attribute(self):
        pl = Place()
        self.assertEqual(str, type(Place.description))
        self.assertIn("description", dir(pl))
        self.assertNotIn("desctiption", pl.__dict__)

    def test_number_rooms_attribute(self):
        pl = Place()
        self.assertEqual(int, type(Place.number_rooms))
        self.assertIn("number_rooms", dir(pl))
        self.assertNotIn("number_rooms", pl.__dict__)

    def test_number_bathrooms_attribute(self):
        pl = Place()
        self.assertEqual(int, type(Place.number_bathrooms))
        self.assertIn("number_bathrooms", dir(pl))
        self.assertNotIn("number_bathrooms", pl.__dict__)

    def test_max_guest_attribute(self):
        pl = Place()
        self.assertEqual(int, type(Place.max_guest))
        self.assertIn("max_guest", dir(pl))
        self.assertNotIn("max_guest", pl.__dict__)

    def test_price_by_night_attribute(self):
        pl = Place()
        self.assertEqual(int, type(Place.price_by_night))
        self.assertIn("price_by_night", dir(pl))
        self.assertNotIn("price_by_night", pl.__dict__)

    def test_latitude_attribute(self):
        pl = Place()
        self.assertEqual(float, type(Place.latitude))
        self.assertIn("latitude", dir(pl))
        self.assertNotIn("latitude", pl.__dict__)

    def test_longitude_attribute(self):
        pl = Place()
        self.assertEqual(float, type(Place.longitude))
        self.assertIn("longitude", dir(pl))
        self.assertNotIn("longitude", pl.__dict__)

    def test_amenity_ids_attribute(self):
        pl = Place()
        self.assertEqual(list, type(Place.amenity_ids))
        self.assertIn("amenity_ids", dir(pl))
        self.assertNotIn("amenity_ids", pl.__dict__)

    def test_two_state_created_at_and_updated_at(self):
        state1 = Place()
        sleep(0.05)
        state2 = Place()
        self.assertLess(state1.created_at, state2.created_at)
        self.assertLess(state1.updated_at, state2.updated_at)

    def test_two_states_unique_id(self):
        state1 = Place()
        state2 = Place()
        self.assertNotEqual(state1.id, state2.id)

    def test_str_representation_state(self):
        date_time = datetime.today()
        date_time_repr = repr(date_time)
        state = Place()
        state.id = "21212"
        state.created_at = state.updated_at = date_time
        state_str = state.__str__()
        self.assertIn("[Place] (21212)", state_str)
        self.assertIn("'id': '21212'", state_str)
        self.assertIn("'created_at': " + date_time_repr, state_str)
        self.assertIn("'updated_at': " + date_time_repr, state_str)

    def test_inst_None_kwargs(self):
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)

    def test_inst_kwargs(self):
        date_time = datetime.today()
        datimeiso = date_time.isoformat()
        st = Place(id="987654", created_at=datimeiso, updated_at=datimeiso)
        self.assertEqual(st.id, "987654")
        self.assertEqual(st.created_at, date_time)
        self.assertEqual(st.updated_at, date_time)

    def test_save(self):
        stat = Place()
        sleep(0.05)
        first_updated_at = stat.updated_at
        stat.save()
        self.assertLess(first_updated_at, stat.updated_at)

    def test_two_state_save(self):
        stat = Place()
        sleep(0.05)
        first_updated_at = stat.updated_at
        stat.save()
        second_updated_at = stat.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        stat.save()
        self.assertLess(second_updated_at, stat.updated_at)

    def test_save_with_arg(self):
        stat = Place()
        with self.assertRaises(TypeError):
            stat.save(None)


if __name__ == "__main__":
    unittest.main()
