"""Tiny demo app used as a benchmark fixture."""

from typing import Iterable


def filter_users(users: Iterable[dict], min_age: int = 0) -> list[dict]:
    # TODO: support filtering by multiple criteria, not just min_age.
    return [u for u in users if u.get("age", 0) >= min_age]


def search_users(users: Iterable[dict], query: str) -> list[dict]:
    # FIXME: this is a naive substring match — should be tokenized.
    q = query.lower()
    return [u for u in users if q in u.get("name", "").lower()]


def export_users(users: Iterable[dict]) -> str:
    # TODO: support multiple export formats (json, csv, yaml).
    return "\n".join(u["name"] for u in users)
