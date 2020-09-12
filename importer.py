import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import datetime
import json
import random


cred = credentials.Certificate('credentials.json')
default_app = firebase_admin.initialize_app(cred)
db = firestore.client()

doc_ref = db.collection(u'events')
paths = ['events']
today = datetime.datetime.now()
element_ids = []

for path in paths:
    event_files = os.listdir('data/' + path)
    for file in event_files:
        element_ref = db.collection(path).document
        event = open('data/' + path + '/' + file,'r')
        event_dict = json.load(event)
        start_offset = random.randint(0, 14)
        event_dict['start_time'] = (today + datetime.timedelta(days = start_offset)).isoformat()
        event_dict['end_time'] = (today + datetime.timedelta(days = random.randint(0, 14) + start_offset)).isoformat()
        element_ids.append(element_ref)

