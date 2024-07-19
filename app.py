from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/tools")
def tools():
    return render_template("tools.html")
@app.route("/certificates")
def certificates():
    return render_template("certificates.html")

if __name__=="__main__":
    app.run(debug=True)