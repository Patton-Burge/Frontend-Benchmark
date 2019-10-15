# Guestbook - Server Rendered Frontend Benchmark

In this project you will demonstrate your ability to work as a frontend
developer with HTML/CSS/JS inside a small Django project.

The project is a simple guestbook application where a user can do 4 things:

- View the latest entries
- View the top (most liked) entries
- Create a new entry
- Like an entry

I've provided the backend code for the project. You're responsible
for building the HTML, CSS, and JS required for the UI.

## The Backend - What Is Provided

### Models - What Is My Data

The core of this application is the `Entry` model. Any time our we talk about
an `Entry`, we mean an object with the following attributes:

- `id` - A unique identifier for that `Entry`
- `content` - The text content for that `Entry`
- `likes` - The number of likes that the `Entry` has received
- `created_at` - The datetime when the `Entry` was created

### URLs

The backend exposes 6 URLs, but you only really care about 4 of them:

- `entries/` renders a template named `latest_entries.html`. The template
  is provided a variable named `entries` which is an iterable (you can loop
  over it) of `Entry` objects. The `entries` variable is ordered most recent
  to least recent. Your page should:
  - Display the `content` and `likes` for each `Entry`.
  - Display a link to `entries/create`.
  - Display a "Like" button that uses `fetch` to make a `POST` request to
    `entries/<int:id>/like`. When the response gets back from the server,
    update the DOM to reflect the updated `likes`.
- `entries/top` is exactly the same as `entries/` but it uses a template named
  `top_entries.html` and the backend orders the `entries` variable from most
  liked to least liked.
- `entries/create` renders a template named `create_entry.html`. The template
  should display a form that `POST`s to `entries/create` with a single input
  named `content`. The input should be a `textarea`. The form should not allow
  the user to submit an empty `textarea`.
- `entries/<int:id>/like` does not render a template because it is an API
  endpoint. It expects a `POST` request with an empty body. It will add 1
  to the likes of the `Entry` identified by the `id` provided in the path.
  It responds with a JSON object with a single property, `likes`. It contains
  an updated value for the number of likes for the specified `Entry`.

## The Frontend - Your Job

Roughly, your job is use the backend to make sure that the user can do the
4 things listed at the top of this document:

- View the latest entries
- View the top (most liked) entries
- Create a new entry
- Like an entry

Of course, checking those boxes is only part of the work. You should make
sure:

- Your UI is designed with a user in mind. Just because it is technically
  possible doesn't mean that it is pleasant for a human being.
- Your code is written with readers in mind. You might not work on this code
  after submission, but an employer might read it.

### Skills Required

- HTML/CSS Basics (content covered in the static site benchmark)
- HTML Form Basics
- Django Template Language
- JS Basics
- DOM Manipulation
- Responding to Events in JS
- Using `fetch` and `Promise`s in JS

## Getting Started

After setting up your repository you need to set up the database by running
the following command:

    $ python3 manage.py migrate

After this you can start the server and get to work!

    $ python3 manage.py runserver

## Submission

- **All work due by the 4:30 PM Friday October 18.**
- **You should push at least 1 commit per workday.**
