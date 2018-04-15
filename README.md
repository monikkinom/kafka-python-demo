# kafka-python-demo
Kafka Python Demo

## What does it do?
Different producers represent different sensors recording information about a certain activity. They provide coordinates about where they observed the activity. 

Different sensors have differing levels of accuracy and must be considered relatively when calculating the actual value. 

The Consumer consumes information from the 3 sensors and tries to accurately infer the correct coordinates of the object that is trying to be tracked. 

There can be cases where the real time information (which is accurate as possible) about the coordinates is required and this time sensivity may make wrong inferences expensive. In that case, we take a moving average of the reported coordinates and report updated information real time. Well by Strong Law of Large Numbers, these estimates will converge to the real values eventually! 

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

