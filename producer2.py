import json,time
from kafka import KafkaProducer
import numpy as np
mu = 1/np.pi
sigma = 4
producer = KafkaProducer(value_serializer=lambda v: json.dumps(v).encode('utf-8'))
while True:
        time.sleep(1)
        producer.send('sensors', {'from': 'sensor 2','x':str(np.random.normal(mu, sigma)),
        'y':str(np.random.normal(mu, sigma))})
