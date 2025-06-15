from flask import Flask
import threading
import os
import run  # run.py must have a function called run_bot()

app = Flask(__name__)

@app.route("/")
def home():
    return "🤖 Bot is alive and running on Render!"

# Start the Telegram bot in a separate thread
threading.Thread(target=run.run_bot).start()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f"Starting Flask app on port {port}")
    app.run(host="0.0.0.0", port=port)
