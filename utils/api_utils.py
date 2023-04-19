import requests


class APIUtils:
    def __init__(self):
        self.requests = requests.Session()
        self.host = "https://api.meteonomiqs.com"
        self.user_id = "rlknl9m9vxwh91p4"
        self.headers = {
            "X-Application-TZ": "UTC",
            "X-BLOBR-KEY": "sCLMcPen12uk6iTKCz3EEhT7wUMSxuZc"
        }

    def get_weather(self, latitude, longitude, expected_code=200):
        url = f"{self.host}/{self.user_id}/hood/weather/{latitude}/{longitude}/"
        response = self.requests.get(url=url, headers=self.headers)
        assert response.status_code == expected_code, f"Actual response code: {response.status_code} doesn't match with expected: {expected_code}"
        if expected_code == 200:
            response_content = response.json()
            return response_content



