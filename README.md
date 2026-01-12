Go Phish is a security-focused web platform designed to simulate phishing campaigns in a controlled, ethical environment. The system models real-world social engineering techniques and captures security-relevant user interactions—such as link clicks, simulated credential submissions, and reports—without collecting sensitive data.

The platform emphasizes backend systems design, secure telemetry logging, and behavioral analytics to demonstrate how phishing attacks are detected, measured, and analyzed in practice. Go Phish is intentionally non-production and does not target real users; it exists to showcase cybersecurity thinking, defensive engineering principles, and ethical security simulation.

## Campaign Results Overview

The following metrics were collected from an example phishing campaign executed within the Go Phish platform. The campaign modeled a common “account security notice” scenario and measured user interaction patterns across multiple security-relevant events.

### Campaign: Account Security Alert

| Metric                          | Count |
|---------------------------------|-------|
| Campaign Targets                | 120   |
| Link Clicks                     | 44    |
| Credential Submission Attempts  | 11    |
| Phishing Reports                | 26    |

### Key Metrics
- **Click-Through Rate:** 36.7%
- **Credential Exposure Rate:** 9.2%
- **Reporting Rate:** 21.7%

These results reflect realistic social engineering outcomes, where a portion of users engage with the phishing link, a smaller subset attempts credential submission, and security-aware users report suspicious activity.

## Telemetry Observations

Event-level telemetry shows that credential submission attempts typically occurred shortly after link interaction, while report events were more evenly distributed over time. This behavior aligns with real-world phishing patterns, where impulsive actions occur early and reporting follows user reflection or secondary verification.

