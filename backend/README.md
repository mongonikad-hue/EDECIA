# EDECIA Django Backend

A professional Django + Django REST Framework backend for the EDECIA website with a complete content management system.

## Project Structure

```
backend/
├── edecia/                    # Django project configuration
│   ├── settings.py           # Project settings
│   ├── urls.py               # URL routing
│   ├── wsgi.py               # WSGI application
│   └── asgi.py               # ASGI application
├── content/                  # Django app for content management
│   ├── models.py             # Database models (Service, BlogPost, AboutPage)
│   ├── views.py              # API views
│   ├── serializers.py        # DRF serializers
│   ├── permissions.py        # Custom permissions (IsAdminOrReadOnly)
│   ├── admin.py              # Django admin configuration
│   ├── tests.py              # Unit tests
│   └── migrations/           # Database migrations
├── templates/                # HTML templates
│   └── edecia/              # Template files
├── static/                   # Static files (CSS, JS, images)
│   ├── css/                  # Stylesheets
│   ├── js/                   # JavaScript files
│   └── images/               # Images and logos
├── media/                    # User-uploaded files (images, documents)
├── manage.py                 # Django management command
├── db.sqlite3               # SQLite database (development only)
├── requirements.txt         # Python dependencies
├── .gitignore              # Git ignore rules
└── README.md               # This file
```

## Setup & Installation

### 1. Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run Migrations

```bash
python manage.py migrate
```

### 4. Load Sample Data

```bash
python manage.py seed_content
```

### 5. Create Admin User

```bash
python manage.py createsuperuser
```

### 6. Run Development Server

```bash
python manage.py runserver
```

Server will be available at: `http://127.0.0.1:8000`

## Admin Access

- **URL:** http://127.0.0.1:8000/admin/
- Use the superuser credentials created during setup

## API Endpoints

### Services
- `GET /api/services/` - List all services (public)
- `POST /api/services/` - Create service (admin only)
- `GET /api/services/<id>/` - Get service details (public)
- `PUT/PATCH /api/services/<id>/` - Update service (admin only)
- `DELETE /api/services/<id>/` - Delete service (admin only)

### Blog Posts
- `GET /api/blog/` - List all blog posts (public)
- `POST /api/blog/` - Create blog post (admin only)
- `GET /api/blog/<id>/` - Get blog post details (public)
- `PUT/PATCH /api/blog/<id>/` - Update blog post (admin only)
- `DELETE /api/blog/<id>/` - Delete blog post (admin only)

### About Page
- `GET /api/about/` - Get about page content (public)
- `PUT /api/about/` - Update about page (admin only)

## Models

### Service
- `title` - CharField
- `description` - TextField
- `price` - CharField (optional)
- `duration` - CharField (optional)
- `image` - ImageField (optional)
- `created_at`, `updated_at` - Timestamps

### BlogPost
- `title` - CharField
- `slug` - SlugField (unique)
- `content` - TextField
- `image` - ImageField (optional)
- `author` - ForeignKey to User (optional)
- `created_at`, `updated_at` - Timestamps

### AboutPage
- Singleton pattern - only one instance exists
- `content` - TextField
- `updated_at` - Timestamp

## Permissions

- **Public Users:** Can read services, blog posts, and about page
- **Admin Users (`is_staff=True`):** Can create, read, update, and delete all content

Permission logic is implemented in `content/permissions.py` using `IsAdminOrReadOnly`.

## Testing

Run the test suite:

```bash
python manage.py test
```

## Static Files for Production

Collect static files for production deployment:

```bash
python manage.py collectstatic --noinput
```

This creates the `staticfiles/` directory with all compiled static assets.

## Database

The project uses SQLite for development (`db.sqlite3`). For production, configure a proper database (PostgreSQL, MySQL, etc.) in `settings.py`.

## Notes

- All timestamps are in UTC
- Slug fields are auto-generated from titles
- About page uses singleton pattern (pk=1)
- CORS is enabled for all origins (adjust in production)
