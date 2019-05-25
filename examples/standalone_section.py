from flask import Flask
from section import Section

server = Flask(__name__)

app = Section(name="home", server=server, url_base_pathname="/")

if __name__ == "__main__":
    server.run(host="0.0.0.0")
