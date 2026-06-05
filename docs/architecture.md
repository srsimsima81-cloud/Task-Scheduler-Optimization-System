# Task Scheduler Optimization System Architecture

## Overview

The system schedules tasks based on deadlines, priorities, duration, and profit.

## Workflow

Task Input
    ↓
Validation
    ↓
Sorting by Deadline & Priority
    ↓
Greedy Scheduling Algorithm
    ↓
Schedule Generation
    ↓
Performance Evaluation
    ↓
Timeline Visualization
    ↓
Report Generation

## Components

### User Interface
- Streamlit Dashboard
- Task Input Form
- KPI Cards
- Timeline Chart

### Scheduler Engine
- Task Sorting
- Deadline Checking
- Profit Calculation

### Output Module
- Scheduled Tasks
- Missed Tasks
- Performance Metrics

## Data Flow

User Input → Task Object → Scheduler → Results → Dashboard