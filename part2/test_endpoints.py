#!/bin/bash
# HBnB API Automated Test Script
# Automatically captures IDs from POST requests and uses them in subsequent requests

BASE_URL="http://127.0.0.1:5000/api/v1"

echo "===== 1️⃣ Users ====="

# Create a new user and capture USER_ID
USER_ID=$(curl -s -X POST $BASE_URL/users/ \
-H "Content-Type: application/json" \
-d '{
  "first_name": "Sola",
  "last_name": "AI",
  "email": "sola@example.com",
  "password": "123456",
  "is_admin": true
}' | jq -r '.id')

echo "Created user ID: $USER_ID"
echo -e "\n"

# Get all users
echo "Getting all users..."
curl -s -X GET $BASE_URL/users/
echo -e "\n"

# Get the created user
echo "Getting user $USER_ID..."
curl -s -X GET $BASE_URL/users/$USER_ID
echo -e "\n"

# Update the user
echo "Updating user $USER_ID..."
curl -s -X PUT $BASE_URL/users/$USER_ID \
-H "Content-Type: application/json" \
-d '{
  "first_name": "SolaUpdated",
  "last_name": "AIUpdated"
}'
echo -e "\n"

echo "===== 2️⃣ Amenities ====="

# Create a new amenity and capture AMENITY_ID
AMENITY_ID=$(curl -s -X POST $BASE_URL/amenities \
-H "Content-Type: application/json" \
-d '{
  "name": "Pool",
  "description": "Indoor swimming pool"
}' | jq -r '.id')

echo "Created amenity ID: $AMENITY_ID"
echo -e "\n"

# Get all amenities
echo "Getting all amenities..."
curl -s -X GET $BASE_URL/amenities
echo -e "\n"

# Update the amenity
echo "Updating amenity $AMENITY_ID..."
curl -s -X PUT $BASE_URL/amenities/$AMENITY_ID \
-H "Content-Type: application/json" \
-d '{
  "name": "Updated Pool",
  "description": "Updated indoor pool description"
}'
echo -e "\n"

echo "===== 3️⃣ Places ====="

# Create a new place and capture PLACE_ID
PLACE_ID=$(curl -s -X POST $BASE_URL/places/ \
-H "Content-Type: application/json" \
-d '{
  "title": "Ocean View Apartment",
  "description": "Beautiful apartment by the sea",
  "price": 150.0,
  "latitude": 24.7136,
  "longitude": 46.6753,
  "owner_id": "'"$USER_ID"'",
  "amenities": ["'"$AMENITY_ID"'"]
}' | jq -r '.id')

echo "Created place ID: $PLACE_ID"
echo -e "\n"

# Get all places
echo "Getting all places..."
curl -s -X GET $BASE_URL/places/
echo -e "\n"

# Update the place
echo "Updating place $PLACE_ID..."
curl -s -X PUT $BASE_URL/places/$PLACE_ID \
-H "Content-Type: application/json" \
-d '{
  "title": "Ocean View Apartment Updated",
  "price": 180.0,
  "amenities": ["'"$AMENITY_ID"'"]
}'
echo -e "\n"

# Get reviews for the place (should be empty initially)
echo "Getting reviews for place $PLACE_ID..."
curl -s -X GET $BASE_URL/places/$PLACE_ID/reviews
echo -e "\n"

echo "===== 4️⃣ Reviews ====="

# Create a review and capture REVIEW_ID
REVIEW_ID=$(curl -s -X POST $BASE_URL/reviews/ \
-H "Content-Type: application/json" \
-d '{
  "text": "Amazing stay!",
  "rating": 5,
  "user_id": "'"$USER_ID"'",
  "place_id": "'"$PLACE_ID"'"
}' | jq -r '.id')

echo "Created review ID: $REVIEW_ID"
echo -e "\n"

# Update the review
echo "Updating review $REVIEW_ID..."
curl -s -X PUT $BASE_URL/reviews/$REVIEW_ID \
-H "Content-Type: application/json" \
-d '{
  "text": "Updated review text",
  "rating": 4
}'
echo -e "\n"

# Delete the review
echo "Deleting review $REVIEW_ID..."
curl -s -X DELETE $BASE_URL/reviews/$REVIEW_ID
echo -e "\n"
