#!/bin/bash
if [ ${1:-""} = "build" ]; then
    echo "Building and up the containers ..."
    docker-compose up --build -d
else
    echo "Up the containers ..."
    docker-compose up -d
fi

echo "Containers running"

echo "Waiting the database accept connections ..."
sleep 10s
echo "Database is ok"

echo "Running migrations ..."
docker-compose exec web-django python src/manage.py migrate
echo "Database is updated"

echo "Server is running"