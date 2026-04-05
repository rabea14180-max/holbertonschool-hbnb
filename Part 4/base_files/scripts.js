function setCookie(name, value) {
    document.cookie = `${name}=${value}; path=/`;
}

function getCookie(name) {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i += 1) {
        const cookie = cookies[i].trim();
        if (cookie.startsWith(`${name}=`)) {
            return cookie.substring(name.length + 1);
        }
    }
    return null;
}

function getAuthHeaders() {
    const token = getCookie('token');
    const headers = {
        'Content-Type': 'application/json'
    };

    if (token) {
        headers.Authorization = `Bearer ${token}`;
    }

    return headers;
}

function getPlacePrice(place) {
    if (place.price_by_night !== undefined && place.price_by_night !== null) {
        return Number(place.price_by_night);
    }
    if (place.price !== undefined && place.price !== null) {
        return Number(place.price);
    }
    return 0;
}

function getPlaceTitle(place) {
    return place.title || place.name || 'Unnamed place';
}

function getPlaceDescription(place) {
    return place.description || 'No description available';
}

function getPlaceIdFromURL() {
    const params = new URLSearchParams(window.location.search);
    return params.get('id');
}

function checkRequiredAuthentication() {
    const token = getCookie('token');

    if (!token) {
        window.location.href = 'index.html';
        return null;
    }

    return token;
}

function displayPlaces(places) {
    const placesList = document.getElementById('places-list');

    if (!placesList) {
        return;
    }

    placesList.innerHTML = '';

    places.forEach((place) => {
        const placeCard = document.createElement('div');
        placeCard.className = 'place-card';
        placeCard.dataset.price = getPlacePrice(place);

        placeCard.innerHTML = `
            <h3>${getPlaceTitle(place)}</h3>
            <p>${getPlaceDescription(place)}</p>
            <p><strong>Price:</strong> $${getPlacePrice(place)}/night</p>
            <a href="place.html?id=${place.id}" class="details-button">View Details</a>
        `;

        placesList.appendChild(placeCard);
    });
}

function filterPlacesByPrice() {
    const priceFilter = document.getElementById('price-filter');
    const placeCards = document.querySelectorAll('.place-card');

    if (!priceFilter) {
        return;
    }

    const selectedValue = priceFilter.value;

    placeCards.forEach((card) => {
        const placePrice = Number(card.dataset.price);

        if (selectedValue === 'All' || placePrice <= Number(selectedValue)) {
            card.style.display = 'block';
        } else {
            card.style.display = 'none';
        }
    });
}

async function fetchPlaces() {
    try {
        const response = await fetch('http://127.0.0.1:5000/api/v1/places/', {
            method: 'GET',
            headers: getAuthHeaders()
        });

        if (!response.ok) {
            throw new Error('Failed to fetch places');
        }

        const places = await response.json();
        displayPlaces(places);
        filterPlacesByPrice();
    } catch (error) {
        console.error(error);
    }
}

function checkIndexAuthentication() {
    const token = getCookie('token');
    const loginLink = document.getElementById('login-link');

    if (!loginLink) {
        return;
    }

    if (token) {
        loginLink.style.display = 'none';
    } else {
        loginLink.style.display = 'inline-block';
    }
}

function getHostName(place) {
    if (place.owner && place.owner.first_name) {
        const lastName = place.owner.last_name ? ` ${place.owner.last_name}` : '';
        return `${place.owner.first_name}${lastName}`;
    }
    if (place.user && place.user.first_name) {
        const lastName = place.user.last_name ? ` ${place.user.last_name}` : '';
        return `${place.user.first_name}${lastName}`;
    }
    if (place.host) {
        return place.host;
    }
    return 'Unknown host';
}

function getAmenitiesList(place) {
    if (Array.isArray(place.amenities) && place.amenities.length > 0) {
        return place.amenities.map((amenity) => {
            if (typeof amenity === 'string') {
                return amenity;
            }
            return amenity.name || 'Amenity';
        }).join(', ');
    }
    return 'No amenities available';
}

function getReviewsHTML(place) {
    if (!Array.isArray(place.reviews) || place.reviews.length === 0) {
        return '<p>No reviews yet.</p>';
    }

    return place.reviews.map((review) => {
        let reviewer = 'Anonymous';

        if (review.user && review.user.first_name) {
            reviewer = `${review.user.first_name}${review.user.last_name ? ` ${review.user.last_name}` : ''}`;
        } else if (review.user_name) {
            reviewer = review.user_name;
        } else if (review.user_id) {
            reviewer = review.user_id;
        }

        return `
            <div class="review-card">
                <p>${review.comment || review.text || 'No comment provided'}</p>
                <p><strong>User:</strong> ${reviewer}</p>
                <p><strong>Rating:</strong> ${review.rating !== undefined ? review.rating : 'N/A'}</p>
            </div>
        `;
    }).join('');
}

