import uuid

def generate_team_code():
    code = str(uuid.uuid4().int)[:8]
    return code