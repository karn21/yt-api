# yt-api  [![Build Status](https://travis-ci.org/karn21/yt-api.svg?branch=master)](https://travis-ci.org/karn21/yt-api)

![Dashboard](https://github.com/karn21/yt-api/blob/master/etc/dashboard-screenshot.png)

## Local setup
1. Clone this repository.
2. Create a virtual env.
3. Install dependencies using pip

    `pip install -r requirements.txt`
4. Run migrate command

    `python manage.py migrate`
5. Start development server

    `python manage.py runserver`
6. Start background tasks using(Run this command simultaneously in a new terminal).

    `python manage.py process_tasks`
    
7. Visit http://localhost:8000/dashboard in your browser to view dashboard or use postman for testing apis.

