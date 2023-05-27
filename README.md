# GeoDB-Web-Backend-Development

A web application for processing geospatial data and interacting with databases to enable functionality related to geolocation and spatial data analysis.

## Features
* Get Places List: The application allows retrieving a list of all places from the database.
* Create New Place: Users can create new place records by providing the name, description, and coordinates.
* Update Place Information: The application enables updating information for existing places, including the name, description, and coordinates.
* Delete Place: Users can delete place records from the database.
* Find Nearest Place to a Given Point: The application provides the ability to find the nearest place to a specified point by passing the coordinates as query parameters.

All API requests return responses in JSON format. You have created documentation for the API, explaining how to use each endpoint and describing the request parameters and response format.

## Installation

Python3 must be already installed

The project needs to be launched directly in Docker, and all configurations will be automatically generated.

```shell
git https://github.com/evgenijmartynuk07/GeoDB-Web-Backend-Development.git
cd GeoDB_Web_Backend_Development
create .env based on .env.sample
docker-compose up
```

```shell
1. register new user -> api/user/register/
2. get token -> api/user/token/
3. test project -> api/doc/swagger/
```