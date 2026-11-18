# Copilot instructions for the TDD shopping cart exercise

## Build, test, and validation commands

- Run from `viikko4/ttd-ostoskori/`, which contains this project's `pyproject.toml`.
- Install/synchronize the Python 3.14 environment and development dependencies:
  `uv sync --group dev`
- Run the complete test suite:
  `uv run pytest`
- Run one test file:
  `uv run pytest src/tests/ostoskori_test.py`
- Run one test method:
  `uv run pytest src/tests/ostoskori_test.py::TestOstoskori::test_ostoskorin_hinta_ja_tavaroiden_maara_alussa`
- No linting, formatting, build, or type-check command is configured in `pyproject.toml`.
- The project has no application entry point to start; `src/index.py` is a placeholder.

## High-level architecture

- `src/tuote.py` defines `Tuote`, the product model. A product has a name, unit price, and an unused `_saldo` field.
- `src/ostos.py` defines `Ostos`, a cart line for one product. It owns the quantity and delegates product name/price to `Tuote`.
- `src/ostoskori.py` defines `Ostoskori`, the aggregate cart API. It is intended to store one `Ostos` per product and compute item count and total price across those lines.
- `src/tests/ostoskori_test.py` contains unittest-style tests collected by pytest.
- `src/index.py` is currently an unused placeholder.

The implementation is intentionally small and partly TDD scaffolding: `Ostoskori` contains method stubs and comments describing the expected behavior. Implement behavior through the cart API rather than adding price or quantity logic to `Tuote`.

## Key conventions

- Use the existing Finnish domain names and method names (`Tuote`, `Ostos`, `Ostoskori`, `lisaa_tuote`, `poista_tuote`, `tyhjenna`, `ostokset`) consistently.
- Imports are module-local, e.g. `from tuote import Tuote` and `from ostoskori import Ostoskori`; run code and tests through the project root or pytest so `src` is on the Python import path.
- `Ostos` is the quantity-bearing cart line: add multiple units by changing `_lukumaara`, and keep quantities from becoming negative. `Ostoskori.ostokset()` is the list-of-lines view of the cart.
- Keep cart aggregation in `Ostoskori`: `tavaroita_korissa()` sums quantities, `hinta()` sums line prices, and adding the same product should update or locate its existing `Ostos` rather than create duplicate cart lines.
- Tests use `unittest.TestCase` for setup and assertions, while pytest is the configured runner.
