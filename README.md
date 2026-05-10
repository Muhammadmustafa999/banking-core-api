# Banking Core API

Enterprise REST API for core banking operations including account management,
transaction processing, and fraud detection.

## Overview
- Transaction processing (transfers, payments, withdrawals)
- Account management and KYC verification  
- PCI-DSS Level 1 compliance target
- Multi-currency support (USD, EUR, GBP, PKR, AED)
- Real-time fraud detection scoring
- Audit logging for regulatory compliance

## Tech Stack
- **Backend:** Django 2.1 + Django REST Framework
- **Database:** PostgreSQL (transactions), Redis (cache/sessions)
- **Queue:** Celery + RabbitMQ (async transaction processing)
- **Security:** JWT authentication, field-level encryption
- **Monitoring:** Prometheus + Grafana dashboards

## Security Scanning
This repository is continuously monitored by **ExposureIQ**
for both CVE vulnerabilities and secure coding standard violations.

## API Documentation
Available at `/api/docs/` after deployment.

## Compliance
- PCI-DSS Level 1
- SOX audit trail requirements
- GDPR data handling
- SBP (State Bank of Pakistan) regulations