function displayPlaceDetails(place) {
    const placeDetails = document.getElementById('place-details');

    if (!placeDetails) {
        return;
    }

    placeDetails.innerHTML = `
        <h2>${getPlaceTitle(place)}</h2>

        <div class="place-info">
            <p><strong>Host:</strong> ${getHostName(place)}</p>
            <p><strong>Price:</strong> $${getPlacePrice(place)}/night</p>
            <p><strong>Description:</strong> ${getPlaceDescription(place)}</p>
            <p><strong>Amenities:</strong> ${getAmenitiesList(place)}</p>
        </div>

        <h3>Reviews</h3>
        <div class="reviews-list">
            ${getReviewsHTML(place)}
        </div>
    `;
}

function checkPlaceAuthentication() {
    const token = getCookie('token');
    const addReviewSection = document.getElementById('add-review');

    if (!addReviewSection) {
        return token;
    }

    if (token) {
        addReviewSection.style.display = 'block';
    } else {
        addReviewSection.style.display = 'none';
    }

    return token;
}

async function fetchPlaceDetails(placeId) {
    try {
        const response = await fetch(`http://127.0.0.1:5000/api/v1/places/${placeId}`, {
            method: 'GET',
            headers: getAuthHeaders()
        });

        if (!response.ok) {
            throw new Error('Failed to fetch place details');
        }

        const place = await response.json();
        displayPlaceDetails(place);
    } catch (error) {
        console.error(error);
    }
}

async function submitReview(token, placeId, reviewText, rating) {
    const payload = {
        place_id: placeId,
        text: reviewText,
        comment: reviewText,
        rating: Number(rating)
    };

    const response = await fetch('http://127.0.0.1:5000/api/v1/reviews/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            Authorization: `Bearer ${token}`
        },
        body: JSON.stringify(payload)
    });

    return response;
}

document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('login-form');
    const priceFilter = document.getElementById('price-filter');
    const placesList = document.getElementById('places-list');
    const placeDetails = document.getElementById('place-details');
    const reviewForm = document.getElementById('review-form');

    if (loginForm) {
        loginForm.addEventListener('submit', async (event) => {
            event.preventDefault();

            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;

            try {
                const response = await fetch('http://127.0.0.1:5000/api/v1/auth/login', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        email: email,
                        password: password
                    })
                });

                if (response.ok) {
                    const data = await response.json();
                    setCookie('token', data.access_token);
                    window.location.href = 'index.html';
                } else {
                    alert('Login failed: Incorrect email or password');
                }
            } catch (error) {
                console.error(error);
                alert('Something went wrong. Please try again.');
            }
        });
    }

    if (placesList) {
        checkIndexAuthentication();
        fetchPlaces();

        if (priceFilter) {
            priceFilter.addEventListener('change', filterPlacesByPrice);
        }
    }

    if (placeDetails) {
        const placeId = getPlaceIdFromURL();
        checkPlaceAuthentication();

        if (placeId) {
            fetchPlaceDetails(placeId);

            const addReviewLink = document.getElementById('add-review-link');
            if (addReviewLink) {
                addReviewLink.href = `add_review.html?id=${placeId}`;
            }
        }
    }

    if (reviewForm) {
        const token = checkRequiredAuthentication();
        const placeId = getPlaceIdFromURL();
        const reviewTextField = document.getElementById('review-text');
        const ratingField = document.getElementById('rating');

        reviewForm.addEventListener('submit', async (event) => {
            event.preventDefault();

            const reviewText = reviewTextField.value.trim();
            const rating = ratingField.value;

            if (!reviewText || !placeId || !token || !rating) {
                alert('Failed to submit review');
                return;
            }

            try {
                const response = await submitReview(token, placeId, reviewText, rating);

                if (response.ok) {
                    alert('Review submitted successfully!');
                    reviewForm.reset();
                    window.location.href = `place.html?id=${placeId}`;
                } else {
                    alert('Failed to submit review');
                }
            } catch (error) {
                console.error(error);
                alert('Failed to submit review');
            }
        });
    }
});
