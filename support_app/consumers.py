import json
from time import sleep
from random import randint
from threading import Thread
from channels.generic.websocket import WebsocketConsumer
from support_app.core.event_tracer import EventTracer, StatsCollector
from support_app.core.user_interaction import UserInteraction

class QueryWebSocketConsumer(WebsocketConsumer):
    tracer = None
    stats_collector = None

    def connect(self):
        self.accept()
        self.tracer = EventTracer()
        self.stats_collector = StatsCollector()
        event_pusher = EventPusher(consumer=self, tracer=self.tracer)
        event_pusher.start()

    def disconnect(self, close_code):
        print('home websocket closed')

    # This function receive messages from WebSocket.
    def receive(self, text_data):
        query_data_json = json.loads(text_data)
        user_id = query_data_json["user_id"]
        user_query = query_data_json["user_query"]
        user_interaction = UserInteraction(user=user_id,
                                           uquery=user_query)
        expert_answer = user_interaction.get_answer(
            tracer=self.tracer,
            stats_collector=self.stats_collector)
        message = {
                'type' : 'Answer',
                'message': f"{expert_answer}"
            }
        self.send(json.dumps(message))
        stats = self.stats_collector.collectReset()
        self.send(json.dumps({'type': 'Stats', 'message' : stats}))

class EventPusher(Thread) :

    def __init__(self,
                 consumer : QueryWebSocketConsumer,
                 tracer : EventTracer) :
        super(EventPusher, self).__init__()
        self.consumer = consumer
        self.tracer = tracer

    def run(self) :
        try :
            while True :
                trace = self.tracer.get_trace(timeout=1)
                message = {
                    'type' : 'Trace',
                    'message': trace
                }
                self.consumer.send(json.dumps(message))
                sleep(1)
        except Exception as e :
            print(e)
