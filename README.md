# API Rest to convert number to number in extensive

API Rest to received a number (between -99999 and 99999) and convert to number in extensive

## Table of Contents

* [Requirements](#requirements)
* [Setup](#setup)
* [Running](#running)
* [Running with Shell](#running-with-shell)
* [Code Documentation](#code-documentation)
* [Code Analysis](#code-analysis)
* [Execute Unit Test](#execute-unit-test)
* [Accessing API URLs](#accessing-api-urls)
    * [Convert number](#convert-number)

## Requirements

To run this project, you need to install the [Docker](https://docs.docker.com/install/) and [Docker Compose](https://docs.docker.com/compose/install/).

## Setup

To set up the container, you need to execute:

```console
docker-compose build
```

This command will build the container follow the steps in ```Dockerfile```.

## Running

You can run the job with the command:

```console
docker-compose up
```

This command will start the API Rest.

## Running with Shell

To run with shell, you need to execute:

```console
docker-compose run --service-ports api sh
```

After that, you can execute all make commands. So, if you want to run the API you need to execute:

```console
make run
```

## Code Documentation

If you want to see the documentation of code, you need to execute the following command after run the container with shell:

```console
make docs
```

Now, you can access the code documentation opening the file ```docs/build/index.html```

## Code Analysis

If you want to analyze your python code that was written inside the ```src``` folder, you need to execute the following command after run the container with shell:

```console
make lint
```

## Execute Unit Test

If you want to execute the unittest, you need to execute the following command after run the container with shell:

```console
make tests
```

## Accessing API URLs

To access the URLs of API, you can use the command line [curl](https://curl.haxx.se/) or the [Postman](https://www.getpostman.com/)

### Convert number

To convert a number to number in extensive, you need execute the following example:

```console
curl -X GET http://127.0.0.1:5000/99999
```