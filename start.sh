#!/bin/bash
gunicorn sentiment_project.wsgi:application
