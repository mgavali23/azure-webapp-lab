from flask import Flask, jsonify
import os
from datetime import datetime, timezone

app = Flask(__name__)

@app.get("/")
def home():
    return """
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Azure App Service Lab</title>
        <style>
          body { font-family: Arial, sans-serif; max-width: 760px; margin: 60px auto; padding: 0 20px; color: #243247; }
          .card { padding: 28px; border-radius: 14px; background: #f2f6fc; }
          .tag { color: #087e55; font-weight: bold; }
        </style>
      </head>
      <body>
        <div class="card">
          <p class="tag">DEPLOYMENT SUCCESSFUL</p>
          <h1>Hello from Azure App Service!</h1>
          <p>This Python Flask application is running on Azure App Service.</p>
          <p>Use this lab to learn GitHub, GitHub Actions, CI/CD and Azure PaaS.</p>
          <p><a href="/health">Health endpoint</a></p>
        </div>
      </body>
    </html>
    """

@app.get("/health")
def health():
    return jsonify(
        status="healthy",
        application="azure-webapp-lab",
        environment=os.getenv("APP_ENV", "learning"),
        utc_time=datetime.now(timezone.utc).isoformat()
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "8000")))
