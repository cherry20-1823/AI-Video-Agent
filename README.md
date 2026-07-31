# Video Director Agent

Video Director Agent is an extensible AI workflow for planning, generating,
managing, and composing video assets.

## Current Features

- Project and scene domain models
- Pluggable LLM providers
- Storyboard planner
- Prompt builder
- Video provider interface
- Image provider interface
- Workspace asset management
- Mock image and video generation
- Unified task result model

## Workflow

    Topic
      |
      v
    LLM Planner
      |
      v
    Project and Scenes
      |
      v
    Prompt Builder
      |
      +--> Image Provider
      |
      +--> Video Provider
      |
      v
    Workspace Assets

## Installation

    python -m venv .venv
    source .venv/bin/activate
    pip install -e ".[dev]"

## Run

    python -m vda.main

## Tests

    pytest

## Code Quality

    ruff check .
