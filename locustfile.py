from locust import HttpLocust, TaskSet, task

class HomescreenTest(TaskSet):

    @task
    def home(self):
        self.client.get("/")

class HomeTest(HttpLocust):
    task_set = HomescreenTest
    # minimum and maximum wait in milli seconds
    min_wait = 1000
    max_wait = 5000

