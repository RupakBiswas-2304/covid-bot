# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from .utility import *
from rasa_sdk.events import SlotSet

male = ["father","brother", "husband","friend", "son"]
female = ["mother", "sister", "wife", "girlfriend","daughter"]


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
        
        relative = tracker.get_slot("relative")
        # print(relative, type(relative))

        x = ""
        if relative in male:
            x = "He"
        elif relative in female : 
            x = "She"
        else :
            x = "You"

        if (score == 7):
            dispatcher.utter_message(text=f"{x} have high chances of having covid19 , please consult a doctor")
        elif (score >= 4 and score <= 6):
            dispatcher.utter_message(text=f"{x} have chances of having covid19 , please consult take rest, [medication comes here]")
        elif (score >= 1 and score <= 3):
            dispatcher.utter_message(text=f"{x} have low chances of having covid19 , please isolate your self and take rest")
        else :
            dispatcher.utter_message(text = f"I don't think {x} may have covid19")
        return []

class AskForCoughAction(Action):
    def name(self) -> Text:
        return "action_ask_symptoms_form_cough"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict):

        relative = tracker.get_slot("relative")
        print(relative, type(relative))
        # male = ["father","brother", "husband","friend"]
        # female = ["mother", "sister", "wife", "girlfriend"]
        msgs = []
        if (relative != None):
            msgs = [
                f"Does your {relative} have cough ?",
                f"Do your {relative} have cough also ?",
            ]
        more_msgs = []
        if (relative in female):
            more_msgs = [
                f"Is she feeling any kind of cough ?",
                f"She have cough ?",
                f"Does she have cough ?"
            ]
        elif (relative in male):
            more_msgs = [
                f"Is he feeling any kind of cough ?",
                f"He have cough ?",
                f"Does he have cough ?"
            ]
        else :
            more_msgs = [
                f"Do you have cough also ?",
                "Do you have any kind of cough?",
                "Are you feeling any kind of cough?"
            ]
        msgs = msgs + more_msgs
        print(msgs)

        dispatcher.utter_message(text=random_string(msgs))
        return []

'''
-----------------------CUSTOM ACTION FOR ASKING SLOTS FOR Cold-------------------


'''
class AskForColdAction(Action):
    def name(self) -> Text:
        return "action_ask_symptoms_form_cold"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict):

        relative = tracker.get_slot("relative")
        print(relative, type(relative))
        # male = ["father","brother", "husband","friend"]
        # female = ["mother", "sister", "wife", "girlfriend"]
        msgs = []
        if (relative != None):
            msgs = [
                f"Does your {relative} have cold ?",
                f"Do your {relative} have cold also ?",
            ]
        more_msgs = []
        if (relative in female):
            more_msgs = [
                f"Is she feeling any kind of cold ?",
                f"She have cold ?",
                f"Does she have cold ?"
            ]
        elif (relative in male):
            more_msgs = [
                f"Is he feeling any kind of cold ?",
                f"He have cold ?",
                f"Does he have cold ?"
            ]
        else :
            more_msgs = [
                f"Do you have cold also ?",
                "Do you have any kind of cold?",
                "Are you feeling any kind of cold?"
            ]
        msgs = msgs + more_msgs
        print(msgs)

        dispatcher.utter_message(text=random_string(msgs))
        return []

# ---------------------------- ASK FOR COLD CUSTOM ACTION---------------------

class AskForFeverAction(Action):
    def name(self) -> Text:
        return "action_ask_symptoms_form_fever"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict):

        relative = tracker.get_slot("relative")
        print(relative, type(relative))
        # male = ["father","brother", "husband","friend"]
        # female = ["mother", "sister", "wife", "girlfriend"]
        msgs = []
        if (relative != None):
            msgs = [
                f"Does your {relative} have fever ?",
                f"Do your {relative} have fever also ?",
            ]
        more_msgs = []
        if (relative in female):
            more_msgs = [
                f"Is she feeling any kind of fever ?",
                f"She have fever ?",
                f"Does she have fever ?"
            ]
        elif (relative in male):
            more_msgs = [
                f"Is he feeling any kind of fever ?",
                f"He have fever ?",
                f"Does he have fever ?"
            ]
        else :
            more_msgs = [
                f"Do you have cough fever ?",
                "Do you have any kind of fever?",
                "Are you feeling any kind of fever?"
            ]
        msgs = msgs + more_msgs
        print(msgs)

        dispatcher.utter_message(text=random_string(msgs))
        return []

# - ---------------------------------- Custom ask function for Tiredness ------------------------------- 

