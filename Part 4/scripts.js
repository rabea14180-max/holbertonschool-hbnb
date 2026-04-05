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

function getPlaceLocation(place) {
    if (place.city && place.country) {
        return `${place.city}, ${place.country}`;
    }
    if (place.location) {
        return place.location;
    }
    if (place.country) {
        return place.country;
    }
    return 'Location not available';
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
            <p><strong>Location:</strong> ${getPlaceLocation(place)}</p>
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

function checkAuthentication() {
    const token = getCookie('token');
    const loginLink = document.getElementById('login-link');

    if (loginLink) {
        if (token) {
            loginLink.style.display = 'none';
        } else {
            loginLink.style.display = 'inline-block';
        }
    }
}

document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('login-form');
    const priceFilter = document.getElementById('price-filter');

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

    if (document.getElementById('places-list')) {
        checkAuthentication();
        fetchPlaces();

        if (priceFilter) {
            priceFilter.addEventListener('change', filterPlacesByPrice);
        }
    }
});
