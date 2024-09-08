from datetime import datetime
import json
import requests
import uuid
import logging
from kafka import KafkaProducer
from airflow import DAG
from airflow.operators.python import PythonOperator
import time

# Setup logging
logging.basicConfig(level=logging.INFO)

# Default arguments for the DAG
default_args = {
    'owner': 'airscholar',
    'start_date': datetime(2024, 9, 7, 10, 37),
    'retries': 1,  # Define retry behavior
    'retry_delay': timedelta(minutes=5)  # Delay between retries
}

# Function to fetch the user data from the API
def get_data():
    try:
        # Fetching data from the API
        response = requests.get("https://randomuser.me/api/")
        response.raise_for_status()  # Raises an error for bad responses (4xx or 5xx)

        # Parsing the JSON response
        data = response.json()

        # Extracting the first result from the API response
        user_data = data['results'][0]

        return user_data

    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching data: {e}")
        return None

# Function to format the fetched user data
def format_data(user_data):
    if not user_data:
        return {}

    data = {}
    location = user_data['location']
    
    data['id'] = str(uuid.uuid4())  # Generating a unique ID
    data['first_name'] = user_data['name']['first']
    data['last_name'] = user_data['name']['last']
    data['gender'] = user_data['gender']
    data['address'] = f"{location['street']['number']} {location['street']['name']}, " \
                      f"{location['city']}, {location['state']}, {location['country']}"
    data['post_code'] = location['postcode']
    data['email'] = user_data['email']
    data['username'] = user_data['login']['username']
    data['dob'] = user_data['dob']['date']
    data['registered_date'] = user_data['registered']['date']
    data['phone'] = user_data['phone']
    data['picture'] = user_data['picture']['medium']

    return data

# Function to stream the data and send it to Kafka
def stream_data():
    # Fetch the user data
    user_data = get_data()
    
    # Format the user data
    formatted_data = format_data(user_data)

    # Print the formatted data as JSON
    # print(json.dumps(formatted_data, indent=3))
    
    producer = KafkaProducer(bootstrap_servers=['broker:29092'], max_block_ms=5000)

    # Push data to message queue
    producer.send('user_created', json.dumps(formatted_data).encode('utf-8'))

    curr_time = time.time()

    while True:
        if time.time() > curr_time + 60:  # 1 minute
            break
        try:
            res = get_data()
            formatted_res = format_data(res)
            producer.send('users_created', json.dumps(formatted_res).encode('utf-8'))
        except Exception as e:
            logging.error(f'An error occurred: {e}')
            continue

# Define the DAG
with DAG('user_automation',
         default_args=default_args,
         schedule_interval='@daily',
         catchup=False) as dag:

    streaming_task = PythonOperator(
        task_id='stream_data_from_api',
        python_callable=stream_data
    )

# For local testing
if __name__ == '__main__':
    stream_data()
