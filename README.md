# Demo Web Server
Demo cách hoạt động của 1 web server với các method POST, GET

# Cài đặt
```css
Cài đặt môi trường python (https://www.python.org/)
```
**Cài đặt thư viện**
```bash
Flask==2.0.2
Flask-Cors==3.0.10
Pillow==8.3.1
click==8.0.1
gunicorn==20.1.0
itsdangerous==2.0.1
Jinja2==3.0.1
jinja2-time==0.2.0
MarkupSafe==2.0.1
SQLAlchemy==1.3.17
Werkzeug==2.0.1
pymongo==3.12.0
```

# Cách dùng
1. Chạy file server.py để khởi tạo server.
2. Url của server sẽ là `http://__IP__:__PORT__/`
3. Sử dụng với cách đường dẫn như sau
   + **Tạo ảnh meme (method POST/GET)**
      - `/10guy?top=....&bottom=....`
      - `/alien?top=....&bottom=....`
      - `/button?top=....&bottom=....`
      
   + **Upload ảnh lên database (method POST)**
      - `/upload`, Xem ví dụ trong `/test/test_request.py`
   
   + **Lấy ảnh từ database và thể hiện trên trình duyệt**
      - `/getfile?username=....&password=.....&file=.....`
