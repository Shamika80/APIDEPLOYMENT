import unittest
import json
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_positive_sum(self):   

    response = self.app.post('/sum', json={'num1': 1, 'num2': 2})
    data = json.loads(response.get_data(as_text=True))
    self.assertEqual(response.status_code, 200)
    self.assertEqual(data['result'], 3)

    def test_negative_sum(self):
        response = self.app.post('/sum', json={'num1': -1, 'num2': -2})
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['result'],-3)
    def test_missing_parameter(self):
        response = self.app.post('/sum', json={'num1': 1})
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', data)

    def test_invalid_result_filter(self):
        """Test with an invalid filter value (non-integer)."""
        response = self.app.get('/sum/result/invalid') 
        self.assertEqual(response.status_code, 404) 

    def test_nonexistent_result_filter(self):
        """Test with a result value that doesn't exist."""
        response = self.app.get('/sum/result/999')  
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)  
        self.assertEqual(data, []) 

if __name__ == '__main__':
    unittest.main()