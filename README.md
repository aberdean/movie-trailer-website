# Movie Trailer Website Project

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/36de46ee51764ad2a3df78a6abfa0082)](https://www.codacy.com/app/aberdean/movie-trailer-website)
[![Maintainability](https://api.codeclimate.com/v1/badges/cb6137214b19210a76b1/maintainability)](https://codeclimate.com/github/aberdean/movie-trailer-website/maintainability)

## Table of Contents

* [Introduction](#introduction)

* [Instructions](#instructions)

## Introduction

This is a project I built for the Udacity Full Stack Web Developer Nanodegree.
The fresh_tomatoes.py file is written by Udacity. The pop_movies.py is written
by me.

## Instructions

To run this project, it is necessary to have the json and requests libraries
installed. They can be installed with pip as follows:

```
pip install json
pip install requests
```

The movies are fetched from The Movie Database (TMDb). It is necessary to have
an API key to fetch the movies. To obtain an API key,

* Sign up on [TMDb](https://www.themoviedb.org/account/signup)
* Go to the [Settings page](https://www.themoviedb.org/settings/api) to request
  an API key

Once you have an API key,

* Enter your API key in the pop_movies.py file, where indicated (on line 8)
* Run pop_movies.py