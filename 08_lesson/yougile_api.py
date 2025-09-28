import requests


class YougileAPI:

    BASE_URL = "https://yougile.com/api-v2"

    API_TOKEN = "YOUR_YOූILE_API_TOKEN"

    def __init__(self):
        self.headers = {
            "Authorization": f"Bearer {self.API_TOKEN}",
            "Content-Type": "application/json"
        }

    def create_project(self, title):
        url = f"{self.BASE_URL}/projects"
        payload = {"title": title}
        return requests.post(url, headers=self.headers, json=payload)

    def get_project(self, project_id):
        url = f"{self.BASE_URL}/projects/{project_id}"
        return requests.get(url, headers=self.headers)

    def update_project(self, project_id, new_title):
        url = f"{self.BASE_URL}/projects/{project_id}"
        payload = {"title": new_title}
        return requests.put(url, headers=self.headers, json=payload)

    def delete_project(self, project_id):
        url = f"{self.BASE_URL}/projects/{project_id}"
        return requests.delete(url, headers=self.headers)
