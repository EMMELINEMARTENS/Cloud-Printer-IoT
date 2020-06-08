
#print [1,2], '\n', [3,4]
# CUPS' API
import sys
sys.path.insert(0,'../app/print')
import firebase_admin
from firebase_admin import credentials, firestore

# firebase
cred = credentials.Certificate("./config/key")
firebase_admin.initialize_app(cred)