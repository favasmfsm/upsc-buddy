#!/usr/bin/env python3
"""Create an admin superuser.

Usage:
  pipenv run python scripts/create_admin_user.py
  pipenv run python scripts/create_admin_user.py --email a@b.com -p secret
"""
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
    parser = argparse.ArgumentParser(description="Create an admin superuser.")
    parser.add_argument(
        "--username",
        default=os.environ.get("ADMIN_USERNAME", "admin"),
        help="Username (default: admin)",
    )
    parser.add_argument(
        "--email",
        default=os.environ.get("ADMIN_EMAIL", "admin@example.com"),
        help="Email used for login (default: admin@example.com)",
    )
    parser.add_argument(
        "-p",
        "--password",
        default=os.environ.get("ADMIN_PASSWORD", "admin12345"),
        help="Password (default: admin12345)",
    )
    parser.add_argument(
        "--reset-password",
        action="store_true",
        help="If email already exists, reset password and admin flags.",
    )
    args = parser.parse_args()

    if not args.password:
        parser.error("Password is required (use -p or ADMIN_PASSWORD).")

    setup_django()
    from user.models import UserAccount

    existing = UserAccount.objects.filter(email=args.email).first()
    if existing:
        if args.reset_password:
            existing.set_password(args.password)
            existing.username = args.username
            existing.is_superuser = True
            existing.is_staff = True
            existing.save()
            print(f"Updated admin user {args.email!r}.")
        else:
            print(
                f"User {args.email!r} already exists. "
                "Pass --reset-password to update password and admin flags."
            )
        return

    UserAccount.objects.create_superuser(
        email=args.email,
        password=args.password,
        username=args.username,
    )
    print(f"Admin superuser {args.email!r} created successfully.")


if __name__ == "__main__":
    main()
