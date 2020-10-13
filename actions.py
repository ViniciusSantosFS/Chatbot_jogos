# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List, Union
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.forms import FormAction

class jogoForm(FormAction):
    def name(self):
        return "jogoForm"

    @staticmethod
    def required_slots(tracker):
        return ["jogo"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
                "jogo": [#self.from_intent(intent = "confirmar_pedido", value = True),
                         #self.from_intent(intent = "solicitar", value = True),
                         self.from_entity(entity= "jogo")]
        }
    def submit(self,
               dispatcher:CollectingDispatcher,
               tracker: Tracker,
               doamin: Dict[Text, Any]) -> List[Dict]:

        dispatcher.utter_message("")
        return[]


class nomeForm(FormAction):
    def name(self):
        return "nomeForm"

    @staticmethod
    def required_slots(tracker):
        return ["nome"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
                "nome": [self.from_intent(intent = "nome", value = True),
                         self.from_entity(entity= "nome")]

        }
    def submit(self,
               dispatcher:CollectingDispatcher,
               tracker: Tracker,
               doamin: Dict[Text, Any]) -> List[Dict]:

        dispatcher.utter_message("")
        return[]



#class Actionjogos(Action):
    #def name(self) -> Text:
     #   return "action_jogos"

   # def run(self, dispatcher: CollectingDispatcher,
      #      tracker: Tracker,
     #       domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
      #  jogos = tracker.get_slot("jogo")
     #   nome_jogo = "God of war 2"
     #   dispatcher.utter_message(text="Aqui esta o jogo {}:{}".format(nome_jogo,jogos))
     #   return[SlotSet("jogo", nome_jogo)]


#class Action_num_nalista(Action):
 #   def name(self) -> Text:
  #      return "action_num_nalista"

#    def run(self, dispatcher: CollectingDispatcher,
 #           tracker: Tracker,
  #          domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
   #     num_lista = tracker.get_slot("num_na_lista")
    #    num = "1"
     #   dispatcher.utter_message(text="O número é {}:{}".format(num_lista,num))
      #  return[SlotSet("num_na_lista", num)]