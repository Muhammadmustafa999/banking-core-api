"""
Production settings — Banking Core API
"""

# SEC: DEBUG left True in production file
DEBUG = True

# SEC: Wildcard hosts
ALLOWED_HOSTS = ['*']

# Database config
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': 'prod-db.bank-internal.com',
        'NAME': 'banking_core',
        'USER': 'db_admin',
        # SEC: Hardcoded password
        'PASSWORD': 'SuperSecureDB2024!',
        'PORT': '5432',
    }
}

# SEC: Hardcoded email credentials
EMAIL_HOST_USER = 'banking-alerts@bank.com'
EMAIL_HOST_PASSWORD = 'EmailPass789!'

# SEC: Weak JWT secret
JWT_SECRET = "secret123"

# Stripe config
# SEC: Live API key hardcoded
STRIPE_SECRET_KEY = "sk_live_EXAMPLE_KEY_PATTERN_HERE"

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'banking',
]
