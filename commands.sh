#!/bin/bash
help() {
    printf "Available commands:\n- init\n- start_server\n"
}

init() {
    source webdev/Scripts/activate
    python manage.py runserver
}

start_server() {
    python manage.py runserver
}