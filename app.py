from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to my Flask App on Render!</h1><p>Deployed using Render's free hosting service.</p>"

if __name__ == "__main__":
    app.run(debug=True)
