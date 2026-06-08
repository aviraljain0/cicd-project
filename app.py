from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>🚀 CI/CD Pipeline — Version 2.0</h1>
    <p>This update was deployed <strong>automatically</strong> using:</p>
    <ul>
        <li>✅ GitHub Actions</li>
        <li>✅ Docker</li>
        <li>✅ AWS EC2</li>
    </ul>
    <p>No manual deployment was done!</p>
    """

@app.route("/health")
def health():
    return {"status": "healthy", "version": "2.0"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)