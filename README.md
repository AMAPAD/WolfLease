# WolfLease

[![DOI](https://zenodo.org/badge/884969191.svg)](https://doi.org/10.5281/zenodo.14226956)
![App Version](https://img.shields.io/badge/version-v3.0-blue)
![Status](https://img.shields.io/badge/status-active--development-green)
![Run Tests](https://img.shields.io/badge/tests-passing-brightgreen)
[![Coverage Status](https://coveralls.io/repos/github/AMAPAD/WolfLease/badge.svg?branch=master)](https://coveralls.io/github/AMAPAD/WolfLease?branch=master)
[![Autopep8 Code Check](https://github.com/AMAPAD/WolfLease/actions/workflows/autopep8.yml/badge.svg)](https://github.com/AMAPAD/WolfLease/actions/workflows/autopep8.yml)
[![PyLint Code Check](https://github.com/AMAPAD/WolfLease/actions/workflows/pylint.yml/badge.svg)](https://github.com/AMAPAD/WolfLease/actions/workflows/pylint.yml)
[![Flake8 Lint](https://github.com/AMAPAD/WolfLease/actions/workflows/flake8.yml/badge.svg)](https://github.com/AMAPAD/WolfLease/actions/workflows/flake8.yml)
[![Django CI](https://github.com/AMAPAD/WolfLease/actions/workflows/django.yml/badge.svg)](https://github.com/AMAPAD/WolfLease/actions/workflows/django.yml)

<a href="https://opensource.org/licenses/MIT">![GitHub](https://img.shields.io/github/license/AMAPAD/WolfLease)</a>&nbsp;&nbsp;
![GitHub top language](https://img.shields.io/github/languages/top/AMAPAD/WolfLease)&nbsp;&nbsp; <a href="https://github.com/AMAPAD/WolfLease/issues">
![GitHub issues](https://img.shields.io/github/issues/AMAPAD/WolfLease)</a>&nbsp;&nbsp; <a href="https://github.com/AMAPAD/WolfLease/issues?q=is%3Aissue+is%3Aclosed">
![GitHub closed issues](https://img.shields.io/github/issues-closed/AMAPAD/WolfLease)</a>&nbsp;&nbsp;

## Table of Contents

- [Description](#description)
- [Built With](#built-with)
- [Getting Started](#getting-started)
- [WolfLease Endpoints](#wolflease-endpoints)
- [Searching through Models](#searching-through-models)
- [Roadmap](#roadmap)
- [Credits](#credits)
- [New Case Studies](#new-case-studies)

## Description

<br>

Finding apartments on a lease can be a difficult and time-consuming task. We can sublease a room to save time, possibly rent, and enjoy the benefits of a shorter lease time. WolfLease is an application to help people find Apartments offering rooms on sublease and move in faster! WolfLease allows us to search for flats based on location, facilities, sublease start and end dates, etc.

Project IDEA Video :
https://drive.google.com/file/d/1So9pzp7Hglt7QMxl0QJm10g9hcy8bAR-/view?usp=drive_link

Project Workflow Demo :
https://drive.google.com/file/d/1UIDhQFq20Ftor684CyYbFY8sy3HyM18s/view?usp=drive_link

Project Brainrot Video :
https://pdftobrainrot.org/share/103258316980824109809_1732676755941

- ## Built with

  <img src = "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original-wordmark.svg" width="40" height="40"/>
  <img src = "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain-wordmark.svg" width="40" height="40"/>

- **Language used:** Python
- **Libraries used:** Django
- **Libraries used:** Streamlit

## Getting started:

- ### Prerequisite:

  - Download [Python3.11](https://www.python.org/downloads/) on your system.

- ### Run Instructions

  **TRADITIONAL SETUP:**

  - Clone [this (Wolflease) github repo](https://github.com/sumeetkhillare/WolfLease).

  - Navigate to project directory.

  - Create a virtual environment:

    `python -m venv project_env`

  - Activate the virtual environment:

    `source project_env/bin/activate`

  - Build the virtual environment:

    `pip install -r requirements_v2.txt`

  - Run:

    `python manage.py runserver`

    `streamlit run app.py`

  - Site will be hosted at:
    `http://127.0.0.1:8000/`

    `http://127.0.0.1:3000`

    **DOCKER SETUP:**

  - Clone the repository:

  ```bash
  git clone https://github.com/subodh30/WolfLease.git
  cd WolfLease
  ```

  - Build and run with Docker Compose:

  ```bash
  docker compose up --build
  ```

  This will:

  - Start the MariaDB database
  - Launch the Django backend API (available at http://localhost:8000)
  - Start the Streamlit frontend (available at http://localhost:8501)

## 🚀 What's New in Version 2.0

We're excited to introduce a suite of powerful new features designed to revolutionize your subleasing experience!

### 🏠 For Room Seekers:

- **Comprehensive Flat Finder**: Explore our extensive database of available subleases with just a few clicks.
- **Smart Filtering**: Pinpoint your perfect home using our advanced criteria-matching and date-based availability filters.
- **Roommate Match**: Discover compatible roommates through our different profiles on portal based on personalized preferences.
- **In-Depth Property Insights**: Access detailed information about flats and their owners to make informed decisions.
- **Know Your Rights**: Stay informed with our dedicated tenant rights resource page.
- **Seamless User Experience**: Enjoy a smooth, secure authentication process for hassle-free access to all features.

### 🏢 For Property Owners:

- **Effortless Listing Management**: Showcase your properties to a wide audience with our user-friendly listing tool.
- **Digital Lease Signing**: Streamline your paperwork with our convenient online lease signing feature.
- **Property Management Hub**: Take control with a comprehensive dashboard for managing properties and visualizing key data.

### 💼 For All Users:

- **All-in-One Platform**: Experience our newly designed website, offering a centralized hub for all your subleasing needs.
- **Intuitive Dashboard**: Gain valuable insights and manage your activities with our sleek, information-rich user interface.

Discover the future of subleasing with Wolflease 2.0 – Where finding your perfect space or tenant is just a click away!

## WolfLease Endpoints

#### Admin page

| HTTP Method | URL                          | Description |
| ----------- | ---------------------------- | ----------- |
| `GET`       | http://localhost:8000/admin/ | Admin page  |

#### Owner

| HTTP Method | URL                                    | Description        |
| ----------- | -------------------------------------- | ------------------ |
| `POST`      | http://localhost:8000/owners           | Create new Owner   |
| `PUT`       | http://localhost:8000/owners/{ownerId} | Update Owner by ID |
| `GET`       | http://localhost:8000/owners           | Get all Owners     |
| `DELETE`    | http://localhost:8000/owners/{ownerId} | Delete Owner by ID |

#### Apartment

| HTTP Method | URL                                            | Description            |
| ----------- | ---------------------------------------------- | ---------------------- |
| `POST`      | http://localhost:8000/apartments               | Create a new Apartment |
| `PUT`       | http://localhost:8000/apartments/{apartmentID} | Update Apartment by ID |
| `GET`       | http://localhost:8000/apartments               | Get all Apartments     |
| `DELETE`    | http://localhost:8000/apartments/{apartmentID} | Delete Apartment by ID |

#### Lease

| HTTP Method | URL                                   | Description        |
| ----------- | ------------------------------------- | ------------------ |
| `POST`      | http://localhost:8000/lease           | Create a new Lease |
| `PUT`       | http://localhost:8000/lease/{LeaseID} | Update Lease by ID |
| `GET`       | http://localhost:8000/lease           | Get all lease      |
| `DELETE`    | http://localhost:8000/lease/{LeaseID} | Delete Lease by ID |

#### Flat

| HTTP Method | URL                                  | Description       |
| ----------- | ------------------------------------ | ----------------- |
| `POST`      | http://localhost:8000/flats          | Create a new Flat |
| `PUT`       | http://localhost:8000/flats/{flatID} | Update Flat by ID |
| `GET`       | http://localhost:8000/flats          | Get all Flats     |
| `DELETE`    | http://localhost:8000/flats/{flatID} | Delete Flat by ID |

#### User

| HTTP Method | URL                                  | Description       |
| ----------- | ------------------------------------ | ----------------- |
| `POST`      | http://localhost:8000/users          | Create a new User |
| `PUT`       | http://localhost:8000/users/{userID} | Update User by ID |
| `GET`       | http://localhost:8000/users          | Get all Users     |
| `DELETE`    | http://localhost:8000/users/{userID} | Delete User by ID |

#### Interested

| HTTP Method | URL                                          | Description           |
| ----------- | -------------------------------------------- | --------------------- |
| `POST`      | http://localhost:8000/interests              | Create a new Interest |
| `PUT`       | http://localhost:8000/interests/{interestID} | Update Interest by ID |
| `GET`       | http://localhost:8000/interests              | Get all Interests     |
| `DELETE`    | http://localhost:8000/interests/{interestID} | Delete Interest by ID |

## Searching through Owners, Apartments, Lease, Flats, User Models

| HTTP Method | URL                                                   | Description                                                    |
| ----------- | ----------------------------------------------------- | -------------------------------------------------------------- |
| `GET`       | http://localhost:8000/owners?search={email}           | Search for an Owner with given email                           |
| `GET`       | http://localhost:8000/owners?search={contact_number}  | Search for an Owner with given contact number                  |
| `GET`       | http://localhost:8000/apartments?search={address}     | Search for Apartments by address                               |
| `GET`       | http://localhost:8000/apartments?search={facilities}  | Search for Apartments with different facilities of your choice |
| `GET`       | http://localhost:8000/apartments?search={owner}       | Search for Apartments by owner                                 |
| `GET`       | http://localhost:8000/lease?search={lease_end_date}   | Search for Lease by end date                                   |
| `GET`       | http://localhost:8000/lease?search={lease_start_date} | Search for Lease by start date                                 |
| `GET`       | http://localhost:8000/flats?search={availabilty}      | Search for Flats that are available                            |
| `GET`       | http://localhost:8000/flats?search={rent_per_room}    | Search for Flats by rent amount                                |
| `GET`       | http://localhost:8000/users?search={email}            | Search for an User with given email                            |
| `GET`       | http://localhost:8000/users?search={contact_number}   | Search for a User with given contact number                    |

## Roadmap

- [List of Roadmap features](https://github.com/sumeetkhillare/WolfLease/issues?q=is%3Aopen+is%3Aissue)

## WolfLease V3 by Group 08

Team Members:

1. Ashwattha Phatak
2. Anish Mulay
3. Akshay Dongare

## WolfLease V2 by Group 44

Team Members:

1. Shashank Ajit Walke
2. Sumeet Bapurao Khillare
3. Xiaoqin Pi

## Credits

Project : WolfLease forked from https://github.com/subodh30/WolfLease

[Subodh Gujar](https://github.com/subodh30)

[Ameya Vaichalkar](https://github.com/ameyagv)

[Rohan Shiveshwarkar](https://github.com/RoninS28)

[Kunal Patil](https://github.com/kunalpatil1810)

[Yash Sonar](https://github.com/Yash-567)

## New Case Studies

### 1. Sarah, a young professional moving to a new city, is looking for the perfect roommate. She uses Wolflease 2.0 to leverage the power of LLMs in finding compatible roommates through the Profile Matching section:

- Using the Roommate Match feature, Sarah creates a detailed profile, including her preferences for living arrangements, lifestyle, and budget.
- The Profile Matching section uses LLM-powered algorithms to suggest potential roommates who share similar interests, habits, and living preferences.
- Sarah connects with matched roommates and finds someone who aligns with her lifestyle and expectations.

**Potential Outcome:** Sarah successfully finds a compatible roommate, making her relocation process smoother and more efficient.

### 2. Alex, a prospective renter, is considering multiple flats and wants to make an informed decision by reading reviews from previous tenants. He uses Wolflease 2.0 to add and view reviews:

- Alex adds a review for a flat he's lived in previously, sharing his thoughts on the living experience, amenities, and overall satisfaction.
- He then browses the reviews for currently available flats, which helps him gauge the living conditions, owner responsiveness, and neighborhood dynamics.
- The Review Section enables Alex to make an informed decision based on the shared experiences of other tenants.

**Potential Outcome:** Alex can confidently choose the best flat based on genuine reviews, while also contributing valuable feedback to the community.
