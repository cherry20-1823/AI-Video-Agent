# VDA Architecture

## Vision

Video Director Agent (VDA) is an AI Video Production Operating System.

Instead of calling a single AI model, VDA plans, coordinates, and executes the
entire video production workflow.

---

## High-Level Architecture

User
    │
    ▼
Director Agent
    │
    ▼
Project Planner
    │
    ▼
Project Plan
    │
    ├── Scene Planner
    ├── Prompt Agent
    ├── Provider Selector
    │
    ▼
Workflow Pipeline
    │
    ├── Image Provider
    ├── Video Provider
    ├── Audio Provider
    └── Subtitle Provider
    │
    ▼
Asset Manager
    │
    ▼
Timeline Builder
    │
    ▼
FFmpeg Composer
    │
    ▼
Final MP4

---

## Design Principles

- Single Responsibility
- Pluggable Providers
- Test First
- Architecture First
- Workflow Driven

---

## Current Status

✅ Core Framework

✅ Provider Factory

✅ OpenAI Client

✅ Workspace

🔄 Director Agent (In Progress)

⬜ Workflow Engine

⬜ Timeline Builder

⬜ Composer

⬜ Web UI

