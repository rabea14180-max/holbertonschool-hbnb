function setCookie(name, value) {
    document.cookie = `${name}=${value}; path=/`;
}

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
    return null;
}

function parseJwt(token) {
    try {
        return JSON.parse(atob(token.split('.')[1]));
    } catch (e) {
        return null;
    }
}

/** Backend API root. Override before loading scripts: window.HBNB_API_BASE = 'http://localhost:5000'; */
const API_BASE = (typeof window !== 'undefined' && window.HBNB_API_BASE) || 'http://127.0.0.1:5000';

const HOUSE_SETS = [
    // House 1
    {
        exterior: 'https://images.unsplash.com/photo-1512917774080-9991f1c4c750?auto=format&fit=crop&w=1200&q=80&ixlib=rb-4.0.3',
        livingroom: 'https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?auto=format&fit=crop&w=800&q=80&ixlib=rb-4.0.3',
        bedroom: 'https://images.unsplash.com/photo-1560067174-c5a3a8f37060?auto=format&fit=crop&w=800&q=80&ixlib=rb-4.0.3',
        kitchen: 'https://images.unsplash.com/photo-1556910103-1c02745aae4d?auto=format&fit=crop&w=800&q=80&ixlib=rb-4.0.3',
        bathroom: 'https://images.unsplash.com/photo-1620626011761-996317b8d101?auto=format&fit=crop&w=800&q=80&ixlib=rb-4.0.3',
        hallway: 'https://images.unsplash.com/photo-1629079447841-f0eb1a7fbccb?auto=format&fit=crop&w=800&q=80&ixlib=rb-4.0.3'
    },
    // House 2
    {
        exterior: 'https://images.unsplash.com/photo-1583608205776-bfd35f0d9f83?auto=format&fit=crop&w=1200&q=80&ixlib=rb-4.0.3',
        livingroom: 'https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?auto=format&fit=crop&w=800&q=80&ixlib=rb-4.0.3',
        bedroom: 'https://images.unsplash.com/photo-1578683010236-d716f9a3f461?auto=format&fit=crop&w=800&q=80&ixlib=rb-4.0.3',
        kitchen: 'https://images.unsplash.com/photo-1556909212-d5b604d0c90d?auto=format&fit=crop&w=800&q=80&ixlib=rb-4.0.3',
        bathroom: 'https://images.unsplash.com/photo-1552321554-5fefe8c9ef14?auto=format&fit=crop&w=800&q=80&ixlib=rb-4.0.3',
        hallway: 'https://images.unsplash.com/photo-1565182999561-18d7dc61c393?auto=format&fit=crop&w=800&q=80&ixlib=rb-4.0.3'
    },
    // House 3
    {
        exterior: 'https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?auto=format&fit=crop&w=1200&q=80&ixlib=rb-4.0.3',
        livingroom: 'https://images.unsplash.com/photo-1600607686527-6fb886090705?auto=format&fit=crop&w=800&q=80&ixlib=rb-4.0.3',
        bedroom: 'https://images.unsplash.com/photo-1616594039964-ae9021a400a0?auto=format&fit=crop&w=800&q=80&ixlib=rb-4.0.3',
        kitchen: 'https://images.unsplash.com/photo-1600566752355-35792bedcfea?auto=format&fit=crop&w=800&q=80&ixlib=rb-4.0.3',
        bathroom: 'https://images.unsplash.com/photo-1584622650111-993a426fbf0a?auto=format&fit=crop&w=800&q=80&ixlib=rb-4.0.3',
        hallway: 'https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=800&q=80&ixlib=rb-4.0.3'
    },
    // House 4
    {
        exterior: 'https://images.unsplash.com/photo-1510798831971-661eb04b3739?auto=format&fit=crop&w=1200&q=80&ixlib=rb-4.0.3',
        livingroom: 'https://images.unsplash.com/photo-1586023492125-27b2c045efd7?auto=format&fit=crop&w=800&q=80&ixlib=rb-4.0.3',
        bedroom: 'https://images.unsplash.com/photo-1540518614846-7eded433c457?auto=format&fit=crop&w=800&q=80&ixlib=rb-4.0.3',
        kitchen: 'https://images.unsplash.com/photo-1584622781564-1d987f7333c1?auto=format&fit=crop&w=800&q=80&ixlib=rb-4.0.3',
        bathroom: 'https://images.unsplash.com/photo-1600573472550-8090b5e0745e?auto=format&fit=crop&w=800&q=80&ixlib=rb-4.0.3',
        hallway: 'https://images.unsplash.com/photo-1600607688969-a5bfcd64bd28?auto=format&fit=crop&w=800&q=80&ixlib=rb-4.0.3'
    },
    // House 5
    {
        exterior: 'https://images.unsplash.com/photo-1449844908441-8829872d2607?auto=format&fit=crop&w=1200&q=80&ixlib=rb-4.0.3',
        livingroom: 'https://images.unsplash.com/photo-1567016432779-094069806bea?auto=format&fit=crop&w=800&q=80&ixlib=rb-4.0.3',
        bedroom: 'https://images.unsplash.com/photo-1554995207-c18c203602cb?auto=format&fit=crop&w=800&q=80&ixlib=rb-4.0.3',
        kitchen: 'https://images.unsplash.com/photo-1556909114-f6e7ad7d3136?auto=format&fit=crop&w=800&q=80&ixlib=rb-4.0.3',
        bathroom: 'https://images.unsplash.com/photo-1628624747186-a941c476b7ef?auto=format&fit=crop&w=800&q=80&ixlib=rb-4.0.3',
        hallway: 'https://images.unsplash.com/photo-1600566752229-250ce4d11fc7?auto=format&fit=crop&w=800&q=80&ixlib=rb-4.0.3'
    }
];

