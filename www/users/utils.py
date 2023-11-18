import uuid
def generate_ref_code():
    code = str(uuid.uuid4()).replace('-','')[:12]
    return code

def generate_email_verification_token():
    code = str(uuid.uuid4().int)[:6]
    return code

def generate_sms_verification_token():
    code = str(uuid.uuid4().int)[:6]
    return code
