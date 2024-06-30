import uuid 

def generateID36():
    id = str(uuid.uuid4().int)
    return id
