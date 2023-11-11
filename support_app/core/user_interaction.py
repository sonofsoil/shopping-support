from queue import Queue
from support_app.core.event_tracer import EventTracer
from support_app.core.order_query_expert import answer_order_query

class UserInteraction():
    user_id : str = ''
    user_query : str = ''
    expert_answer : str = ''

    def __init__(self, user : str, uquery : str, eanswer : str = None) :
        self.user_id = user
        self.user_query = uquery
        self.expert_answer = eanswer

    def get_answer(self, tracer : EventTracer) :
        if self.user_query:
            self.expert_answer = answer_order_query(
                user_id=self.user_id,
                user_query=self.user_query,
                tracer=tracer)
        return self.expert_answer
