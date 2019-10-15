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

### What Is My Data

The core of this application is the `Entry` model. Any time our we talk about
an `Entry`, we mean an object with the following attributes:

- `id` - A unique identifier for that `Entry`
- `content` - The text content for that `Entry`
- `likes` - The number of likes that the `Entry` has received
- `created_at` - The datetime when the `Entry` was created

### URLs

The backend exposes 6 URLs, but you only really care about 4 of them:

- `entries/` renders a template named `latest_entries.html`
- `entries/top`
- `entries/create`
- `entries/<int:id>/like`
