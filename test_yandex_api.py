import requests
import pytest
import time
import os


TOKEN = os.getenv("YANDEX_TOKEN", "ТОКЕН_ЗДЕСЬ") 
HEADERS = {"Authorization": f"OAuth {TOKEN}"}
BASE_URL = "https://cloud-api.yandex.net/v1/disk/resources"

class TestYandexDiskAPI:

    def setup_method(self):
        self.folder_name = f"test_hw4_folder_{int(time.time())}"
        self.url_create = f"{BASE_URL}/?path=/{self.folder_name}"
        self.url_check = f"{BASE_URL}/?path=/{self.folder_name}"

    def teardown_method(self):
        delete_url = f"{BASE_URL}/?path=/{self.folder_name}&permanent=true"
        requests.delete(delete_url, headers=HEADERS)

    def test_create_folder_success(self):
        response_create = requests.put(self.url_create, headers=HEADERS)
        assert response_create.status_code in [200, 201], f"Ошибка создания: {response_create.text}"

        response_check = requests.get(self.url_check, headers=HEADERS)
        assert response_check.status_code == 200
        
        data = response_check.json()
        assert data["type"] == "dir", "Созданный объект не является папкой (dir)"
        assert data["name"] == self.folder_name, "Имя созданной папки не совпадает"

    def test_create_folder_without_token(self):
        headers_no_auth = {} 
        response = requests.put(self.url_create, headers=headers_no_auth)
        
        assert response.status_code == 401, "Доступ разрешился без токена, это ошибка!"

    def test_create_existing_folder(self):
        requests.put(self.url_create, headers=HEADERS)
        
        response = requests.put(self.url_create, headers=HEADERS)
        
        assert response.status_code == 409, f"Ожидалась ошибка 409, получено: {response.status_code}"