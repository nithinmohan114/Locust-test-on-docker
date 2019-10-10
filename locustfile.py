from locust import HttpLocust, TaskSet, task


class HomescreenTest(TaskSet):

    @task(1)
    def home(self):
        self.client.get("/")

    @task(2)
    def polls(self):
        self.client.get("/polls")

    @task(3)
    def polls_list(self):
        self.client.get("/polls/2/")


class HomeTest(HttpLocust):
    task_set = HomescreenTest
    # minimum and maximum wait in milli seconds
    min_wait = 5
    max_wait = 4
