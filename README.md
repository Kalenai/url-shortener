# URL Shortener Microservice

## What is this?

A URL shortener service built on Flask, satisfying the requirements for FreeCodeCamp's URL Shortener Microservice project using Python.

Additionally, I plan to add a graphical frontend version along with the API.

## Project Specs

<https://www.freecodecamp.org/challenges/url-shortener-microservice>

### User stories

* I can pass a URL as a parameter and I will receive a shortened URL in the JSON response.

* When I visit that shortened URL, it will redirect me to my original link.

### Example creation usage

```url
https://little-url.herokuapp.com/new/https://www.google.com
https://little-url.herokuapp.com/new/http://foo.com:80
```

### Example creation output

```json
{ "original_url":"http://foo.com:80",
  "short_url":"https://little-url.herokuapp.com/8170" }
```

### Usage

```url
https://little-url.herokuapp.com/2871
```

### Will redirect to

```url
https://www.google.com/
```