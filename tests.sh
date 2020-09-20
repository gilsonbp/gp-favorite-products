#!/bin/bash
# set -e : Forces the script to exit if any error occurs
set -e

if [ -z $1 ]; then
    # If the user does not pass any arguments, we will run ALL tests + coverage
    echo "Running the complete test suite"
    pip install coverage --quiet
    coverage run --source='apps' manage.py test
    coverage report
else
    echo "Testing" "$@"
    python manage.py test "$@"
fi
