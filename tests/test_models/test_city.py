#!/usr/bin/python3
"""model create test class city"""

import unittest
import os
import models
import unittest
from models.city import City
from datetime import datetime
from time import sleep


class TestCity(unittest.TestCase):
    """class test state"""
    def setUP(self):
        """creeate opj State test"""
        self.city = City()

    def test_not_args(self):
        self.assertEqual(City, type(City()))

    def test_state_id_str(self):
        self.assertEqual(str, type(City.state_id))

    def test_name_str(self):
        self.assertEqual(str, type(City.name))

    def test_two_state_created_at_and_updated_at(self):
        state1 = City()
        sleep(0.05)
        state2 = City()
        self.assertLess(state1.created_at, state2.created_at)
        self.assertLess(state1.updated_at, state2.updated_at)

    def test_two_states_unique_id(self):
        state1 = City()
        state2 = City()
        self.assertNotEqual(state1.id, state2.id)

    def test_str_representation_state(self):
        date_time = datetime.today()
        date_time_repr = repr(date_time)
        state = City()
        state.id = "21212"
        state.created_at = state.updated_at = date_time
        state_str = state.__str__()
        self.assertIn("[City] (21212)", state_str)
        self.assertIn("'id': '21212'", state_str)
        self.assertIn("'created_at': " + date_time_repr, state_str)
        self.assertIn("'updated_at': " + date_time_repr, state_str)

    def test_inst_None_kwargs(self):
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)

    def test_inst_kwargs(self):
        date_time = datetime.today()
        datime_iso = date_time.isoformat()
        st = City(id="987654", created_at=datime_iso, updated_at=datime_iso)
        self.assertEqual(st.id, "987654")
        self.assertEqual(st.created_at, date_time)
        self.assertEqual(st.updated_at, date_time)

    def test_save(self):
        stat = City()
        sleep(0.05)
        first_updated_at = stat.updated_at
        stat.save()
        self.assertLess(first_updated_at, stat.updated_at)

    def test_two_state_save(self):
        stat = City()
        sleep(0.05)
        first_updated_at = stat.updated_at
        stat.save()
        second_updated_at = stat.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        stat.save()
        self.assertLess(second_updated_at, stat.updated_at)

    def test_save_with_arg(self):
        stat = City()
        with self.assertRaises(TypeError):
            stat.save(None)


if __name__ == "__main__":
    unittest.main()
