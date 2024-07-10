from kafka import KafkaConsumer, KafkaProducer
import json
from collections import defaultdict
from datetime import datetime, timedelta

# Initialize data structures for insights
device_type_count = defaultdict(int)
app_version_count = defaultdict(int)
user_logins = defaultdict(list)
locale_frequency = defaultdict(int)

# Time window for unusual login detection (e.g., 5 minutes)
TIME_WINDOW = timedelta(minutes=5)   # Can be picked from environment variable

def process_data(data):
    global device_type_count, app_version_count, user_logins, locale_frequency
    
    # Count logins by device type and app version
    device_type_count[data['device_type']] += 1
    app_version_count[data['app_version']] += 1
    
    # Analyze login frequency by locale
    locale_frequency[data['locale']] += 1
    
    # Identify unusual login patterns
    current_time = datetime.fromtimestamp(int(data['timestamp']))
    user_id = data['user_id']
    user_logins[user_id].append((current_time, data['ip']))
    
    # Remove old login records outside the time window
    user_logins[user_id] = [(t, ip) for t, ip in user_logins[user_id] if current_time - t <= TIME_WINDOW]
    
    # Check for unusual login patterns
    unusual_login = False
    if len(user_logins[user_id]) > 1:
        ips = set(ip for _, ip in user_logins[user_id])
        if len(ips) > 1:
            unusual_login = True
    
    # Add processed information to the data
    data['processed'] = True
    data['unusual_login'] = unusual_login
    
    # Generate insights
    insights = {
        'device_type_count': dict(device_type_count),
        'app_version_count': dict(app_version_count),
        'locale_frequency': dict(locale_frequency),
        'unusual_login_detected': unusual_login
    }
    
    return data, insights

consumer = KafkaConsumer(
    'user-login',   # Can be picked from environment variable
    bootstrap_servers='localhost:29092',   # Can be picked from environment variable
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

producer = KafkaProducer(
    bootstrap_servers='localhost:29092',   # Can be picked from environment variable
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

for message in consumer:
    try:
        data = message.value
        processed_data, insights = process_data(data)
        
        # Send processed data to the new topic
        producer.send('processed-user-login', value=processed_data)    # Can be picked from environment variable
        
        # Send insights to a separate topic
        producer.send('user-login-insights', value=insights)   # Can be picked from environment variable
        
        # Print insights for demonstration (you may want to remove this in production)
        print(f"Processed data: {processed_data}")
        print(f"Insights: {insights}")
        print("---")
    
    except Exception as e:
        print(f"Error processing message: {e}")