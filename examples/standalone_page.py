from flask import Flask
from page import Page1

server = Flask(__name__)

app = Page1(name="home", server=server, url_base_pathname="/")

if __name__ == "__main__":
    server.run(host="0.0.0.0")
