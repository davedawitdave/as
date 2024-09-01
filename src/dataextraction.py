# src/dataextraction.py

import logging
from src.models import SurveyData, Session
from src.dataextraction import fetch_data_from_kobotoolbox


def insert_data_to_db(data):
    session = Session()
    try:
        for record in data:
            survey_entry = SurveyData(
                id=record.get("_id"),
                uuid=record.get("formhub/uuid"),
                start_time=record.get("starttime"),
                end_time=record.get("endtime"),
                survey_date=record.get("cd_survey_date"),
                unique_id=record.get("sec_a/unique_id"),
                country_name=record.get("sec_a/cd_biz_country_name"),
                region_name=record.get("sec_a/cd_biz_region_name"),
                bda_name=record.get("sec_b/bda_name"),
                cohort=record.get("sec_b/cd_cohort"),
                program=record.get("sec_b/cd_program"),
                client_name=record.get("sec_c/cd_client_name"),
                client_id_manifest=record.get("sec_c/cd_client_id_manifest"),
                location=record.get("sec_c/cd_location"),
                phone=record.get("sec_c/cd_clients_phone"),
                phone_smart_feature=record.get("sec_c/cd_clients_phone_smart_feature"),
                gender=record.get("sec_c/cd_gender"),
                age=record.get("sec_c/cd_age"),
                nationality=record.get("sec_c/cd_nationality"),
                strata=record.get("sec_c/cd_strata"),
                disability=record.get("sec_c/cd_disability") == "Yes",
                education=record.get("sec_c/cd_education"),
                client_status=record.get("sec_c/cd_client_status"),
                sole_income_earner=record.get("sec_c/cd_sole_income_earner") == "Yes",
                responsible_people=record.get("sec_c/cd_howrespble_pple"),
                business_status=record.get("group_mx5fl16/cd_biz_status"),
                biz_operating=record.get("group_mx5fl16/bd_biz_operating") == "yes",
                submission_time=record.get("_submission_time"),
                geolocation=str(record.get("_geolocation")),
            )
            session.add(survey_entry)
        session.commit()
        logging.info(f"Successfully inserted {len(data)} records into the database.")
    except Exception as e:
        logging.error(f"Error inserting data: {e}")
        session.rollback()
    finally:
        session.close()


# Example usage
if __name__ == "__main__":

    api_url = (
        "https://kf.kobotoolbox.org/api/v2/assets/aW9w8jHjn4Cj8SSQ5VcojK/data.json"
    )
    headers = {"Authorization": "Token your_token_here", "Cookie": "django_language=en"}
    data = fetch_data_from_kobotoolbox(api_url, headers)
    insert_data_to_db(data)
