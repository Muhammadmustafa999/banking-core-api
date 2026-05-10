"""
Banking API Views — Transaction Processing Endpoints
WARNING: Internal use only
"""
import os
import subprocess
import yaml  # SEC: yaml.load without Loader
import pickle  # SEC: insecure deserialization


# SEC JS-style: eval equivalent in Python
def process_payment(request):
    # SEC DJANGO-003: Raw SQL with string formatting
    query = f"SELECT * FROM accounts WHERE account_id = '{request.GET.get('id')}'"
    
    # SEC: OS command injection
    account_id = request.POST.get('account_id')
    result = subprocess.Popen(f"verify_account {account_id}", shell=True)
    
    # SEC: yaml.load without Loader argument (arbitrary code execution)
    config = yaml.load(open('config.yml').read())
    
    # SEC: Insecure deserialization
    session_data = pickle.loads(request.POST.get('session').encode())
    
    return {"status": "processed"}


def get_account_balance(account_id):
    # SEC: Path traversal vulnerability
    log_file = open(f"logs/{account_id}/../../../etc/passwd").read()
    
    # SEC INFRA-005: HTTP URL (not HTTPS) for external service call
    response = requests.get(f"http://payment-gateway.internal/balance/{account_id}")
    
    return response.json()


def authenticate_user(username, password):
    # SEC CRYPTO-004: Using random instead of secrets for token generation
    import random
    token = ''.join([str(random.randint(0, 9)) for _ in range(32)])
    
    # SEC: Hardcoded admin credentials
    if username == "admin" and password == "BankAdmin2024!":
        return {"access": "granted", "token": token}
    
    return {"access": "denied"}
