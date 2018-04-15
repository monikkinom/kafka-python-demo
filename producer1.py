import json,time
from kafka import KafkaProducer
import numpy as np
mu = 1/np.pi
sigma = 4
producer = KafkaProducer(value_serializer=lambda v: json.dumps(v).encode('utf-8'))
while True:
        producer.send('sensors', {'from': 'sensor 1','x':str(np.random.normal(mu, sigma)),
        'y':str(np.random.normal(mu, sigma))}))
