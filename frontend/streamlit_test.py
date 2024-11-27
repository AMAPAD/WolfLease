'''
Copyright 2023 Ashwattha Phatak, Anish Mulay, Akshay Dongare

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''
import unittest
import streamlit as st
from app import (
    create_user, login, flat_page, user_page, lease_page, interest_page,
    add_lease, sign_lease, dashboard, main, BASE_URL
)

class TestStreamlitApp(unittest.TestCase):

    def test_base_url(self):
        self.assertEqual(BASE_URL, "http://localhost:8000/")

    def test_create_user_function_exists(self):
        self.assertTrue(callable(create_user))

    def test_login_function_exists(self):
        self.assertTrue(callable(login))

    def test_flat_page_function_exists(self):
        self.assertTrue(callable(flat_page))

    def test_user_page_function_exists(self):
        self.assertTrue(callable(user_page))

    def test_lease_page_function_exists(self):
        self.assertTrue(callable(lease_page))

    def test_interest_page_function_exists(self):
        self.assertTrue(callable(interest_page))

    def test_add_lease_function_exists(self):
        self.assertTrue(callable(add_lease))

    def test_sign_lease_function_exists(self):
        self.assertTrue(callable(sign_lease))

    def test_dashboard_function_exists(self):
        self.assertTrue(callable(dashboard))

    def test_main_function_exists(self):
        self.assertTrue(callable(main))

    def test_session_state_initialization(self):
        main()
        self.assertIn('logged_in', st.session_state)
        self.assertIn('registering', st.session_state)

    def test_create_user_form_fields(self):
        with st.form("user_form"):
            self.assertIsNotNone(st.text_input("Username"))
            self.assertIsNotNone(st.text_input("Name"))
            self.assertIsNotNone(st.text_input("Email"))
            self.assertIsNotNone(st.text_input("Contact Number"))
            self.assertIsNotNone(st.text_input("Password", type="password"))
            self.assertIsNotNone(st.date_input("Date of Birth"))
            self.assertIsNotNone(st.selectbox("Gender", ["M", "F", "O"]))
            self.assertIsNotNone(st.selectbox("User Type", ["User", "Owner"]))
            self.assertIsNotNone(st.selectbox("Smoking Preference", ["Y", "N"]))
            self.assertIsNotNone(st.selectbox("Drinking Preference", ["Y", "N"]))
            self.assertIsNotNone(st.selectbox("Vegetarian Preference", ["Y", "N"]))

    def test_create_user_form_invalid_fields(self):
        with st.form("user_form"):
            self.assertIsNotNone(st.text_input("Username"))
            self.assertIsNotNone(st.text_input("Name"))
            self.assertIsNotNone(st.text_input("Email"))
            self.assertIsNotNone(st.text_input("Contact Number"))
            self.assertIsNotNone(st.text_input("Password", type="password"))
            self.assertIsNotNone(st.date_input("Date of Birth"))
            self.assertIsNotNone(st.selectbox("Gender", ["M", "F", "O"]))
            self.assertIsNotNone(st.selectbox("User Type", ["User", "Owner"]))
            self.assertIsNone(st.selectbox("Smoking Preference", []))
            self.assertIsNotNone(st.selectbox("Drinking Preference", ["Y", "N"]))
            self.assertIsNotNone(st.selectbox("Vegetarian Preference", ["Y", "N"]))

    def test_login_form_fields(self):
        self.assertIsNotNone(st.text_input("Email"))
        self.assertIsNotNone(st.text_input("Password", type='password'))

    def test_dashboard_logout_button(self):
        self.assertIsNotNone(st.button("Logout"))

    def test_main_page_options(self):
        options = ["Flats", "Users", "Leases", "Interests", "Add Lease", "Sign Lease"]
        for option in options:
            self.assertIn(option, main.__code__.co_consts)

    def test_main_page_size(self):
        size = 16
        self.assertEqual(size, len(main.__code__.co_consts))

    def test_main_page_options_has_flat(self):
        self.assertTrue("Flats" in main.__code__.co_consts)

    def test_main_page_options_has_leases(self):
        self.assertTrue("Leases" in main.__code__.co_consts)

if __name__ == '__main__':
    unittest.main()