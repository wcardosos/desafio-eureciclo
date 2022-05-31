#!/bin/bash
docker-compose up -d

if [ ${1:-""} = "coverage" ]; then
    docker-compose exec web-django coverage run --source='.' src/manage.py test
    docker-compose exec web-django coverage report
else
    docker-compose exec web-django python src/manage.py test
fi
