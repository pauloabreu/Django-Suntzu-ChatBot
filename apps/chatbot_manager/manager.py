from django.db import models
from nltk.chat.util import Chat
from apps.pair_messages.models import PairMessage
from apps.pairs.models import Pair
from apps.reflections.models import Reflection

class ChatBotManager():
    def respond(text):

        reflec = {item.key:item.value for item in Reflection.objects.all()}

        pairs = []

        pairs_query = Pair.objects.all()
        for pair_item in pairs_query:
            item = [pair_item.key]
            vals = []
            pair_message_query = PairMessage.objects.filter(pair=pair_item)
            for pair_message in pair_message_query:
                vals.append(pair_message.value)
            item.append(vals)
            pairs.append(item)

        #print(pairs)
            
        chat = Chat(pairs, reflec)
        msg = chat.respond(text)
        if msg == None:
            return "Sorry, I didn't catch that. Can you repeat it?"
        return msg