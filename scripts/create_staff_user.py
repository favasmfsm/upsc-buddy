#!/usr/bin/env python3
"""Create a staff user (is_staff=True, not superuser)."""
from __future__ import annotations

import argparse
import os
import sys

import django


def setup_django() -> None:
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if base_dir not in sys.path:
        sys.path.insert(0, base_dir)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.dev")
    django.setup()


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a staff user.")
    parser.add_argument("--email", default=os.environ.get("STAFF_EMAIL", "staff@example.com"))
    parser.add_argument("--username", default=os.environ.get("STAFF_USERNAME", "staff"))
    parser.add_argument("-p", "--password", default=os.environ.get("STAFF_PASSWORD", "staff12345"))
    args = parser.parse_args()

    setup_django()
    from user.models import UserAccount

    if UserAccount.objects.filter(email=args.email).exists():
        print(f"User {args.email!r} already exists.")
        return

    UserAccount.objects.create_user(
        email=args.email,
        password=args.password,
        username=args.username,
        is_staff=True,
    )
    print(f"Staff user {args.email!r} created.")


if __name__ == "__main__":
    main()
