#!/usr/bin/python3
"""model create test class user"""
import unittest
import os
import models
import unittest
from models.user import User
from time import sleep
from datetime import datetime


class TestUser(unittest.TestCase):
    """class test user"""
    def setUP(self):
        self.user = User()

    def test_not_args(self):
        self.assertEqual(User, type(User()))

    def test_email_str(self):
        self.assertEqual(str, type(User.email))

    def test_password_str(self):
        self.assertEqual(str, type(User.password))

    def test_first_name_str(self):
        self.assertEqual(str, type(User.first_name))

    def test_last_name_str(self):
        self.assertEqual(str, type(User.last_name))

    def test_two_user_unique_id(self):
        user1 = User()
        user2 = User()
        self.assertNotEqual(user1.id, user2.id)

    def test_two_users_created_at_and_updated_at(self):
        user1 = User()
        sleep(0.05)
        user2 = User()
        self.assertLess(user1.created_at, user2.created_at)
        self.assertLess(user1.updated_at, user2.updated_at)

    def test_str_representation(self):
        date_time = datetime.today()
        date_time_repr = repr(date_time)
        user = User()
        user.id = "21212"
        user.created_at = user.updated_at = date_time
        user_str = user.__str__()
        self.assertIn("[User] (21212)", user_str)
        self.assertIn("'id': '21212'", user_str)
        self.assertIn("'created_at': " + date_time_repr, user_str)
        self.assertIn("'updated_at': " + date_time_repr, user_str)

    def test_instantiation_None_kwargs(self):
        with self.assertRaises(TypeError):
            User(id=None, created_at=None, updated_at=None)

    def test_save_one_user(self):
        user = User()
        sleep(0.05)
        first_updated_at = user.updated_at
        user.save()
        self.assertLess(first_updated_at, user.updated_at)

    def test_save_two_user(self):
        user = User()
        sleep(0.05)
        first_updated_at = user.updated_at
        user.save()
        second_updated_at = user.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        user.save()
        self.assertLess(second_updated_at, user.updated_at)

    def test_save_with_arg(self):
        user = User()
        with self.assertRaises(TypeError):
            user.save(None)

    def test_save_updates_file(self):
        user = User()
        user.save()
        usid = "User." + user.id
        with open("file.json", "r") as f:
            self.assertIn(usid, f.read())


if __name__ == "__main__":
    unittest.main()
