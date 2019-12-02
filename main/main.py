#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sanic import Sanic
from sanic_session import InMemorySessionInterface
from sanic_jinja2 import SanicJinja2
from sanic import response


app = Sanic()

# Serves files from the static folder to the URL /static
app.static('/static', './static')

jinja = SanicJinja2(app)
session = InMemorySessionInterface(cookie_name=app.name, prefix=app.name)


@app.middleware("request")
async def add_session_to_request(request):
    # before each request initialize a session
    # using the client's request
    await session.open(request)


@app.middleware("response")
async def save_session(request, response):
    # after each request save the session,
    # pass the response to set client cookies
    await session.save(request, response)


@app.route("/")
async def index(request):
    request["flash"]("success message", "success")
    request["flash"]("info message", "info")
    request["flash"]("warning message", "warning")
    request["flash"]("error message", "error")
    request["session"]["user"] = "session user"
    return jinja.render("index.html", request, greetings="Hello, sanic!")

# @app.route("/blog")
# async def blog(request):
#     return response.json({'message': 'Hello world!'})
    # request["flash"]("success message", "success")
    # request["flash"]("info message", "info")
    # request["flash"]("warning message", "warning")
    # request["flash"]("error message", "error")
    # request["session"]["user"] = "session user"
    # return jinja.render("single.html", request, greetings="Hello, sanic!")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000, debug=True)
