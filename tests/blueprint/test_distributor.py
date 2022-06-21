from tests.fixtures import FlaskClientWithDB
from tests.db_helper import add_dummy_data_for_distributor
import json, unittest

class TestDistributor(FlaskClientWithDB):
    def setUp(self):
        super().setUp()
        add_dummy_data_for_distributor(self.db)

    def test_retrieve_distributor_happy_case(self):
        api = "/distributor/retrieve?name=UDL"
        HEADERS = {"Content-Type": "application/json"}
        res = self.client.get(api, headers=HEADERS, follow_redirects=True)
        self.assertEqual(res.status_code, 200)
       
        expected_response = {'address': 'peshawar', 'contact': '1234', 'id': 1, 'name': 'UDL'}
        self.assertEqual(res.json, expected_response)

    def test_retrieve_distributor_required_parameters(self):
        # Field 1 (REQUIRED)
        api = "/distributor/retrieve"
        HEADERS = {"Content-Type": "application/json"}
        res = self.client.get(api, headers=HEADERS, follow_redirects=True)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(res.json, {'errors': {'query': {'name': ['Missing data for required field.']}}})

    def test_add_distributor_happy_case(self):
        api = "/distributor/add"
        HEADERS = {"Content-Type": "application/json"}
        payload = {
            "name": "imran",
            "contact": "25236"
        }

        res = self.client.post(api, headers=HEADERS, data=json.dumps(payload) ,follow_redirects=True)
        self.assertEqual(res.status_code, 200)
        
        expected_response = {'address': None, 'contact': '25236', 'id': 3, 'name': 'imran'}
        self.assertEqual(res.json, expected_response)
        # self.assertTrue(typr(res.json["name"]), )

    def test_add_distributor_wrong_values_passed_case(self):
        api = "/distributor/add"
        HEADERS = {"Content-Type": "application/json"}
        payload = {
            "name": "imran",
            "contact": "25236"
        }

        # Wrong value for field 1 (name)
        wrong_payload = payload.copy()
        wrong_payload["name"] = 123
        res = self.client.post(api, headers=HEADERS, data=json.dumps(wrong_payload) ,follow_redirects=True)
        self.assertEqual(res.status_code, 422)

        # Wrong value for field 2 (contact)
        wrong_payload = payload.copy()
        wrong_payload["contact"] = 123
        res = self.client.post(api, headers=HEADERS, data=json.dumps(wrong_payload) ,follow_redirects=True)
        self.assertEqual(res.status_code, 422)
        

    def tearDown(self):
        super().tearDown()


if __name__ == "__main__":
    unittest.main()

