# URL Shortener Microservice

## What is this?

A URL shortener service built on Flask, providing both an API and a graphical frontend.

You can find it deployed [here](https://briefly-url.herokuapp.com/).

### Example creation usage

```url
https://briefly-url.herokuapp.com/new/https://www.google.com
https://briefly-url.herokuapp.com/new/http://foo.com:80
```

### Example creation output

```json
{ "original_url":"http://foo.com:80",
  "short_url":"https://briefly-url.herokuapp.com/8170" }
```

### Usage

```url
https://briefly-url.herokuapp.com/2871
```

### Will redirect to

```url
https://www.google.com/
```

## Project Specs

This was originally built to satisfy the requirements of FreeCodeCamp's URL Shortener Microservice project.

You can find those requirements [here](https://www.freecodecamp.org/challenges/url-shortener-microservice).