# Architecture Recommendation for an IoT Sensor Data Platform

## Problem Description

A mid-sized manufacturing company is building SensorHub, an IoT data ingestion platform for its factory network. Factory floors send batch uploads of sensor readings throughout the day — each upload can contain up to 100,000 readings, but uploads happen in irregular bursts tied to shift handovers and equipment cycles. Between bursts the system may be almost entirely idle.

The engineering team has 8 people: 3 backend engineers, 2 data engineers, 2 frontend engineers, and 1 DevOps engineer. There is no dedicated database administrator. The team's monitoring practice is limited — they currently use basic uptime checks and have no structured logging or alerting pipeline in place.

The company's cloud budget for this platform is capped at $2,000/month. The CTO has explicitly said the team should not over-provision for peak capacity if there is a cost-effective alternative.

Your task is to produce an architecture recommendation for SensorHub.

## Output Specification

Write your recommendation to `recommendation.md`.
