# Architecture Recommendation for a Fintech Fraud Detection Platform

## Problem Description

PayShield is a fintech startup building a real-time fraud detection and risk scoring platform for payment processors. When a transaction is initiated, PayShield receives an event, scores it for fraud risk within milliseconds, and returns a pass/flag/block decision.

The system handles millions of transaction events per day and must process each scoring request in under 200ms. Account balance and transaction history data requires strict consistency — a transaction must never be scored against stale balance data.

PayShield processes card data on behalf of payment processors and must comply with PCI DSS, requiring strict isolation of the cardholder data environment from the rest of the platform.

The engineering team has 12 people: 4 senior engineers, 6 mid-level engineers, and 2 DevOps engineers. There is no dedicated DBA — the engineers manage their own data stores. The team has solid monitoring experience and runs a mature on-call rotation.

Your task is to produce an architecture recommendation for PayShield.

## Output Specification

Write your recommendation to `recommendation.md`.
