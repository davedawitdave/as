# dashboard/webhook.py

from flask import Flask, request, jsonify
import logging
from src.dataextraction import insert_data_to_db
from src.fetch_data import fetch_data_from_kobotoolbox
from src.config import API_URL, HEADERS

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)


@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        data = request.json
        if data:
            insert_data_to_db(data)
            logging.info(f"Received and processed {len(data)} records.")
            return jsonify({"message": "Data processed successfully!"}), 200
        else:
            logging.error("No JSON data found in the request.")
            return jsonify({"error": "No data provided"}), 400
    except Exception as e:
        logging.error(f"Error processing webhook data: {e}")
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
