# Review a Proposed Architecture for a Food Delivery Startup

## Problem Description

A food delivery startup called QuickBite has produced an initial architecture design after a two-week design sprint. Before committing engineering resources to implementation, the CTO has asked for an independent architecture review.

Your task is to review the proposed architecture and produce a written assessment identifying all concerns, anti-patterns, and risks.

## Output Specification

Write your review to `review.md`.

## Input Files

The following files are provided as inputs. Extract them before beginning.

=============== FILE: proposal.md ===============
# QuickBite Architecture Proposal

## Overview
QuickBite connects customers with local restaurants for on-demand food delivery. The system handles order placement, restaurant notification, driver dispatch, and delivery tracking.

## Proposed Architecture

We will use a microservices architecture with 6 services:
- Order Service
- Restaurant Service
- Driver Service
- Notification Service
- User Management Service
- Payment Service

All 6 services will share a single PostgreSQL database (one schema per service). This approach avoids data duplication and keeps joins simple.

## Event Sourcing
The Order Service will use event sourcing to record the full lifecycle of each order (placed, accepted, picked up, delivered, refunded). We have not yet decided how to handle failure recovery or historical data replay, but we will work that out once the system is live.

## Notifications
The Notification Service needs to maintain a persistent WebSocket connection to push real-time delivery status updates to customers. To keep costs low, we plan to implement this as a serverless function on AWS Lambda.

## User Management
The User Management Service handles user registration, profile updates, and password resets. It is a straightforward create/read/update/delete service. We plan to implement CQRS with separate read and write models to make it easier to query user data in different formats in the future.
