from src.dataextraction import insert_data_to_db
from src.models import SurveyData

# Assuming you have a function to fetch data
data = [
    {
        "_id": 1,
        "formhub/uuid": "12345",
        "starttime": "2024-08-29T08:00:00",
        "endtime": "2024-08-29T09:00:00",
        "cd_survey_date": "2024-08-29",
        "sec_a/unique_id": "ABC123",
        "sec_a/cd_biz_country_name": "CountryX",
        # More fields as needed
    }
]

insert_data_to_db(data)
