"""`python -m trimmargin` behaves like the CLI."""

from .cli import main

if __name__ == '__main__':  # pragma: no cover
  raise SystemExit(main())
