# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import firestore
# from firebase_admin import storage

import cv2


# keyFile = 'aibigdata.json'

# storageBucket = 'aibigdata-107598064-271403.appspot.com'


# cred = credentials.Certificate(keyFile)

# firebase_admin.initialize_app(cred, {'storageBucket': storageBucket})

# client = firestore.client()

# bucket = storage.bucket()

# blob = bucket.blob('test/aibigdata.json')
# blob.upload_from_filename(keyFile)
# blob.make_public()



# db = firestore.client()

# db.collection('test').document().set({'aaa':123, 'bbb':222})




vc = cv2.VideoCapture('Sample.mp4')
num  = vc.get(cv2.CAP_PROP_FPS)
print(num)
ret , frame  = vc.read()
cv2.imwrite('test.png', frame)
for i in range(10):
    print(i * int(num))
    vc.set(1, int(num) * i)
    ret , frame  = vc.read()
    cv2.imwrite(str(i) + '.png', frame)
    
