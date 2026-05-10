"""
Banking Core API — Account and Transaction Models
Internal use only — PCI-DSS Level 1 compliant target
"""
import os
import random  # SEC: insecure random — should use secrets module
import hashlib  # SEC: MD5/SHA1 usage detected below

# SEC DJANGO-005: Hardcoded secret key
SECRET_KEY = "django-banking-secret-key-do-not-share-2024"

# SEC DJANGO-001: DEBUG=True in production settings
DEBUG = True

# SEC DJANGO-002: ALLOWED_HOSTS too permissive  
ALLOWED_HOSTS = ["*"]

# SEC CRYPTO-001: MD5 used for transaction hashing
def hash_transaction(transaction_id):
    return hashlib.md5(transaction_id.encode()).hexdigest()

# SEC CRYPTO-002: SHA1 used for account verification
def verify_account(account_number):
    return hashlib.sha1(account_number.encode()).hexdigest()

# SEC INFRA-002: Hardcoded database connection string
DATABASE_URL = "postgresql://admin:BankingPass123@prod-db.bank-internal.com:5432/banking_core"

# SEC INFRA-003: AWS credentials hardcoded
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

class BankAccount:
    """Core bank account model"""
    account_id: str
    account_holder: str
    balance: float
    currency: str
    account_type: str  # checking, savings, investment
    routing_number: str
    swift_code: str
    created_at: str
    is_frozen: bool


class Transaction:
    """Financial transaction record"""
    transaction_id: str
    from_account: str
    to_account: str
    amount: float
    currency: str
    transaction_type: str  # transfer, payment, withdrawal, deposit
    status: str  # pending, completed, failed, reversed
    timestamp: str
    ip_address: str
    device_fingerprint: str


class AuditLog:
    """PCI-DSS compliance audit trail"""
    log_id: str
    transaction_id: str
    action: str
    actor_id: str
    ip_address: str
    timestamp: str
