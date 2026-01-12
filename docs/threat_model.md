# Go Phish Threat Modeling

## Purpose
Go Phish is a controlled phishing simulation platform designed for educational and portfolio purposes.  
This document outlines potential threats, mitigations, and security design considerations to show a security-conscious design approach.

---

## Actors
1. **Admin (Internal)**  
   - Manages campaigns, views metrics
   - Requires role-based access

2. **Participant (Simulated)**  
   - Interacts with phishing simulations
   - Only simulated identities; no real users

3. **External Attacker**  
   - Could attempt to exploit platform vulnerabilities (SQL injection, telemetry manipulation)

---

## Assets
- **Campaign Data**: Names, descriptions, status (non-sensitive)  
- **Telemetry Events**: Clicks, submissions, reports (behavioral, non-credential)  
- **Metrics & Analytics**: Aggregated data for dashboard

---

## Threats & Mitigations

| Threat | Description | Mitigation |
|--------|-------------|------------|
| **Data Leakage** | Sensitive user credentials stored accidentally | No real credentials stored; only behavioral metadata |
| **SQL Injection** | Malicious inputs via events or campaigns | Pydantic validation, parameterized queries via SQLAlchemy |
| **Unauthorized Access** | Admin APIs accessed by participants | Role-based access checks, separate API paths |
| **Telemetry Tampering** | Participant could alter event counts | Append-only events, audit timestamps, optional future hashing |
| **Denial of Service** | High-volume event posting could crash DB | Async ingestion, request rate limiting (future extension) |
| **Sensitive Logging** | Logging sensitive info accidentally | Minimal metadata, no secrets or credentials in logs |

---

## Security Principles Applied
- **Least Privilege**: Participants cannot access analytics or campaigns management  
- **Defense in Depth**: Multiple layers of input validation and role separation  
- **Data Minimization**: Store only behavioral signals, never sensitive content  
- **Immutable Telemetry**: Events are append-only and timestamped  
- **Ethical Boundaries**: No real phishing or emails sent  

---

## Future Enhancements
- Tamper-evident logs (hash chain per campaign)  
- Anomaly detection alerts for unusual event patterns  
- Rate-limiting middleware for event ingestion  
- Export to SIEM/Log Management tools for SOC-style demonstration

---

**Conclusion**:  
This threat model demonstrates that Go Phish is designed with security awareness in mind. It highlights ethical constraints, controlled exposure, and telemetry-focused security engineering — exactly what recruiters and reviewers want to see.
