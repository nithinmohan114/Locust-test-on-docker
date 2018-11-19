from locust import HttpLocust, TaskSet, task


class HomescreenTest(TaskSet):

    @task
    def home(self):
        self.client.get("/")

    @task
    def polls(self):
        self.client.get("/polls")

    @task
    def polls_list(self):
        self.client.get("/polls/2/")


class HomeTest(HttpLocust):
    task_set = HomescreenTest
    # minimum and maximum wait in milli seconds
    min_wait = 1000
    max_wait = 5000