function getPlaceImage(placeId, width = 400, height = 300, roomType = 'exterior') {
    let hash = 0;
    if (placeId) {
        for (let i = 0; i < placeId.length; i++) {
            hash = placeId.charCodeAt(i) + ((hash << 5) - hash);
        }
    }
    const houseIndex = Math.abs(hash) % HOUSE_SETS.length; // Completely binds a place to a cohesive Unique House Set
    
    // Safely map room types
    let category = 'exterior';
    if (roomType.includes('livingroom')) category = 'livingroom';
    else if (roomType.includes('bedroom')) category = 'bedroom';
    else if (roomType.includes('kitchen')) category = 'kitchen';
    else if (roomType.includes('bathroom')) category = 'bathroom';
    else if (roomType.includes('hallway')) category = 'hallway';
    
    return HOUSE_SETS[houseIndex][category];
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

        const placeTitle = getPlaceTitle(place);
        const placeDesc = getPlaceDescription(place);
        placeCard.dataset.title = placeTitle.toLowerCase();
        placeCard.dataset.desc = placeDesc.toLowerCase();

        // Calculate Average Rating
        let ratingText = '⭐ New';
        if (Array.isArray(place.reviews) && place.reviews.length > 0) {
            const validReviews = place.reviews.filter(r => r.rating !== undefined && r.rating !== null);
            if (validReviews.length > 0) {
                const total = validReviews.reduce((sum, r) => sum + Number(r.rating), 0);
                ratingText = `⭐ ${(total / validReviews.length).toFixed(1)}`;
            }
        }

        placeCard.innerHTML = `
            <a href="place.html?id=${place.id}" style="text-decoration: none; color: inherit; display: flex; flex-direction: column; height: 100%;">
                <div class="place-card-image" style="width: 100%; height: 300px; overflow: hidden; border-radius: 12px; margin-bottom: 15px;">
                    <img src="${place.image_url || getPlaceImage(place.id, 400, 300)}" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.3s;" onerror="this.parentElement.parentElement.parentElement.style.display='none'" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'" />
                </div>
                <div class="place-card-content">
                    <div style="display: flex; justify-content: space-between; align-items: start;">
                        <h3 style="margin: 0; font-size: 1rem; font-weight: 600; color: var(--text-primary); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; padding-right: 10px;">${placeTitle}</h3>
                        <span style="font-weight: 400; font-size: 0.95rem; color: var(--text-primary); flex-shrink: 0;">${ratingText.replace('⭐', '★')}</span>
                    </div>
                    <div class="city-country-tag" style="color: var(--text-secondary); font-size: 0.95rem; margin-top: 4px;">Loc: ${place.latitude || '0'}, ${place.longitude || '0'}</div>
                    <div style="color: var(--text-secondary); font-size: 0.95rem; display: -webkit-box; -webkit-line-clamp: 1; -webkit-box-orient: vertical; overflow: hidden;">${placeDesc}</div>
                    <div class="price" style="margin-top: 6px; font-size: 1rem;">
                        <span style="font-weight: 600; color: var(--text-primary);">$${getPlacePrice(place)}</span>
                        <span style="font-weight: 400; color: var(--text-primary);">night</span>
                    </div>
                </div>
            </a>
        `;

        placesList.appendChild(placeCard);
        
        // Reverse Geocoding for a real city name asynchronously
        if (place.latitude && place.longitude) {
            fetch(`https://nominatim.openstreetmap.org/reverse?format=json&lat=${place.latitude}&lon=${place.longitude}&zoom=10`)
                .then(r => r.json())
                .then(data => {
                    const city = data.address?.city || data.address?.town || data.address?.village || data.address?.county || data.address?.state || 'Unknown Location';
                    const country = data.address?.country || '';
                    const locTag = placeCard.querySelector('.city-country-tag');
                    if (locTag) locTag.innerHTML = `${city}${country ? ', ' + country : ''}`;
                }).catch(err => console.log('Geocoding err for ' + place.id));
        }
    });
}

function filterPlaces() {
    const priceFilter = document.getElementById('price-filter');
    const searchFilter = document.getElementById('search-filter');
    const placeCards = document.querySelectorAll('.place-card');

    if (!priceFilter || !searchFilter) {
        return;
    }

    const maxPrice = priceFilter.value;
    const searchTerm = searchFilter.value.toLowerCase().trim();

    placeCards.forEach((card) => {
        const placePrice = Number(card.dataset.price);
        const title = card.dataset.title;
        const desc = card.dataset.desc;

        const matchesPrice = (maxPrice === 'All' || placePrice <= Number(maxPrice));
        const matchesSearch = (searchTerm === '' || title.includes(searchTerm) || desc.includes(searchTerm));

        if (matchesPrice && matchesSearch) {
            card.style.display = 'block';
        } else {
            card.style.display = 'none';
        }
    });
}

const mockPlacesData = [
    { id: 'mock-1', title: 'Luxury Villa by the Beach', description: 'Experience the ultimate relaxation with an expansive private pool and direct ocean access. The perfect getaway.', price: 450, latitude: 25.0343, longitude: -77.3963, reviews: [{rating: 5}, {rating: 5}, {rating: 4}], amenities: [{name: 'WiFi'}, {name: 'Pool'}, {name: 'Ocean View'}, {name: 'Private Beach Access'}, {name: 'Air Conditioning'}] },
    { id: 'mock-2', title: 'Cozy Mountain Cabin', description: 'Perfect retreat for nature lovers. Includes a wood-burning fireplace and stunning woodland views.', price: 85, latitude: 45.3859, longitude: 4.3900, reviews: [{rating: 4}, {rating: 5}], amenities: [{name: 'Indoor Fireplace'}, {name: 'Heating'}, {name: 'Free Parking'}, {name: 'Kitchen'}, {name: 'Hot Water'}] },
    { id: 'mock-4', title: 'Historic Castle Wing', description: 'Feel like royalty in this beautifully restored 18th-century castle wing with medieval architecture.', price: 299, latitude: 51.1784, longitude: -1.8262, reviews: [{rating: 4}], amenities: [{name: 'Free Parking'}, {name: 'Garden or Backyard'}, {name: 'Indoor Fireplace'}, {name: 'Dedicated Workspace'}] },
    { id: 'mock-5', title: 'Minimalist Desert Eco-Home', description: 'Off-grid sustainable living with spectacular stargazing and panoramic desert landscapes.', price: 120, latitude: 34.1361, longitude: -116.0542, reviews: [{rating: 5}, {rating: 5}, {rating: 5}], amenities: [{name: 'Solar Power'}, {name: 'Desert View'}, {name: 'Patio or Balcony'}, {name: 'Kitchen'}, {name: 'Free Parking'}] }
];

