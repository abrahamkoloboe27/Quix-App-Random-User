from quixstreams import Application
from quixstreams.kafka.configuration import ConnectionConfig

# Configuration de la connexion
connection = ConnectionConfig(
    bootstrap_servers='localhost:9092', 
    security_protocol="PLAINTEXT"  
    )

print(connection)
# Initialiser l'application Quix avec la configuration de connexion
try:
    app = Application(broker_address=connection)
except Exception as e:
    print(e)

# Spécifiez le topic auquel vous souhaitez produire des messages
topic_name = 'user_created'  # Remplacez par le nom de votre topic
topic = app.topic(topic_name, value_deserializer='json')
output = app.topic(name="get_data", value_deserializer='json')
sdf = app.dataframe(output)

if __name__ == "__main__":
    app.run(sdf)
