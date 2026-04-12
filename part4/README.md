# HBnB part 4 - Simple Web Client 

## 📌 Project Overview
This project is the fourth phase of a full-stack application, focusing on building a client-side web interface that interacts with a previously developed back-end API.

In previous phases, the backend API was developed using Flask, including models, business logic, and RESTful endpoints.
In this phase, the focus shifts to building a client-side web application that interacts with this API.

This phase completes the system by enabling real user interaction with the API.

## 🎯 Project Objectives

The main objectives of this phase are:

 - Design a clean, structured, and user-friendly interface
 - Connect the front-end with back-end services using API calls
 - Implement secure authentication using JWT stored in cookies
 - Build a responsive and dynamic web application
 - Enhance user experience using client-side rendering

## 🏗️ Application Architecture

🔄 Flow of the System

  1- User interacts with UI (form, button, filter)
  
  2- JavaScript captures the event
  
  3- Request is sent to the API
  
  4- API processes and returns JSON response
  
  5- UI updates dynamically without reload

## 🧩 Tasks Implementation

### Task 0: Design (UI Structure & Styling)

In this task, we completed and structured all required HTML pages and applied styling using CSS.

### Implementation Details
- Created the main pages:
  - `login.html`
  - `index.html`
  - `place.html`
  - `add_review.html`
- Used semantic HTML5 elements such as:
  - `<header>`, `<nav>`, `<main>`, `<footer>`
- Built reusable UI components:
  - Place Cards (`place-card`)
  - Review Cards (`review-card`)
- Designed consistent layout:
  - Header with logo and navigation links
  - Footer with “All rights reserved”
- Applied required styling rules:
  - Margin: 20px
  - Padding: 10px
  - Border: 1px solid #ddd
  - Border radius: 10px

### Outcome
A clean, structured, and user-friendly interface that matches the design requirements and is ready to be connected with JavaScript logic.

### Task 1: Login Functionality

We implemented user authentication by connecting the login form with the backend API.

### Implementation Details
- Added event listener to the login form
- Prevented default form submission using:
```bash
event.preventDefault();
```
- Sent a POST request to the login endpoint:
```bash
fetch('/login', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ email, password }) });
```
- Handled API response:
  - On success:
    - Stored JWT token in cookies
    - Redirected user to `index.html`
  - On failure:
    - Displayed error message

### Outcome
A fully functional login system that securely authenticates users and manages sessions.

### Task 2: List of Places (Index Page)

We implemented the main page that displays all available places dynamically.

### Implementation Details
- Checked authentication status using cookies:
   - Show login link if not authenticated
   - Hide it if authenticated
- Fetched places data from API using:
```bash
fetch('/places', {
  headers: {
    Authorization: `Bearer ${token}`
  }
});
```
- Dynamically created place cards using JavaScript:
   - Name
   - Price per night
   - "View Details" button
- Implemented client-side filtering:
   - Dropdown with price options (10, 50, 100, All)
   - Used JavaScript to show/hide cards without reload

### Outcome
A dynamic homepage that displays places and allows users to filter results instantly.

### Task 3: Place Details

We built a page to display detailed information about a selected place.

### Implementation Details
- Extracted `place_id` from URL using:
```bash
window.location.search
```
- Fetched place details from API
- Displayed:
   - Name
   - Description
   - Price
   - Amenities
   - Reviews
- Rendered reviews dynamically using review cards
- Controlled visibility of "Add Review":
   - Visible only if user is authenticated

### Outcome
A fully dynamic details page that presents complete information about a place and adapts based on user authentication.

### Task 4: Add Review

We implemented a form that allows authenticated users to submit reviews.

### Implementation Details
- Checked authentication on page load:
   - If not authenticated → redirect to index.html
- Extracted place_id from URL
- Added event listener to review form
- Sent POST request to API:
```bash
fetch('/reviews', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    Authorization: `Bearer ${token}`
  },
  body: JSON.stringify({
    place_id: placeId,
    text: reviewText
  })
});
```
- Handled response:
  - Success → show confirmation + clear form
  - Failure → show error message

### Outcome
A secure and functional review system integrated with the backend API.

## Conclusion
In this phase, we successfully built a complete front-end client that interacts with a backend API.

We implemented:
- Authentication system
- Dynamic data rendering
- Client-side filtering
- Secure review submission

This project demonstrates a real-world example of integrating front-end and back-end systems into a fully functional web application.

---

# Our HBnB Website

### The login/sign up page:

![WhatsApp Image 2026-04-11 at 20 11 51 (1)](https://github.com/user-attachments/assets/44bf7dee-7d7f-4efa-85bb-48e906ac5909)

![WhatsApp Image 2026-04-11 at 20 11 52](https://github.com/user-attachments/assets/e894425b-6110-4695-b2d3-b03018e978f6)

![WhatsApp Image 2026-04-11 at 20 11 52 (1)](https://github.com/user-attachments/assets/cd5ea865-5651-4b05-a5a2-905331f361b1)

---

### The main page:

![WhatsApp Image 2026-04-11 at 20 11 51](https://github.com/user-attachments/assets/a2802c7b-b5ff-4615-a1ec-436c7fc6a669)

---

### Submitting new review:

![WhatsApp Image 2026-04-11 at 20 11 53](https://github.com/user-attachments/assets/e0d29196-a605-4b9e-8266-4377712bae64)

---

### Listing the reviews "Admin POV":

![WhatsApp Image 2026-04-11 at 20 17 49 (1)](https://github.com/user-attachments/assets/3a7a4db3-193f-4a1c-b931-621f9778a4a7)

Note: The admin can't review it's place 

---

### Adding new place "by the admin':

![WhatsApp Image 2026-04-11 at 21 12 12](https://github.com/user-attachments/assets/f56b3aa7-288a-4b9b-9ceb-c3ea43b381cc)

![WhatsApp Image 2026-04-11 at 21 12 12 (1)](https://github.com/user-attachments/assets/3bb17f0c-dfbf-4f3f-909c-bcb3dcc819ff)

![WhatsApp Image 2026-04-11 at 21 12 13](https://github.com/user-attachments/assets/1524e482-b4a8-4c0d-a48e-3f4282933646)

---

### Place details:

![WhatsApp Image 2026-04-11 at 22 05 45](https://github.com/user-attachments/assets/69362dce-cfa1-4cc7-a5c9-13aefbb066ee)

![WhatsApp Image 2026-04-11 at 22 09 21](https://github.com/user-attachments/assets/98c6ebd4-ef93-457d-b880-d3ee8af84664)

---

### The price Filter:

![WhatsApp Image 2026-04-11 at 22 05 44](https://github.com/user-attachments/assets/28122aa3-5236-45dd-973f-78189699b336)

---
### Authors
- Solaf Alessa
- Rabea Thabit
- Hamsa Alammar 
