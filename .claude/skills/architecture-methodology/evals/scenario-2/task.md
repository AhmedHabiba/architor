# Review an Architecture Proposal for a Healthcare Analytics Platform

## Problem Description

A team is building MedInsight, a healthcare analytics platform that aggregates patient records from multiple hospital systems and provides dashboards for clinical staff to spot trends and anomalies. After an internal design sprint, the team has produced an architecture proposal and wants an independent review before committing to the design.

Your task is to act as the architecture agent and conduct a thorough review of the proposal. Identify all concerns, risks, and questions the team must resolve before this design should be approved.

## Output Specification

Produce `architecture-review.md` — a detailed written review of the proposal.

## Input Files

The following files are provided as inputs. Extract them before beginning.

=============== FILE: proposal.md ===============
# MedInsight Architecture Proposal

## Overview
MedInsight will ingest HL7/FHIR records from 12 hospital systems, transform and normalise the data, and serve analytics dashboards to approximately 500 clinical staff.

## Proposed Architecture
We will adopt an event-driven microservices architecture. This is the same approach used by Netflix, Uber, and Airbnb for handling large-scale data ingestion, so it is the natural choice for a data platform like ours.

We plan 14 independent microservices:
- Data Ingestion Service
- HL7 Parser Service
- FHIR Normalisation Service
- Patient Deduplication Service
- Event Router Service
- Analytics Aggregation Service
- Dashboard API Service
- Auth Service
- Notification Service
- Audit Log Service
- Admin Service
- Report Export Service
- Data Archival Service
- Config Service

## Technology Choices
We will use Kafka for event streaming between services.

## Team
The engineering team consists of 3 developers. No dedicated DevOps engineer.

## Timeline
8 months to production.

## Open Items
- Security and regulatory compliance (HIPAA) — we'll work this out as we build
- Uptime and availability requirements — TBD, probably fine for a dashboard tool
- Cost model — not defined yet
- Monitoring and alerting — standard stuff, we'll handle it later