async function fetchPlaces() {
    try {
        const response = await fetch(`${API_BASE}/api/v1/places/`, {
            method: 'GET',
            headers: getAuthHeaders()
        });

        if (!response.ok) {
            throw new Error('Failed to fetch places');
        }

        let places = await response.json();
        if (!Array.isArray(places)) {
            places = [];
        }

        displayPlaces(places);
        filterPlaces();
    } catch (error) {
        console.error(error);
    }
}

function checkAuthentication() {
    const token = getCookie('token');
    
    // Hide old hardcoded nav actions
    const oldContainer = document.getElementById('nav-actions-container');
    if (oldContainer) oldContainer.style.display = 'none';

    // Target the profile pill
    const userNavPill = document.querySelector('.user-nav-pill');
    
    if (userNavPill) {
        userNavPill.id = 'profile-btn';
        
        // Enhance Pill Styling
        userNavPill.addEventListener('mouseover', () => userNavPill.style.boxShadow = '0 2px 8px rgba(0,0,0,0.15)');
        userNavPill.addEventListener('mouseout', () => userNavPill.style.boxShadow = 'none');
    
        // Create Dropdown Container Dynamically
        let dropdown = document.getElementById('profile-dropdown');
        if (!dropdown) {
            dropdown = document.createElement('div');
            dropdown.id = 'profile-dropdown';
            dropdown.style.display = 'none';
            dropdown.style.position = 'absolute';
            dropdown.style.top = '115%'; // Appear right below header
            dropdown.style.right = '0';
            dropdown.style.background = 'var(--surface-color)';
            dropdown.style.borderRadius = '14px';
            dropdown.style.boxShadow = '0 4px 18px rgba(0,0,0,0.12)';
            dropdown.style.width = '240px';
            dropdown.style.border = '1px solid var(--border-color)';
            dropdown.style.overflow = 'hidden';
            dropdown.style.zIndex = '9999';
            dropdown.style.flexDirection = 'column';
            dropdown.style.padding = '8px 0';
            
            // Ensure parent nav handles absolute positioning
            userNavPill.parentNode.style.position = 'relative'; 
            userNavPill.parentNode.appendChild(dropdown);
            
            // Toggle Logic
            userNavPill.addEventListener('click', (e) => {
                e.stopPropagation();
                dropdown.style.display = dropdown.style.display === 'flex' ? 'none' : 'flex';
            });
            document.addEventListener('click', () => { dropdown.style.display = 'none'; });
        }
    
        dropdown.innerHTML = '';
    
        // Build Settings Menu based on Login State
        if (!token) {
            dropdown.innerHTML += `<a href="login.html" class="dropdown-item" style="padding: 12px 16px; text-decoration: none; color: var(--text-primary); font-weight: 600;">Log in</a>`;
            dropdown.innerHTML += `<a href="register.html" class="dropdown-item" style="padding: 12px 16px; text-decoration: none; color: var(--text-primary); border-bottom: 1px solid var(--border-color); margin-bottom: 4px;">Sign up</a>`;
            dropdown.innerHTML += `<a href="#" onclick="showComingSoon('Host your home')" class="dropdown-item" style="padding: 12px 16px; text-decoration: none; color: var(--text-primary); font-size: 0.95rem;">Host your home</a>`;
            dropdown.innerHTML += `<a href="#" onclick="showComingSoon('Help Center')" class="dropdown-item" style="padding: 12px 16px; text-decoration: none; color: var(--text-primary); font-size: 0.95rem;">Help</a>`;
        } else {
            const payload = parseJwt(token);
            if (payload && payload.is_admin) {
                dropdown.innerHTML += `<a href="add_place.html" class="dropdown-item" style="padding: 12px 16px; text-decoration: none; color: var(--text-primary); font-weight: 600; border-bottom: 1px solid var(--border-color);">➕ Add Place (Admin)</a>`;
                dropdown.innerHTML += `<a href="add_amenity.html" class="dropdown-item" style="padding: 12px 16px; text-decoration: none; color: var(--text-primary); font-weight: 600; border-bottom: 1px solid var(--border-color);">➕ Add Amenity (Admin)</a>`;
            }
            dropdown.innerHTML += `<a href="#" onclick="showComingSoon('Messages')" class="dropdown-item" style="padding: 12px 16px; text-decoration: none; color: var(--text-primary); font-weight: 600;">Messages</a>`;
            dropdown.innerHTML += `<a href="#" onclick="showComingSoon('Trips Bookings')" class="dropdown-item" style="padding: 12px 16px; text-decoration: none; color: var(--text-primary); font-weight: 600;">Trips</a>`;
            dropdown.innerHTML += `<a href="#" onclick="showComingSoon('Wishlists')" class="dropdown-item" style="padding: 12px 16px; text-decoration: none; color: var(--text-primary); border-bottom: 1px solid var(--border-color); margin-bottom: 4px;">Wishlists</a>`;
            dropdown.innerHTML += `<a href="#" onclick="showComingSoon('Host your home')" class="dropdown-item" style="padding: 12px 16px; text-decoration: none; color: var(--text-primary); font-size: 0.95rem;">Host your home</a>`;
            dropdown.innerHTML += `<a href="#" onclick="openAccountSettings()" class="dropdown-item" style="padding: 12px 16px; text-decoration: none; color: var(--text-primary); font-size: 0.95rem;">Account settings</a>`;
    
            const logoutLink = document.createElement('a');
            logoutLink.href = '#';
            logoutLink.className = 'dropdown-item';
            logoutLink.style = "padding: 12px 16px; text-decoration: none; color: #ef4444; border-top: 1px solid var(--border-color); margin-top: 4px; font-size: 0.95rem; font-weight: 500;";
            logoutLink.textContent = 'Log out';
            logoutLink.addEventListener('click', (e) => {
                e.preventDefault();
                document.cookie = 'token=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;';
                window.location.href = 'index.html';
            });
            dropdown.appendChild(logoutLink);
        }
    
        // Unified Hover Effects for Menu Settings
        Array.from(dropdown.children).forEach(child => {
            child.addEventListener('mouseover', () => child.style.backgroundColor = 'var(--background-color)');
            child.addEventListener('mouseout', () => child.style.backgroundColor = 'transparent');
            child.style.transition = 'background-color 0.2s ease-in';
            child.style.cursor = 'pointer';
            child.style.display = 'block';
        });
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

async function getReviewsHTML(place) {
    if (!Array.isArray(place.reviews) || place.reviews.length === 0) {
        return '<p>No reviews yet.</p>';
    }

    const reviewPromises = place.reviews.map(async (review) => {
        let reviewer = 'Anonymous';

        if (review.user && review.user.first_name) {
            reviewer = `${review.user.first_name}${review.user.last_name ? ` ${review.user.last_name}` : ''}`;
        } else if (review.user_name) {
            reviewer = review.user_name;
        } else if (review.user_id) {
            try {
                const res = await fetch(`${API_BASE}/api/v1/users/${review.user_id}`);
                if (res.ok) {
                    const userData = await res.json();
                    if (userData.first_name) {
                        reviewer = `${userData.first_name}${userData.last_name ? ` ${userData.last_name}` : ''}`;
                    } else {
                        reviewer = review.user_id;
                    }
                } else {
                    reviewer = review.user_id;
                }
            } catch (e) {
                reviewer = review.user_id;
            }
        }
        
        let stars = 'N/A';
        if (review.rating !== undefined && review.rating !== null) {
            const rawRating = Math.max(1, Math.min(5, Number(review.rating)));
            stars = '★'.repeat(rawRating) + '☆'.repeat(5 - rawRating);
        }

        return `
            <div class="review-card">
                <p>${review.comment || review.text || 'No comment provided'}</p>
                <p><strong>User:</strong> ${reviewer}</p>
                <p><strong>Rating:</strong> <span class="review-rating">${stars}</span></p>
            </div>
        `;
    });

    const htmlArray = await Promise.all(reviewPromises);
    return htmlArray.join('');
}

async function displayPlaceDetails(place) {
    const placeDetails = document.getElementById('place-details');

    if (!placeDetails) {
        return;
    }

    const amenitiesListHTML = Array.isArray(place.amenities) && place.amenities.length > 0
        ? place.amenities.map(a => {
            const name = typeof a === 'string' ? a : (a.name || 'Amenity');
            const icon = (typeof a !== 'string' && a.icon_url) ? `<img src="${a.icon_url}" style="width:20px;height:20px;margin-right:8px;vertical-align:middle;border-radius:4px" alt="icon">` : '🔹 ';
            return `<span class="amenity-tag" style="display:inline-flex;align-items:center;">${icon}${name}</span>`;
        }).join('')
        : '<span class="amenity-tag">No amenities available</span>';

    const reviewsHTML = await getReviewsHTML(place);

    let ratingText = '⭐ New (No reviews yet)';
    if (Array.isArray(place.reviews) && place.reviews.length > 0) {
        const validRev = place.reviews.filter(r => r.rating !== undefined && r.rating !== null);
        if (validRev.length > 0) {
            const total = validRev.reduce((sum, r) => sum + Number(r.rating), 0);
            ratingText = `⭐ ${(total / validRev.length).toFixed(1)} / 5.0 (${validRev.length} Reviews)`;
        }
    }

    let mapHtml = `<p class="location-tag" style="font-size: 1rem; color: var(--text-color);">📍 Coordinates: ${place.latitude ?? 'N/A'} , ${place.longitude ?? 'N/A'}</p>`;
    if (place.latitude && place.longitude) {
        const lat = Number(place.latitude);
        const lon = Number(place.longitude);
        mapHtml = `
            <div style="border-radius: var(--radius); overflow: hidden; border: 1px solid var(--border-color); margin-top: 10px;">
                <iframe width="100%" height="250" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="https://www.openstreetmap.org/export/embed.html?bbox=${lon-0.05}%2C${lat-0.05}%2C${lon+0.05}%2C${lat+0.05}&amp;layer=mapnik&amp;marker=${lat}%2C${lon}"></iframe>
            </div>
            <p class="location-tag" style="font-size: 0.9rem; margin-top: 5px;">Geographic Coordinates: ${lat.toFixed(4)}, ${lon.toFixed(4)}</p>
        `;
    }

    // Dynamic House Rules based on Place
    let houseRules = `
        <li style="margin-bottom: 8px;">🚭 No Smoking</li>
        <li style="margin-bottom: 8px;">🚫 No Pets allowed</li>
        <li style="margin-bottom: 8px;">🕰 Check-in after 3:00 PM</li>
        <li>⏰ Checkout before 11:00 AM</li>
    `;
    if (place.id === 'mock-1') {
        houseRules = `<li style="margin-bottom: 8px;">🚭 No Smoking inside (Balcony allowed)</li><li style="margin-bottom: 8px;">🐾 Pets allowed (Max 2 dogs)</li><li style="margin-bottom: 8px;">🎉 No parties or events</li>`;
    } else if (place.id === 'mock-2') {
        houseRules = `<li style="margin-bottom: 8px;">🚭 No Smoking strictly</li><li style="margin-bottom: 8px;">🐾 Pet friendly environment</li><li style="margin-bottom: 8px;">🔥 Extinguish fire before sleeping</li>`;
    } else if (place.id === 'mock-5') {
        houseRules = `<li style="margin-bottom: 8px;">🚬 Smoking allowed outdoors only</li><li style="margin-bottom: 8px;">🚫 No Pets</li><li style="margin-bottom: 8px;">⚡ Conserve solar energy during night</li>`;
    }

    placeDetails.innerHTML = `
        <div class="place-header" style="margin-bottom: 1.5rem;">
            <h1 style="font-size: 1.8rem; font-weight: 600; color: var(--text-primary); margin-bottom: 8px;">${getPlaceTitle(place)}</h1>
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div style="font-size: 1rem; color: var(--text-primary); display: flex; align-items: center; gap: 8px; font-weight: 500;">
                    <span style="font-weight: 600;">${ratingText.replace('⭐', '★')}</span>
                    <span style="color: var(--text-secondary);">·</span>
                    <span class="city-country-detail-tag" style="text-decoration: underline;">Loc: ${place.latitude ?? '0'}, ${place.longitude ?? '0'}</span>
                </div>
            </div>
        </div>
        
        <!-- Airbnb Premium 6-Image Gallery (Self-healing Broken Image Removal) -->
        <div style="display: grid; grid-template-columns: 2fr 1fr 1fr; grid-auto-rows: 200px; gap: 8px; border-radius: 16px; overflow: hidden; margin-bottom: 2rem;">
            <img src="${place.image_url || getPlaceImage(place.id, 1200, 800, 'exterior')}" style="grid-column: span 2; grid-row: span 2; width: 100%; height: 100%; object-fit: cover; cursor: zoom-in; transition: opacity 0.2s;" onerror="this.style.display='none'" onmouseover="this.style.opacity=0.9" onmouseout="this.style.opacity=1" onclick="openLightbox(this.src)" />
            <img src="${getPlaceImage(place.id, 800, 600, 'livingroom')}" style="width: 100%; height: 100%; object-fit: cover; cursor: zoom-in; transition: opacity 0.2s;" onerror="this.style.display='none'" onmouseover="this.style.opacity=0.9" onmouseout="this.style.opacity=1" onclick="openLightbox(this.src)" />
            <img src="${getPlaceImage(place.id, 800, 600, 'kitchen')}" style="width: 100%; height: 100%; object-fit: cover; cursor: zoom-in; transition: opacity 0.2s;" onerror="this.style.display='none'" onmouseover="this.style.opacity=0.9" onmouseout="this.style.opacity=1" onclick="openLightbox(this.src)" />
            <img src="${getPlaceImage(place.id, 800, 600, 'bedroom')}" style="width: 100%; height: 100%; object-fit: cover; cursor: zoom-in; transition: opacity 0.2s;" onerror="this.style.display='none'" onmouseover="this.style.opacity=0.9" onmouseout="this.style.opacity=1" onclick="openLightbox(this.src)" />
            <img src="${getPlaceImage(place.id, 800, 600, 'bathroom')}" style="width: 100%; height: 100%; object-fit: cover; cursor: zoom-in; transition: opacity 0.2s;" onerror="this.style.display='none'" onmouseover="this.style.opacity=0.9" onmouseout="this.style.opacity=1" onclick="openLightbox(this.src)" />
            <img src="${getPlaceImage(place.id, 800, 600, 'hallway')}" style="width: 100%; height: 100%; object-fit: cover; cursor: zoom-in; transition: opacity 0.2s;" onerror="this.style.display='none'" onmouseover="this.style.opacity=0.9" onmouseout="this.style.opacity=1" onclick="openLightbox(this.src)" />
        </div>
        
        <div class="place-info" style="display: grid; grid-template-columns: 2fr 1fr; gap: 40px;">
            <div class="info-main">
                <div style="display: flex; justify-content: space-between; align-items: start;">
                    <div>
                        <h2 style="font-size: 1.4rem; font-weight: 600;">Entire home hosted by ${getHostName(place)}</h2>
                        <div style="color: var(--text-secondary); margin-top: 4px; font-size: 1rem;">10 guests · 4 bedrooms · 5 beds · 3 baths</div>
                    </div>
                </div>
                
                <hr style="border: 0; border-top: 1px solid var(--border-color); margin: 2rem 0;">
                
                <h3 style="font-size: 1.3rem; margin-bottom: 12px; font-weight: 600;">About this space</h3>
                <p style="color: var(--text-secondary); line-height: 1.6; font-size: 1.05rem;">${getPlaceDescription(place)}</p>
                
                <hr style="border: 0; border-top: 1px solid var(--border-color); margin: 2rem 0;">
                
                <h3 style="font-size: 1.3rem; margin-bottom: 15px; font-weight: 600;">What this place offers</h3>
                <div class="amenities-list" style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px;">
                    ${amenitiesListHTML}
                </div>

                <hr style="border: 0; border-top: 1px solid var(--border-color); margin: 2rem 0;">
                
                <h3 style="font-size: 1.3rem; margin-bottom: 15px; font-weight: 600;">Where you'll be</h3>
                ${mapHtml}
            </div>
            
            <div class="info-sidebar">
                <div style="background: var(--surface-color); border: 1px solid var(--border-color); border-radius: 12px; padding: 20px; box-shadow: 0 6px 16px rgba(0,0,0,0.12); position: sticky; top: 100px;">
                    <div style="font-size: 1.4rem; font-weight: 600; margin-bottom: 20px;">$${getPlacePrice(place)} <span style="font-size: 1rem; color: var(--text-secondary); font-weight: 400;">night</span></div>
                    
                    <div style="border: 1px solid var(--text-secondary); border-radius: 8px; margin-bottom: 15px;">
                        <div style="display: flex; border-bottom: 1px solid var(--text-secondary);">
                            <div style="flex: 1; padding: 10px; border-right: 1px solid var(--text-secondary);">
                                <div style="font-size: 0.7rem; font-weight: bold; text-transform: uppercase;">Check-in</div>
                                <div style="font-size: 0.9rem;">Add date</div>
                            </div>
                            <div style="flex: 1; padding: 10px;">
                                <div style="font-size: 0.7rem; font-weight: bold; text-transform: uppercase;">Checkout</div>
                                <div style="font-size: 0.9rem;">Add date</div>
                            </div>
                        </div>
                        <div style="padding: 10px;">
                            <div style="font-size: 0.7rem; font-weight: bold; text-transform: uppercase;">Guests</div>
                            <div style="font-size: 0.9rem;">1 guest</div>
                        </div>
                    </div>
                    
                    <button class="btn" style="width: 100%; font-size: 1rem; font-weight: 600; margin-bottom: 20px;">Reserve</button>
                    <p style="text-align: center; color: var(--text-secondary); font-size: 0.9rem; margin-bottom: 15px;">You won't be charged yet</p>
                    
                    <hr style="border: 0; border-top: 1px solid var(--border-color); margin: 1.5rem 0;">

                    <h3 style="font-size: 1.1rem; margin-bottom: 10px; font-weight: 600;">House Rules</h3>
                    <ul style="list-style-type: none; padding: 0; margin: 0; font-size: 0.95rem; color: var(--text-secondary); line-height: 1.4;">
                        ${houseRules}
                    </ul>
                </div>
            </div>
        </div>
    `;

    // Fetch precise location name for the details page
    if (place.latitude && place.longitude) {
        fetch(`https://nominatim.openstreetmap.org/reverse?format=json&lat=${place.latitude}&lon=${place.longitude}&zoom=10`)
            .then(r => r.json())
            .then(data => {
                const city = data.address?.city || data.address?.town || data.address?.village || data.address?.county || data.address?.state || 'Unknown Location';
                const country = data.address?.country || '';
                const detailLocTag = placeDetails.querySelector('.city-country-detail-tag');
                if (detailLocTag) detailLocTag.innerHTML = `${city}${country ? ', ' + country : ''}`;
            }).catch(err => console.log(err));
    }
    placeDetails.innerHTML += `
        <div class="reviews-section" style="margin-top: 3rem;">
            <div class="reviews-header" style="margin-bottom: 20px;">
                <h3 style="font-size: 1.4rem; font-weight: 600;">Reviews</h3>
            </div>
            <div class="reviews-list" style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
                ${reviewsHTML}
            </div>
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
    if (placeId.startsWith('mock-')) {
        const place = mockPlacesData.find(p => p.id === placeId);
        if (place) {
            displayPlaceDetails(place);
            return;
        }
    }

    try {
        const response = await fetch(`${API_BASE}/api/v1/places/${placeId}`, {
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

    const response = await fetch(`${API_BASE}/api/v1/reviews/`, {
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
    const registerGuestForm = document.getElementById('register-guest-form');
    const registerAdminForm = document.getElementById('register-admin-form');
    const searchFilter = document.getElementById('search-filter');
    const addPlaceForm = document.getElementById('add-place-form');
    
    // Global Authentication Check for navigation
    checkAuthentication();

    if (addPlaceForm) {
        const token = getCookie('token');
        const payload = parseJwt(token);
        if (!payload || !payload.is_admin) {
            alert('Access denied. Admin privileges required.');
            window.location.href = 'index.html';
            return;
        }

        // Load amenities
        const amenitiesContainer = document.getElementById('amenities-container');
        fetch(`${API_BASE}/api/v1/amenities`, { headers: getAuthHeaders() })
            .then(res => res.json())
            .then(amenities => {
                amenitiesContainer.innerHTML = '';
                if (amenities && amenities.length > 0) {
                    amenities.forEach(amenity => {
                        const lbl = document.createElement('label');
                        lbl.className = 'amenity-checkbox-item';
                        lbl.innerHTML = `<input type="checkbox" name="amenity" value="${amenity.id}"> ${amenity.name}`;
                        amenitiesContainer.appendChild(lbl);
                    });
                } else {
                    amenitiesContainer.innerHTML = '<p>No amenities available.</p>';
                }
            })
            .catch(err => {
                amenitiesContainer.innerHTML = '<p>Failed to load amenities.</p>';
            });

        addPlaceForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const title = document.getElementById('place-title').value;
            const price = document.getElementById('place-price').value;
            const latitude = document.getElementById('place-latitude').value;
            const longitude = document.getElementById('place-longitude').value;
            const description = document.getElementById('place-description').value;
            const customImage = document.getElementById('place-image') ? document.getElementById('place-image').value : '';

            // Collect selected amenities
            const selectedAmenities = Array.from(document.querySelectorAll('input[name="amenity"]:checked')).map(cb => cb.value);

            try {
                const response = await fetch(`${API_BASE}/api/v1/places/`, {
                    method: 'POST',
                    headers: getAuthHeaders(),
                    body: JSON.stringify({
                        title, price: parseFloat(price), latitude: parseFloat(latitude), longitude: parseFloat(longitude), description, amenities: selectedAmenities, image_url: customImage
                    })
                });

                if (response.ok) {
                    const data = await response.json();
                    if (customImage.trim() !== '') {
                        localStorage.setItem('customImage_' + data.id, customImage);
                    }
                    alert('Place added successfully!');
                    window.location.href = 'index.html';
                } else {
                    const data = await response.json().catch(() => ({}));
                    const msg = data.error || data.message || `HTTP ${response.status}`;
                    alert(`Failed to add place: ${msg}`);
                }
            } catch (err) {
                console.error(err);
                alert('Something went wrong submitting the place.');
            }
        });
    }

    const addAmenityForm = document.getElementById('add-amenity-form');
    if (addAmenityForm) {
        const token = getCookie('token');
        const payload = parseJwt(token);
        if (!payload || !payload.is_admin) {
            alert('Access denied. Admin privileges required.');
            window.location.href = 'index.html';
            return;
        }

        addAmenityForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const name = document.getElementById('amenity-name').value;
            const iconUrl = document.getElementById('amenity-icon') ? document.getElementById('amenity-icon').value : '';
            const description = document.getElementById('amenity-description').value;

            try {
                const response = await fetch(`${API_BASE}/api/v1/amenities`, {
                    method: 'POST',
                    headers: getAuthHeaders(),
                    body: JSON.stringify({
                        name: name,
                        description: description,
                        icon_url: iconUrl
                    })
                });

                if (response.ok) {
                    alert('Amenity created successfully!');
                    window.location.href = 'index.html';
                } else {
                    const data = await response.json();
                    alert(`Failed to create amenity: ${data.message || data.error || 'Unknown error'}`);
                }
            } catch (err) {
                console.error(err);
                alert('Something went wrong submitting the amenity.');
            }
        });
    }

    if (loginForm) {
        loginForm.addEventListener('submit', async (event) => {
            event.preventDefault();

            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;

            try {
                const response = await fetch(`${API_BASE}/api/v1/users/login`, {
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

    async function handleRegistration(event, isAdmin) {
        event.preventDefault();
        
        const prefix = isAdmin ? 'admin' : 'guest';
        const firstName = document.getElementById(`${prefix}-first-name`).value;
        const lastName = document.getElementById(`${prefix}-last-name`).value;
        const email = document.getElementById(`${prefix}-email`).value;
        const password = document.getElementById(`${prefix}-password`).value;

        try {
            const response = await fetch(`${API_BASE}/api/v1/users/register`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    first_name: firstName,
                    last_name: lastName,
                    email: email,
                    password: password,
                    is_admin: isAdmin
                })
            });

            if (response.ok) {
                alert(`Registration successful as ${isAdmin ? 'Admin' : 'Guest'}! You can now log in.`);
                window.location.href = 'login.html';
            } else {
                const data = await response.json();
                alert(`Registration failed: ${data.error || 'Unknown error'}`);
            }
        } catch (error) {
            console.error(error);
            alert('Something went wrong. Please try again.');
        }
    }

    if (registerGuestForm) {
        registerGuestForm.addEventListener('submit', (e) => handleRegistration(e, false));
    }
    
    if (registerAdminForm) {
        registerAdminForm.addEventListener('submit', (e) => handleRegistration(e, true));
    }

    if (placesList) {
        fetchPlaces();

        if (priceFilter) {
            priceFilter.addEventListener('change', filterPlaces);
        }
        
        if (searchFilter) {
            searchFilter.addEventListener('input', filterPlaces);
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
                alert('Please fill out all fields before submitting.');
                return;
            }

            try {
                const response = await submitReview(token, placeId, reviewText, rating);

                if (response.ok) {
                    alert('Review submitted successfully!');
                    reviewForm.reset();
                    window.location.href = `place.html?id=${placeId}`;
                } else {
                    const data = await response.json();
                    alert(`Failed to submit review: ${data.error || data.message || 'Unknown error'}`);
                }
            } catch (error) {
                console.error(error);
                alert('Failed to submit review. Please try again later.');
            }
        });
    }

    // Theme Switcher Logic
    const toggleSwitch = document.querySelector('.theme-switch input[type="checkbox"]');
    const currentTheme = localStorage.getItem('theme');

    if (currentTheme) {
        document.documentElement.setAttribute('data-theme', currentTheme);
      
        if (toggleSwitch && currentTheme === 'dark') {
            toggleSwitch.checked = true;
        }
    }

    function switchTheme(e) {
        if (e.target.checked) {
            document.documentElement.setAttribute('data-theme', 'dark');
            localStorage.setItem('theme', 'dark');
        } else {
            document.documentElement.setAttribute('data-theme', 'light');
            localStorage.setItem('theme', 'light');
        }    
    }

    if (toggleSwitch) {
        toggleSwitch.addEventListener('change', switchTheme, false);
    }
});

// Image Lightbox Functionality
window.openLightbox = function(bgUrl) {
    if (!bgUrl) return;
    const url = bgUrl.replace(/^url\(["']?/, '').replace(/["']?\)$/, '');
    
    // Create Modal container
    const modal = document.createElement('div');
    modal.style.position = 'fixed';
    modal.style.top = '0';
    modal.style.left = '0';
    modal.style.width = '100vw';
    modal.style.height = '100vh';
    modal.style.backgroundColor = 'rgba(0, 0, 0, 0.9)';
    modal.style.zIndex = '99999';
    modal.style.display = 'flex';
    modal.style.justifyContent = 'center';
    modal.style.alignItems = 'center';
    modal.style.cursor = 'zoom-out';
    modal.style.opacity = '0';
    modal.style.transition = 'opacity 0.2s ease-in-out';
    modal.onclick = () => {
        modal.style.opacity = '0';
        setTimeout(() => document.body.removeChild(modal), 200);
    };

    // Create Image
    const img = document.createElement('img');
    img.src = url;
    img.style.maxWidth = '90%';
    img.style.maxHeight = '90%';
    img.style.borderRadius = '12px';
    img.style.boxShadow = '0 10px 40px rgba(0,0,0,0.4)';
    img.style.objectFit = 'contain';
    img.style.transform = 'scale(0.9)';
    img.style.transition = 'transform 0.2s ease-in-out';
    
    // Create Close Button
    const closeBtn = document.createElement('div');
    closeBtn.innerHTML = '✕';
    closeBtn.style.position = 'absolute';
    closeBtn.style.top = '25px';
    closeBtn.style.right = '40px';
    closeBtn.style.color = '#fff';
    closeBtn.style.fontSize = '2.5rem';
    closeBtn.style.cursor = 'pointer';
    closeBtn.style.fontWeight = 'bold';

    modal.appendChild(img);
    modal.appendChild(closeBtn);
    document.body.appendChild(modal);

    // Trigger animation
    setTimeout(() => {
        modal.style.opacity = '1';
        img.style.transform = 'scale(1)';
    }, 10);
};

// ===================================
// ACCOUNT SETTINGS & DROPDOWN INTEGRATION
// ===================================
function initAccountSettings() {
    if (document.getElementById('account-settings-modal')) return;

    const modalHTML = `
        <div id="account-settings-modal" style="display: none; position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; background: rgba(0,0,0,0.5); z-index: 10000; align-items: center; justify-content: center; backdrop-filter: blur(4px);">
            <div style="background: var(--surface-color); width: 100%; max-width: 450px; border-radius: 16px; padding: 30px; box-shadow: 0 10px 30px rgba(0,0,0,0.2); position: relative; animation: slideUp 0.3s ease-out;">
                <button id="close-account-modal" style="position: absolute; top: 15px; right: 15px; background: transparent; border: none; font-size: 1.5rem; cursor: pointer; color: var(--text-secondary);">&times;</button>
                <h2 style="margin-top: 0; color: var(--text-primary); font-size: 1.4rem; border-bottom: 1px solid var(--border-color); padding-bottom: 15px; margin-bottom: 20px;">Account Settings</h2>
                <form id="account-settings-form">
                    <div style="margin-bottom: 15px;">
                        <label style="display: block; margin-bottom: 8px; font-weight: 500; font-size: 0.95rem; color: var(--text-primary);">First Name</label>
                        <input type="text" id="acc-first-name" style="width: 100%; padding: 12px; border: 1px solid var(--border-color); border-radius: 8px; font-size: 1rem; color: var(--text-primary); background: transparent;" required>
                    </div>
                    <div style="margin-bottom: 15px;">
                        <label style="display: block; margin-bottom: 8px; font-weight: 500; font-size: 0.95rem; color: var(--text-primary);">Last Name</label>
                        <input type="text" id="acc-last-name" style="width: 100%; padding: 12px; border: 1px solid var(--border-color); border-radius: 8px; font-size: 1rem; color: var(--text-primary); background: transparent;" required>
                    </div>
                    <div style="margin-bottom: 25px;">
                        <label style="display: block; margin-bottom: 8px; font-weight: 500; font-size: 0.95rem; color: var(--text-primary);">New Password (Optional)</label>
                        <input type="password" id="acc-password" placeholder="Leave blank to keep current" style="width: 100%; padding: 12px; border: 1px solid var(--border-color); border-radius: 8px; font-size: 1rem; color: var(--text-primary); background: transparent;">
                    </div>
                    <button type="submit" style="width: 100%; padding: 14px; background: var(--primary-color); color: white; border: none; border-radius: 8px; font-size: 1.05rem; font-weight: 600; cursor: pointer; transition: opacity 0.2s;">Save Configuration</button>
                    <div id="acc-settings-msg" style="margin-top: 15px; text-align: center; font-size: 0.9rem; font-weight: 500;"></div>
                </form>
            </div>
        </div>
    `;
    document.body.insertAdjacentHTML('beforeend', modalHTML);

    document.getElementById('close-account-modal').addEventListener('click', () => {
        document.getElementById('account-settings-modal').style.display = 'none';
    });

    document.getElementById('account-settings-form').addEventListener('submit', async (e) => {
        e.preventDefault();
        const msg = document.getElementById('acc-settings-msg');
        msg.textContent = 'Saving...';
        msg.style.color = 'var(--text-secondary)';

        const fName = document.getElementById('acc-first-name').value;
        const lName = document.getElementById('acc-last-name').value;
        const pwd = document.getElementById('acc-password').value;

        const payload = { first_name: fName, last_name: lName };
        if (pwd.trim() !== '') payload.password = pwd;

        const token = getCookie('token');
        if (!token) return;
        const jwtData = parseJwt(token);

        try {
            const res = await fetch(`${API_BASE}/api/v1/users/${jwtData.sub}`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${token}`
                },
                body: JSON.stringify(payload)
            });

            if (res.ok) {
                msg.textContent = 'Settings updated successfully!';
                msg.style.color = '#10b981';
                document.getElementById('acc-password').value = '';
                setTimeout(() => { document.getElementById('account-settings-modal').style.display = 'none'; }, 1500);
            } else {
                const data = await res.json();
                msg.textContent = data.error || 'Failed to update';
                msg.style.color = '#ef4444';
            }
        } catch (err) {
            msg.textContent = 'Network Error. Check backend.';
            msg.style.color = '#ef4444';
        }
    });
}
window.openAccountSettings = async function() {
    initAccountSettings();
    const token = getCookie('token');
    const msg = document.getElementById('acc-settings-msg');
    if (msg) msg.textContent = '';
    
    document.getElementById('account-settings-modal').style.display = 'flex';
    
    // Validate JWT first
    if (!token) return;
    const jwtData = parseJwt(token);
    
    try {
        const res = await fetch(`${API_BASE}/api/v1/users/${jwtData.sub}`, {
            headers: { 'Authorization': `Bearer ${token}` }
        });
        if (res.ok) {
            const data = await res.json();
            document.getElementById('acc-first-name').value = data.first_name || '';
            document.getElementById('acc-last-name').value = data.last_name || '';
        }
    } catch(err) {
        console.error("Failed to fetch user data for pre-filling", err);
    }
};

window.showComingSoon = function(featureName) {
    alert(featureName + ' is an upcoming feature currently in development! Stay tuned!');
};
