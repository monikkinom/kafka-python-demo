# kafka-python-demo
Kafka Python Demo

## To setup
Install the required library
`pip install kafka-python`

Create the topics

`bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic sensors`

`bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic location`

Once the topics are ready, launch each file in a new terminal tab. To start all of the producers, simply do:

`python producer1.py & python producer2.py & python producer3.py`

To read, run `python consumer.py` in one tab and `python consumer_loc.py` in the other. 

Once all the producers and consumers are running, you will begin to the see the calculated coordinates on consumers_loc.py

