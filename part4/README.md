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

### Task 1: Design (UI Structure & Styling)

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

### Task 2: Login Functionality

We implemented user authentication by connecting the login form with the backend API.

### Implementation Details
- Added event listener to the login form
- Prevented default form submission using:
event.preventDefault();
- Sent a POST request to the login endpoint:
fetch('/login', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ email, password }) });










