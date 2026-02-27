# Organization Context — [Your Organization Name]

> **Instructions:** Fill this out before starting the architecture session.
> The more detail you provide, the more relevant the recommendations will be.
> If you skip this file, `/analyze-prd` will offer a discovery interview to fill it in.

## Team Profile (REQUIRED)

- **Team size:** [e.g., 6 developers, 1 DevOps, 1 QA]
- **Seniority distribution:** [e.g., 2 senior, 3 mid, 1 junior]
- **Key skills:** [e.g., Strong in Java/Spring, moderate React, no Go experience]
- **Gaps:** [e.g., No dedicated DBA, no security specialist]
- **Availability:** [e.g., Full team dedicated, or 50% shared with other projects]

## Current Technology Stack (REQUIRED)

- **Backend:** [e.g., Java 17 / Spring Boot 3.1]
- **Frontend:** [e.g., React 18 / TypeScript]
- **Database:** [e.g., PostgreSQL 14, Redis 7]
- **Messaging:** [e.g., RabbitMQ 3.12]
- **Cloud provider:** [e.g., AWS eu-west-1 and me-south-1]
- **Container orchestration:** [e.g., EKS / Kubernetes 1.28]
- **CI/CD:** [e.g., GitHub Actions, ArgoCD]
- **Monitoring:** [e.g., Datadog, PagerDuty]

## Technology Preferences (RECOMMENDED)

- **Preferred:** [Technologies the org favors and has experience with]
- **Approved but less experienced:** [Technologies allowed but team needs ramp-up]
- **Banned / Avoid:** [Technologies with past problems or policy restrictions]
  - [e.g., MongoDB — operational issues in 2024, abandoned after 3 months]
  - [e.g., GraphQL — team lacks experience, past project overran by 2 months]

## Infrastructure Constraints (REQUIRED)

- **Cloud regions:** [e.g., Must deploy in me-south-1 for data residency]
- **Network:** [e.g., VPN required for internal services, no public endpoints]
- **Budget:** [e.g., Monthly cloud budget ~$5K, cannot exceed $8K]
- **Existing services to integrate:** [e.g., Corporate LDAP, SAP ERP, legacy Oracle DB]

## Compliance & Security Requirements (REQUIRED if applicable)

- **Regulatory:** [e.g., NCA ECC, PCI-DSS, HIPAA, GDPR, SOC2]
- **Data residency:** [e.g., All PII must stay in Saudi Arabia]
- **Encryption:** [e.g., AES-256 at rest, TLS 1.3 in transit]
- **Audit:** [e.g., All state changes must be audit-logged for 7 years]
- **Authentication:** [e.g., Must integrate with corporate SSO / Azure AD]

## Timeline & Delivery Constraints (REQUIRED)

- **Target go-live:** [e.g., Q3 2026]
- **Phased delivery acceptable?** [Yes/No — if yes, what's the MVP scope?]
- **Hard deadlines:** [e.g., Regulatory deadline, contract commitment]

## Past Architecture Decisions — Lessons Learned (OPTIONAL but valuable)

> List past architecture decisions that went well or badly.
> This helps the agent avoid repeating mistakes.

- **[Year/Quarter]:** [What happened, what was learned]
  - e.g., 2024 Q2: Attempted event sourcing for order management. Abandoned after 3 months — team couldn't debug event replay issues.
  - e.g., 2023 Q4: ElasticSearch cluster for search. Operational overhead unsustainable with 1 DevOps engineer. Switched to PostgreSQL full-text search.

## Non-Negotiable Requirements (REQUIRED)

> Things that MUST be true regardless of architecture decisions.

- [e.g., 99.9% availability SLA]
- [e.g., Sub-200ms API response time at p95]
- [e.g., Zero-downtime deployments]
- [e.g., All services must be containerized]
