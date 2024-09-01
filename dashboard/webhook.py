from flask import Flask, request, jsonify
import logging
from src.dataextraction import insert_data_to_db

app = Flask(__name__)


@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        data = request.json  # Get the incoming JSON data
        insert_data_to_db(data)  # Insert the data into the database
        return (
            jsonify({"status": "success", "message": "Data received and inserted"}),
            200,
        )
    except Exception as e:
        logging.error(f"Error in webhook: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
