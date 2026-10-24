# Django scaffold

This directory contains the Django initialization committed by Yevgeniy Averyanov for [QON-1](https://qonys.youtrack.cloud/issue/QON-1). The default Django applications, `/admin/`, SQLite and console email are configured. Residential domain models, DRF routes, company/buyer flows, workers, SMTP and AI processing are not implemented here yet.

## Local setup

Install [uv from its official source](https://docs.astral.sh/uv/getting-started/installation/). Run from this directory:

```console
uv sync --frozen
```

The project requires Python 3.14 or later. uv can obtain a compatible managed interpreter. Dependency versions come from the committed `uv.lock`; do not silently downgrade them to match a different local Python.

Create `backend/.env` by copying `.env.example`. Replace the secret-key placeholder with a locally generated value. For example, generate one with:

```console
uv run python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Keep the resulting value in the ignored `.env` file. `DJANGO_DEBUG=True` is for local development only. No SMTP credentials are needed for console email.

```console
uv run python manage.py check
uv run python manage.py migrate
uv run python manage.py runserver 127.0.0.1:8000
```

The final command starts the local server. `/` has no application page; `/admin/` is the existing entry point. If testing admin login, create a local user interactively with `uv run python manage.py createsuperuser`.

## Verification

```console
uv run python manage.py check
uv run python manage.py makemigrations --check --dry-run
```

These checks validate the scaffold configuration and model/migration consistency. They do not establish business acceptance. `uv run python manage.py test` currently has no project-specific business tests. Planned scenario conditions and metrics are in [the evaluation plan](../docs/submission-2026-10-24/17-evaluation-plan.md).
