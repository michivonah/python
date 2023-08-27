from flask import Flask, request, jsonify, redirect

app = Flask(__name__)

@app.route("/hello")
def helloWorld():
    return "Hello World"

@app.route("/<slug>")
def shortUrl(slug):
    #return f"This is a short url! Your slug: {slug}"
    destination = f"https://www.google.com/search?q={slug}"
    return redirect(destination, code=302)

if __name__ == "__main__":
    app.run(debug=True)