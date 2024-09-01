from fastapi import FastAPI, Request, HTTPException
from src.dataextraction import insert_data_to_db
import logging

app = FastAPI()

@app.post("/webhook")
async def webhook(request: Request):
    try:
        data = await request.json()  # Get the incoming JSON data
        insert_data_to_db(data)  # Insert the data into the database
        return {"status": "success", "message": "Data received and inserted"}
    except Exception as e:
        logging.error(f"Error in webhook: {e}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
