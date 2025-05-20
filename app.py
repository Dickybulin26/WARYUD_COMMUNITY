from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello, World!</h1>"

@app.route("/halaman2", defaults={"nilai": 0, '_route': 'halaman1'})
@app.route("/halaman2/<int:nilai>", defaults={'_route': 'halaman2'})
def halaman2(nilai, _route):
    if _route == 'halaman1':
        return "<h1>Hello, World!</h1>"
    elif _route == 'halaman2':
        nilai = nilai + 100
        #* return "<h1>Hello, " + nilai + "</h1>"
        #* return "<h1>Hello, %s!</h1>" % nilai

        return f"<h1>Hello, {nilai}</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2025, debug=True)