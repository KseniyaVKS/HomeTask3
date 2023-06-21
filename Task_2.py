import requests
class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        params = {
            "path": path_to_file.split('\\')[-1]
        }
        headers = {
            "Authorization": token
        }
        response = requests.get(url, headers=headers, params=params)
        url_for_upload = response.json().get('href', '')
        with open(path_to_file, 'rb') as f:
            response2 = requests.put(url_for_upload, files={"file": f})

if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя:
    path_to_file = input("Введите путь к файлу: ")
    token = input("Введите токен: ")
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)