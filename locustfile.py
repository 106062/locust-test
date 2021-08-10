import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def hello_world(self):
        self.client.get("/");

    @task
    def post_num(self):
        with self.client.post("/numof2", json = { "num1" : "1", "num2" : "3" }, 
                              catch_response = True ) as response:
            if response.json() ["Result"] != "0":
                response.failure("Error");
