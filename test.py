from main import app, association, get_role_id
import unittest
import requests
import logging
import os
import time


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(message)s',
                    handlers=[logging.StreamHandler(),logging.FileHandler(filename=os.path.join("logs/Log_"+time.strftime("%Y%m%d-%H%M%S")+".log"))])



base_url = 'http://localhost:5000'

class UnitTest(unittest.TestCase):
    def test_association(self):
        with app.app_context():
            c = association(1)
            # print(c)
            # result = app.app_context()
            response = requests.get(f"{base_url}/employees/1")
            self.assertEqual(200, c.status_code)
            logging.info("Unit Test 1 Pass")

    def test_get_role_id(self):
        with app.app_context():
            c = get_role_id(1)
            # response = requests.get(f"{base_url}/roles/1")
            self.assertEqual(200, c.status_code)
            logging.info("Unit Test 2 Pass")



class TestEmployee(unittest.TestCase):
    employee = {'first_name': 'Narayan',
                'last_name': 'Sankara',
                'emp_id': 3}

    # Check for responce 200
    def test_employee_retrieve(self):
        result = app.test_client()
        response = result.get(f"{base_url}/employees")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        logging.info("Emp: Test 1 - test_employee_retrieve Pass")


    # check if application/json

    def test_content_type(self):
        result = app.test_client()
        response = result.get(f"{base_url}/employees")
        self.assertEqual(response.content_type, "application/json")
        logging.info("Emp: Test 2 - test_content_type Pass")


    # check for data return

    def test_vaidate_emp(self):
        result = app.test_client()
        response = result.get(f"{base_url}/employees")
        self.assertTrue(b'Savan' in response.data)
        logging.info("Emp: Test 3 - test_validate_emp Pass")

    # check length of json
    def test_length_emp(self):
        response = requests.get(f"{base_url}/employees")
        self.assertEqual(len(response.json()), 1)
        logging.info("Emp: Test 4 test_length_emp Pass")


    # test create employee record
    def test_post_emp(self):
        response = requests.post(f"{base_url}/employees", self.employee)
        self.assertEqual(response.status_code, 200)
        logging.info("Emp: Test 5 - test_post_emp Pass")



class TestRole(unittest.TestCase):
    role = {
        "role_name": "Finance"
    }
    expected_result = {
        "roles": {
            "role_id": 1,
            "role_name": "Manager"
        }
    }
    updated_role = {"role_name": "ADMIN007"}

    # Check for responce 200
    def test_roles_retrieve(self):
        result = app.test_client()
        response = result.get(f"{base_url}/roles")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        logging.info("Role: Test 1 - test_role_tetrieve Pass")

    # check if application/json
    def test_content_type(self):
        result = app.test_client()
        response = result.get(f"{base_url}/roles")
        self.assertEqual(response.content_type, "application/json")
        logging.info("Role: Test 2 - test_content_type Pass")


    # check for data return
    def test_vaidate_role(self):
        result = app.test_client()
        response = result.get(f"{base_url}/roles")
        self.assertTrue(b'Admin' in response.data)
        logging.info("Role: Test 3 - test_validate_role Pass")

    # check json length
    def test_length_role(self):
        response = requests.get(f"{base_url}/roles")
        self.assertEqual(len(response.json()), 1)
        logging.info("Role: Test 4 - test_length_role Pass")

    # test Create role record
    def test_post_role(self):
        response = requests.post(f"{base_url}/roles", self.role)
        self.assertEqual(response.status_code, 200)
        logging.info("Role: Test 5 - test_post_role Pass")

    # test expected result
    def test_expected_role_id(self):
        response = requests.get(f"{base_url}/roles/1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), self.expected_result)
        logging.info("Role: Test 6 - test_expected_role Pass")

    # test update employee
    # def test_update_role(self):
    #     response = requests.put(f"http://127.0.0.1:5000/roles/1", json=self.updated_role)
    #     print(response.json())
    #     self.assertEqual(response.json()['role_name'], self.updated_role['role_name'])
    #     print("Role: Test 7 Completed")


if __name__ == "__main__":
    emptest = TestEmployee()
    roletest = TestRole()
    unit_t = UnitTest()
    emptest.test_employee_retrieve()
    emptest.test_content_type()
    emptest.test_vaidate_emp()
    emptest.test_length_emp()
    emptest.test_post_emp()

    roletest.test_roles_retrieve()
    roletest.test_content_type()
    roletest.test_vaidate_role()
    roletest.test_length_role()
    roletest.test_post_role()
    roletest.test_expected_role_id()
    # roletest.test_update_role()

    unit_t.test_association()
    unit_t.test_get_role_id()