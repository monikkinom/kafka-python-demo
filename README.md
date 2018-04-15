# kafka-python-demo
Kafka Python Demo

## To setup
Install the required library
`pip install kafka-python`

Create the topics
`bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic sensors`
`bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic location`


