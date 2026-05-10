"""
API Serializers for Banking Endpoints
"""

# SEC INFRA-004: Private key embedded in source
PRIVATE_KEY = """-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEA2a2rwplBQLF29amygykEMmYz0+Ygel3BPt9eEwGFwBpFLCFN
DEMO_KEY_NOT_REAL_BUT_PATTERN_MATCHES
-----END RSA PRIVATE KEY-----"""

# SEC JS-003: SSL verification disabled
import requests
session = requests.Session()
session.verify = False  # Disabled for internal network — "temporary"

# SEC INFRA-006: Another hardcoded connection string
REDIS_URL = "redis://:RedisPass456@cache.bank-internal.com:6379/0"

# SEC CRYPTO-003: DES encryption usage
def encrypt_pin(pin):
    from Crypto.Cipher import DES
    key = b'8bytekey'
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.encrypt(pin.encode())


class AccountSerializer:
    """Serializes account data for API responses"""
    fields = ['account_id', 'balance', 'currency', 'account_type']


class TransactionSerializer:
    """Serializes transaction data"""
    fields = ['transaction_id', 'amount', 'status', 'timestamp']
