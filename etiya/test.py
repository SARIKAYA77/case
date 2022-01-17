from api import app
import unittest

class FlaskTest(unittest.TestCase):
    def runTest_train(self):
        tester = app.test_client(self)
        response = tester.get("train")
        status_code = response.status_code
        self.assertEqual(status_code,200)
        print("test case 1 completed")
        
    def runTest_prediction(self):
        tester = app.test_client(self)
        response = tester.get("/prediction/<text>")
        status_code = response.status_code
        self.assertEqual(status_code,308)
        print("test case 2 completed")
        
if __name__ == "__main__":
    tester = FlaskTest()
    tester.runTest_train()
    tester.runTest_prediction()
    
    
        