 export  PYTHONPATH="./";
#PYTHONPATH

#ack demo 
python collecter/rabbitmq/producer.py
python collecter/rabbitmq/consumer.py

#msg demo 
python collecter/rabbitmq/producer_msg.py
python collecter/rabbitmq/consumer_msg.py
