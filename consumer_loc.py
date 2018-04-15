import json
from kafka import KafkaConsumer
consumer = KafkaConsumer('location')
for msg in consumer:
        info = json.loads(msg.value)
        print "estimated location:",info['x'],info['y'],'data_items:',info['len']
