


import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials

listPlate = []
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
result = db.collection("reservation").get()
for  i in result:
    #print(i.to_dict()["plate_number"])
    listPlate.append(i.to_dict()["plate_number"])
    print(listPlate)
plate="123"
if plate in listPlate:
    print("exist")
else:
    print("not exist")




