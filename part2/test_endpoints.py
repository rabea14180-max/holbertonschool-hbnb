#!/bin/bash

BASE_URL="http://127.0.0.1:5000/api/v1"

echo "==============================="
echo "Creating User..."
echo "==============================="

USER_RESPONSE=$(curl -s -X POST $BASE_URL/users \
-H "Content-Type: application/json" \
-d '{
  "first_name": "Solaf",
  "last_name":" Alessa",
  "email": "solaf@test.com",
  "password": "123456"
}')

echo $USER_RESPONSE

USER_ID=$(echo $USER_RESPONSE | grep -o '"id":"[^"]*' | cut -d'"' -f4)
echo "User ID: $USER_ID"

echo "==============================="
echo "Creating Amenity..."
echo "==============================="

AMENITY_RESPONSE=$(curl -s -X POST $BASE_URL/amenities \
-H "Content-Type: application/json" \
-d '{
  "name": "Swimming Pool"
}')

echo $AMENITY_RESPONSE

AMENITY_ID=$(echo $AMENITY_RESPONSE | grep -o '"id":"[^"]*' | cut -d'"' -f4)
echo "Amenity ID: $AMENITY_ID"

echo "==============================="
echo "Creating Place..."
echo "==============================="

PLACE_RESPONSE=$(curl -s -X POST $BASE_URL/places \
-H "Content-Type: application/json" \
-d "{
  \"title\": \"Luxury Villa\",
  \"description\": \"Sea View\",
  \"price\": 500,
  \"latitude\": 24.7136,
  \"longitude\": 46.6753,
  \"owner_id\": \"$USER_ID\",
  \"amenities\": [\"$AMENITY_ID\"]
}")

echo $PLACE_RESPONSE

PLACE_ID=$(echo $PLACE_RESPONSE | grep -o '"id":"[^"]*' | cut -d'"' -f4)
echo "Place ID: $PLACE_ID"

echo "==============================="
echo "Creating Review..."
echo "==============================="

REVIEW_RESPONSE=$(curl -s -X POST $BASE_URL/reviews \
-H "Content-Type: application/json" \
-d "{
  \"text\": \"Amazing place!\",
  \"rating\": 5,
  \"user_id\": \"$USER_ID\",
  \"place_id\": \"$PLACE_ID\"
}")

echo $REVIEW_RESPONSE

echo "==============================="
echo "Getting All Places..."
echo "==============================="

curl -s $BASE_URL/places
echo ""

echo "==============================="
echo "Getting Reviews By Place..."
echo "==============================="

curl -s $BASE_URL/places/$PLACE_ID
echo ""

echo "==============================="
echo "Updating Place Price..."
echo "==============================="

curl -s -X PUT $BASE_URL/places/$PLACE_ID \
-H "Content-Type: application/json" \
-d '{
  "price": 600
}'
echo ""

echo "==============================="
echo "Deleting Review..."
echo "==============================="

REVIEW_ID=$(echo $REVIEW_RESPONSE | grep -o '"id":"[^"]*' | cut -d'"' -f4)

curl -s -X DELETE $BASE_URL/reviews/$REVIEW_ID
echo ""

echo "==============================="
echo "TEST COMPLETED"
echo "==============================="