class AskForTirednessAction(Action):
    def name(self) -> Text:
        return "action_ask_symptoms_form_tiredness"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict):

        relative = tracker.get_slot("relative")
        print(relative, type(relative))
        # male = ["father","brother", "husband","friend"]
        # female = ["mother", "sister", "wife", "girlfriend"]
        msgs = []
        if (relative != None):
            msgs = [
                f"Does your {relative} feeling tiredness ?",
                f"Do your {relative} feeling tired ?",
            ]
        more_msgs = []
        if (relative in female):
            more_msgs = [
                f"Is she feeling tired ?",
                f"She is tired ?",
                f"Does she have tiredness?"
            ]
        elif (relative in male):
            more_msgs = [
                f"Is he feeling tired ?",
                f"He have tiredness ?",
                f"is he tired ?"
            ]
        else :
            more_msgs = [
                f"Do you have tiredness ?",
                "Are you feeling tired",
                "Are you feeling any kind of tiredness?"
            ]
        msgs = msgs + more_msgs
        print(msgs)

        dispatcher.utter_message(text=random_string(msgs))
        return []

# -----------------------------CHEST PAIN CUSTOM SLOT---------------------------------

class AskForChestpainAction(Action):
    def name(self) -> Text:
        return "action_ask_symptoms_form_chest-pain"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict):

        relative = tracker.get_slot("relative")
        print(relative, type(relative))
        # male = ["father","brother", "husband","friend"]
        # female = ["mother", "sister", "wife", "girlfriend"]
        msgs = []
        if (relative != None):
            msgs = [
                f"Does your {relative} have chest pain ?",
                f"Do your {relative} have chest pain also ?",
            ]
        more_msgs = []
        if (relative in female):
            more_msgs = [
                f"Is she feeling any kind of pain in chest ?",
                f"She have chest-pain ?",
                f"Does she have chest-pain ?"
            ]
        elif (relative in male):
            more_msgs = [
                f"Is he feeling any kind of pain in chest ?",
                f"He have chest-pain ?",
                f"Does he have chest pain ?"
            ]
        else :
            more_msgs = [
                f"Do you have Chestpain also ?",
                "Do you have any kind of pain in chest?",
                "Are you feeling any kind of chest pain?"
            ]
        msgs = msgs + more_msgs
        print(msgs)

        dispatcher.utter_message(text=random_string(msgs))
        return []

#-------------------------------loss of taste--------------------------------

class AskForLossOfTasteAction(Action):
    def name(self) -> Text:
        return "action_ask_symptoms_form_loss-of-taste"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict):

        relative = tracker.get_slot("relative")
        print(relative, type(relative))
        # male = ["father","brother", "husband","friend"]
        # female = ["mother", "sister", "wife", "girlfriend"]
        msgs = []
        if (relative != None):
            msgs = [
                f"Does your {relative} lossed taste ?",
                f"Do your {relative} have loss of taste also ?",
            ]
        more_msgs = []
        if (relative in female):
            more_msgs = [
                f"Is she loosing taste ?",
                f"She have losse of taste ?",
                f"And she is not feeling any tast ?"
            ]
        elif (relative in male):
            more_msgs = [
                f"Is he loosing taste ?",
                f"He have losse of taste ?",
                f"And he is not feeling any tast ?"
            ]
        else :
            more_msgs = [
                f"Do you have loss of taste also ?",
                "Do you have lossed your taste ?",
                "You are not getting any taste, right ?"
            ]
        msgs = msgs + more_msgs
        print(msgs)

        dispatcher.utter_message(text=random_string(msgs))
        return []

# ------------------------- difficulty in breathing ---------------------------------

class AskForDifficultyInBreathingAction(Action):
    def name(self) -> Text:
        return "action_ask_symptoms_form_difficulty-in-breathing"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict):

        relative = tracker.get_slot("relative")
        print(relative, type(relative))
        # male = ["father","brother", "husband","friend"]
        # female = ["mother", "sister", "wife", "girlfriend"]
        msgs = []
        if (relative != None):
            msgs = [
                f"Does your {relative} difficulty i breathing ?",
                f"Do your {relative} is facing difficulty in breathing also ?",
            ]
        more_msgs = []
        if (relative in female):
            more_msgs = [
                f"Is she facing difficulty in breathing ?",
                f"She have breathing problem also?",
                f"She if suffering in breathing also ?"
            ]
        elif (relative in male):
            more_msgs = [
                f"Is he  facing difficulty in breathing?",
                f"He have breathing problem also? ?",
                f"He if suffering in breathing also ?"
            ]
        else :
            more_msgs = [
                f"Do you have difficulty in breathing ?",
                "Are you facing difficulty in breathing ?",
                "You can not breath properly, right?"
            ]
        msgs = msgs + more_msgs
        print(msgs)

        dispatcher.utter_message(text=random_string(msgs))
        return []

# reset slot for symptoms
class ResetSlot(Action):

    def name(self):
        return "action_reset_slot"

    def run(self, dispatcher, tracker, domain):
        return [SlotSet("fever", None),
                SlotSet("cold", None),
                SlotSet("cough", None),
                SlotSet("tiredness", None),
                SlotSet("loss-of-taste", None),
                SlotSet("difficulty-in-breathing", None),
                SlotSet("loss-of-taste", None),
                SlotSet("chest-pain", None),
                # SlotSet("relative", None),
                ]