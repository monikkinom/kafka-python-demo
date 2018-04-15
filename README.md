# kafka-python-demo
Kafka Python Demo

## To setup
Install the required library
`pip install kafka-python`

Create the topics
`bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic sensors`

`bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic location`

Once the topics are ready, launch each file in a new terminal tab. To start any one of the files, simply do:

`python producer1.py`

Once all the producers and consumers are running, you will begin to the see the calculated coordinates inferred from consumers_loc.py

