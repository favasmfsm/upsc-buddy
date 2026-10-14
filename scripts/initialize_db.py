#!/usr/bin/env python
"""Initialize DB: migrate and seed Polity demo graph."""
import os
import sys

import django

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.dev")
django.setup()

from django.core.management import call_command

call_command("migrate", interactive=False)
call_command("seed_academy_fortuneias")
call_command("seed_syllabus_skeleton")
call_command("seed_polity")
print("Database initialized.")
