#!/bin/bash

echo "-----------------------"
echo "Test: Get Users"
curl -X GET http://localhost:5000/api/v1/users
echo ""

echo "-----------------------"
echo "Test: Create User"
curl -X POST http://localhost:5000/api/v1/users \
-H "Content-Type: application/json" \
-d '{"name":"Ali","email":"ali@test.com"}'
echo ""

echo "-----------------------"
echo "Test: Invalid User"
curl -X POST http://localhost:5000/api/v1/users \
-H "Content-Type: application/json" \
-d '{"name":"","email":"invalid"}'
echo ""

echo "-----------------------"
echo "Test: Get Places"
curl -X GET http://localhost:5000/api/v1/places
echo ""

echo "-----------------------"
echo "Test: Get Reviews"
curl -X GET http://localhost:5000/api/v1/reviews
echo ""
