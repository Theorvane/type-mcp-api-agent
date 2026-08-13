#!/usr/bin/env python3
"""Fail-closed verification for asynchronous ClawHub skill publication."""

from __future__ import annotations

import argparse
import json
import time
from collections.abc import Callable
from typing import Protocol
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


class HttpResponse(Protocol):
    status: int

    def read(self) -> bytes: ...

    def __enter__(self) -> "HttpResponse": ...

    def __exit__(self, *_: object) -> None: ...


class UrlOpener(Protocol):
    def __call__(self, request: Request, *, timeout: int) -> HttpResponse: ...


def default_opener(request: Request, *, timeout: int) -> HttpResponse:
    return urlopen(request, timeout=timeout)


DEFAULT_ATTEMPTS = 12
DEFAULT_DELAY_SECONDS = 10.0


def version_url(registry: str, slug: str, version: str) -> str:
    return (
        f"{registry.rstrip('/')}/api/v1/skills/{slug}/versions/{version}"
    )


def fetch_public_version(
    registry: str,
    slug: str,
    version: str,
    *,
    opener: UrlOpener = default_opener,
) -> dict[str, object] | None:
    """Return the public version payload, None when its scan is still pending."""
    request = Request(version_url(registry, slug, version), method="GET")
    try:
        with opener(request, timeout=30) as response:
            if response.status != 200:
                raise SystemExit(f"ClawHub public verification returned HTTP {response.status}.")
            try:
                payload = json.loads(response.read())
            except json.JSONDecodeError as error:
                raise SystemExit("ClawHub public verification returned malformed JSON.") from error
    except HTTPError as error:
        if error.code == 404:
            return None
        raise SystemExit(f"ClawHub public verification returned HTTP {error.code}.") from error
    except URLError as error:
        raise SystemExit(f"ClawHub public verification request failed: {error.reason}") from error

    if not isinstance(payload, dict):
        raise SystemExit("ClawHub public verification returned an invalid payload.")
    public_version = payload.get("version")
    if not isinstance(public_version, dict) or public_version.get("version") != version:
        raise SystemExit("ClawHub public verification returned a mismatched version.")
    return payload


def wait_for_publication(
    registry: str,
    slug: str,
    version: str,
    *,
    attempts: int = DEFAULT_ATTEMPTS,
    delay_seconds: float = DEFAULT_DELAY_SECONDS,
    opener: UrlOpener = default_opener,
    sleep: Callable[[float], None] = time.sleep,
) -> dict[str, object]:
    if attempts < 1:
        raise ValueError("attempts must be at least one")
    if delay_seconds < 0:
        raise ValueError("delay_seconds must not be negative")

    for attempt in range(attempts):
        payload = fetch_public_version(registry, slug, version, opener=opener)
        if payload is not None:
            return payload
        if attempt < attempts - 1:
            sleep(delay_seconds)
    raise SystemExit(
        f"ClawHub version {slug}@{version} was not publicly available after {attempts} checks."
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--registry", required=True)
    parser.add_argument("--slug", required=True)
    parser.add_argument("--version", required=True)
    parser.add_argument("--attempts", type=int, default=DEFAULT_ATTEMPTS)
    parser.add_argument("--delay-seconds", type=float, default=DEFAULT_DELAY_SECONDS)
    args = parser.parse_args()
    wait_for_publication(
        args.registry,
        args.slug,
        args.version,
        attempts=args.attempts,
        delay_seconds=args.delay_seconds,
    )
    print(f"Verified public ClawHub version {args.slug}@{args.version}.")


if __name__ == "__main__":
    main()
