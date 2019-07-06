The Intek Movie Friday Night Poll
=================================

The Intek Movie Friday Night Poll is a simple Django app to conduct Web-based polls.

Quick start
-----------

1. Add "IntekMovieFridayPoll" to your INSTALLED_APPS setting like this:

```
    INSTALLED_APPS = [
        ...
        'IntekMovieFridayPoll',
    ]
```

2. Include the polls URLconf in your project `urls.py` like this:

```djangourlpath
    path('IntekMovieFridayPoll/', include('IntekMovieFridayPoll.urls')),
```

3. Run `python manage.py migrate` to create the polls models.

4. Start the development server and visit http://localhost:8000/admin/ to create a poll (you'll need the Admin app enabled).

5. Visit http://localhost:8000/ to participate in the poll.