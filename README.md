# Twitter Streaming Pipeline

## About this service
This service uses [Twitter’s streaming API](https://developer.twitter.com/en/docs/tutorials/consuming-streaming-data) to stream tweets filtering some subjects: `formula 1, f1, formula1`
For every tweet look up for pilot names, and team names and save the outputs into CSV files:
The outputs are:

```
A CSV file with raw data received.
A CSV with drivers names, aggregated by mentions.
A CSV with team names, aggregated by mentions and drivers name.
A CSV with tweets aggregated by country.
```

This repository already contains some data streamed within a 60-minutes time frame from Twitter.

## Getting Started

Before you start getting your hands dirty it's important that you learn the concepts behind the code structure.

Our architecture is based on `Clean Architecture`, if you want to get into the details about this architecture
you can take a look at [Robert C. Martin's blog post](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html).

As mentioned, our architecture is _based_ on `Clean Architecture` so there are some minor differences, this is how the files should be organized:

```
src/
    commom/
    extractor/
    handlers/
    loader/
    logger/
    transformer/
tests/
    unit/
```

## Prerequisites

These instructions will get you a copy of the service up and running on your local machine for development and testing purposes.

Make sure you have all the following prerequisites:

### Python

This service uses Python version 3.8. To download and install the version got to the python page [here](https://www.python.org/downloads/).


### Install libraries

This project uses third parthies python libs.
Make sure you have it all installed in your enviroment.

```
pip install -r requirements.txt
```

## How to execute

Before run the commands you will need to store your Bearer Token inside `src/commom/config.py` file on get_config() method.

To execute the services, use [IPython](https://ipython.readthedocs.io/en/stable/)
After install the requirements, on root folder type `ipython` and run the following commands

### Stream data
```
In [1]: from src.handlers.stream_data import main

In [2]: main()
```

### Aggregate data
```
In [1]: from src.handlers.aggregate_data import main

In [2]: main()
```
