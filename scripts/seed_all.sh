#!/bin/sh
# Load all static content: academy, syllabus spine, then concept content.
# seed_polity runs every Polity chapter seed itself, in order.
set -e

python manage.py seed_academy_fortuneias
python manage.py seed_syllabus_skeleton
python manage.py seed_visual_grammar_catalog
python manage.py seed_polity
python manage.py seed_geomorphology
