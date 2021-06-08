from flask import Flask, render_template, request, url_for
app= Flask(__name__)

@app.route('/')
def index():
   return render_template("index.html")

@app.route('/ct')
def ct():
   return render_template("ct.html")

@app.route('/result')
def result():
   return render_template("result.html")

@app.route('/map')
def map():
   return render_template("map.html")

@app.route('/news')
def news():
   return render_template("news.html")


if __name__ == "__main__":
   app.run(debug=True)