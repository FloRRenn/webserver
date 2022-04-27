import requests

url = 'http://127.0.0.1:5000/upload'
params = {
    "file" : open(r".\test_image.jpg", "rb"),
}

resp = requests.post(url, files = params, data = {"username" : "abcdef", "password" : "12345"})
print(resp.status_code)

