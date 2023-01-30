# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
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

import datetime as dt
from typing import Any, Text, Dict, List
import json

from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.events import AllSlotsReset, SlotSet, Restarted
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_show_reports1"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text=f"{dt.datetime.now()}")
        GetToken()

        return []

class ActionRestarted(Action):
    def name(self):
        return 'action_restarted'

    def run(self, dispatcher, tracker, domain):
        return [Restarted()]


class ActionSlotReset(Action):
    def name(self):
        return 'action_slot_reset'

    def run(self, dispatcher, tracker, domain):
        return [AllSlotsReset()]


class ActionRenew(Action):
    def name(self):
        return 'action_renew'

    def run(self, dispatcher, tracker, domain):
        return_slots = []
        for slot in tracker.slots:
            if slot != "foo":
                return_slots.append(SlotSet(slot, None))
        return return_slots
