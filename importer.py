import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import datetime
import json
import random
import string


cred = credentials.Certificate('credentials.json')
default_app = firebase_admin.initialize_app(cred)
db = firestore.client()

doc_ref = db.collection(u'events')
paths = ['events']

element_ids = []

def get_random_alphanumeric_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join((random.choice(letters_and_digits) for i in range(length)))

event_dict = open('all.json','r')
event_dict = json.load(event_dict)

start = datetime.datetime.now()
print (start)

i = 0
for event in event_dict:
    event['name'] = "[imported] " + str(event['name'])
    key = event['id']
    element_ref = doc_ref.document(key)
    element_ref.set(event)
    element_ids.append(key)
    print ("Added ID: " + key)
    i += 1

print ("Uploaded " + str(i) + " elements in " + str(datetime.datetime.now()- start) + ".")

