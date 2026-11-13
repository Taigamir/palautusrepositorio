# Copilot instructions for the login app

## Build, test, and validation commands

This project is a small Flask application with Robot Framework Browser acceptance tests.

- Install dependencies for the project and dev/test tooling:
  `cd ~/login && uv sync --group dev`
- Start the Flask app locally:
  `cd ~/login && uv run python src/index.py`
- Run the whole Robot suite:
  `cd ~/login && uv run robot src/tests`
- Run a single Robot file:
  `cd ~/login && uv run robot src/tests/login.robot`
- Run a single test case within a file:
  `cd ~/login && uv run robot -t "Login With Correct Credentials" src/tests/login.robot`

There is no dedicated lint, formatting, or type-check command configured in `pyproject.toml`; the project relies on the Robot Browser tests as the validation layer for behavior.

## High-level architecture

- `src/app.py` is the Flask application entrypoint. Route handlers render templates and orchestrate login/register behavior.
- `src/services/user_service.py` contains the business logic for validation and authentication checks. It intentionally keeps validation rules in one place instead of duplicating them across routes.
- `src/repositories/user_repository.py` stores users in memory in a singleton `user_repository`. This is not a persistent database; the state is reset through the `/tests/reset` endpoint used by the Browser tests.
- `src/entities/user.py` defines the `User` domain model.
- `src/templates/` contains the HTML templates for the home, login, register, welcome, and Ohtu pages.
- `src/tests/*.robot` uses Robot Framework + Browser library to drive the live Flask app at `http://localhost:5001` and verify the user flow end-to-end.

## Key conventions in this codebase

- Keep the layer separation consistent: routes in `src/app.py`, business rules in `src/services`, persistence logic in `src/repositories`, and the domain model in `src/entities`.
- Do not bypass `UserService` validation in route handlers; the validation rules are centralized there and are expected to raise `UserInputError`/`AuthenticationError`.
- The app uses a singleton in-memory repository, so tests must reset application state explicitly before each suite. The built-in helper `AppLibrary.reset_application()` calls `POST /tests/reset`.
- Browser tests are acceptance tests for UI flows, not unit tests. When changing the UI or route behavior, update the relevant Robot keyword file and the page objects/keywords in `src/tests/resource.robot` instead of creating a second test style.
- Template names and route names are intentionally aligned (`render_login`, `render_register`, etc.), so changes to one side usually require a matching update to the other.
