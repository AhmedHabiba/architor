# Architecture Recommendation for an Online Learning Platform

## Problem Description

EduStream is an online learning platform offering video courses, quizzes, and certifications. The platform serves a large audience: approximately 300,000 course page views per day, but only around 30,000 quiz submissions per day. Course catalogue browsing and video stream metadata are the dominant read operations. Quiz submission and grade recording, however, require strict accuracy — a student must never see an incorrect grade, and duplicate submissions must be idempotent.

EduStream also processes course subscription payments online. The payments team must operate under PCI DSS compliance, which requires isolating cardholder data from the rest of the system.

Separately, the platform fires a high volume of notifications: course completion events, certificate issuance, instructor reply alerts, and promotional reminders. The team expects the notification volume to grow significantly as the user base grows.

The engineering team has 18 engineers and 3 dedicated DevOps engineers. The team is experienced and has operated distributed systems before.

Your task is to produce an architecture recommendation for EduStream.

## Output Specification

Write your recommendation to `recommendation.md`.
