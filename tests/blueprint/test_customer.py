from tests.db_helper import add_dummy_data_for_customer
from tests.fixtures import FlaskClientWithDB
import unittest


class TestGetCustomer(FlaskClientWithDB):
    def setUp(self):
        super().setUp()

    def test_happy_case(self):
        add_dummy_data_for_customer(self.db)
        api = "/customer/retrieve?name=siraj"
        HEADERS = {"Content-Type": "application/json"}
        res = self.client.get(api, headers=HEADERS, follow_redirects=True)
        expected_response = [{'address': '12345', 'id': 1, 'name': 'siraj'}]
        self.assertEqual(res.json, expected_response)
        self.assertEqual(res.status_code, 200)

    def test_no_parameter_pass_case(self):
        add_dummy_data_for_customer(self.db)
        api = "/customer/retrieve"
        HEADERS = {"Content-Type": "application/json"}
        res = self.client.get(api, headers=HEADERS, follow_redirects=True)
        expected_response = {'errors': {'query': {'name': ['Missing data for required field.']}}}
        self.assertEqual(res.json, expected_response)
        self.assertEqual(res.status_code, 422)

    def test_invalid_data_type_pass_case(self):
        add_dummy_data_for_customer(self.db)
        api = "/customer/retrieve?name=123"
        HEADERS = {"Content-Type": "application/json"}
        res = self.client.get(api, headers=HEADERS, follow_redirects=True)
        expected_response = {'error': 'customer not found'}
        self.assertEqual(res.json, expected_response)
        self.assertEqual(res.status_code, 422)

    
    def test_invalid_name_passed_to_db_case(self):
        add_dummy_data_for_customer(self.db)
        api = "/customer/retrieve?name=ikram"
        HEADERS = {"Content-Type": "application/json"}
        res = self.client.get(api, headers=HEADERS, follow_redirects=True)
        expected_response = {'error': 'customer not found'}
        self.assertEqual(res.json, expected_response)
        self.assertEqual(res.status_code, 422)


    def test_prefix_name_passed_to_db_case(self):
        add_dummy_data_for_customer(self.db)
        api = "/customer/retrieve?name=sir"
        HEADERS = {"Content-Type": "application/json"}
        res = self.client.get(api, headers=HEADERS, follow_redirects=True)
        expected_response = [{'address': '12345', 'id': 1, 'name': 'siraj'}]
        self.assertEqual(res.json, expected_response)
        self.assertEqual(res.status_code, 200)


    def tearDown(self):
        super().tearDown()



if __name__ == "__main__":
    unittest.main()