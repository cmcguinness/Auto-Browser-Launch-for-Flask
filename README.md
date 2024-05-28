# Auto Browser, Auto Port Flask App
When building a desktop app using Flask, there are two problems that plague me:

1. Port 5000 on my Mac is often in use by something else.
2. I have to click the link to launch the browser.

This ultra simple script solves both problems. It launches the browser automatically and uses a random port number.

The code has been tested on MacOS, Windows 11, and Linux (Ubuntu).

The only caveat is that you have to start the app like:

```bash
python3 app.py
```

Instead of:

```bash
flask run
```
