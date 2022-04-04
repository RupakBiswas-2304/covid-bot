# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

class ActionSymptoms(Action):
    def name(self) -> Text:
        return "action_symptoms"

    async def run(self,dispatcher, tracker : Tracker, domain : Dict[Text,Any],) -> List[Dict[Text,Any]]:
        fever = tracker.get_slot("fever")
        cough = tracker.get_slot("cough")
        cold = tracker.get_slot("cold")
        tiredness = tracker.get_slot("tiredness")
        loss_of_taste = tracker.get_slot("loss-of-taste")
        difficulty_in_breathing = tracker.get_slot("difficulty-in-breathing")
        chest_pain = tracker.get_slot("chest-pain")

        print(fever, cough, cold, tiredness, loss_of_taste, difficulty_in_breathing, chest_pain)
        lookup_table = [ fever, cough, cold, tiredness, loss_of_taste, difficulty_in_breathing, chest_pain]
        slots  = [ "fever", "cough", "cold", "tiredness", "loss-of-taste", "difficulty-in-breathing", "chest-pain"]
        
        score = 7
        print(type(difficulty_in_breathing))

        for i in lookup_table:
            if ( i == False):
                score =- 1
        
        if (score == 7):
            dispatcher.utter_message(text="You have high chances of having covid19 , please consult a doctor")
        elif (score >= 4 and score <= 6):
            dispatcher.utter_message(text="You have chances of having covid19 , please consult take rest, [medication comes here]")
        elif (score >= 1 and score <= 3):
            dispatcher.utter_message(text="You have low chances of having covid19 , please isolate your self and take rest")
        dispatcher.utter_message(text = "I don't think you may have covid19")
        return []