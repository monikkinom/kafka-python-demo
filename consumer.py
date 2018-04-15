import json
from kafka import KafkaConsumer,KafkaProducer
results = [0.0,0.0]
elems = 0
consumer = KafkaConsumer('sensors')
producer = KafkaProducer(value_serializer=lambda v: json.dumps(v).encode('utf-8'))
for msg in consumer:
        info = json.loads(msg.value)
        if info['from'] == 'sensor 1':
                c = 1
        elif info['from'] == 'sensor 2':
                c = 0.5
        elif info['from'] == 'sensor 3':
                c = 0.3
        results[0] = (elems*results[0] + c*float(info['x']))/(elems+c)
        results[1] = (elems*results[1] + c*float(info['y']))/(elems+c)
        elems+=1
        producer.send('location',{'x':str(1/results[0]),'y':str(1/results[1]*1.0),'len':str(elems)})
