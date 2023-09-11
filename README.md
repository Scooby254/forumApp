# Django Forums Project

This Django Forums project is a web application designed to create an interactive and user-friendly discussion platform. It leverages the Django framework to handle various functionalities like user authentication, forum/post creation and commenting.

## Features

- **User Authentication**: Users can create accounts, log in, and log out. Authentication is used to track user activity and enable features like posting and commenting.

- **Forum/Post Creation**: Users can create new forums, each with a specific topic or theme. These forums act as containers for discussions.

- **Post/Forum Commenting**: Users can participate in discussions by creating posts or by commenting on existing posts.

- **User Profiles**: Each user has a profile page where they can update their profile details.

- **Search Functionality**: Users can search for specific posts using keywords.

- **Moderator Capabilities**: Certain users can be assigned as moderators with the ability to manage forums.

## Getting Started

### Prerequisites

- Python (>=3.6)
- Django (>=3.1)
- [Other dependencies listed in requirements.txt]

### Installation

1. Clone this repository to your local machine.

```bash
git clone https://github.com/Scooby254/forumApp.git
```

2. Create a virtual environment and activate it.

```bash
python3 -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`
```

3. Install the project dependencies.

```bash
pip install -r requirements.txt
```

4. Apply the database migrations.

```bash
python manage.py migrate
```

5. Create a superuser for admin access.

```bash
python manage.py createsuperuser
```

6. Start the development server.

```bash
python manage.py runserver
```

The application should now be running locally at `http://localhost:8000`.

## Usage

1. Navigate to `http://localhost:8000` in your web browser.
2. Create a new account.
3. Explore existing forums, create new ones, and or participate in discussions.
4. Moderators can access the admin interface at `http://localhost:8000/admin` to manage forums/posts, comments and users.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For any questions or feedback, please contact us at [jeremihmuuo@gmail.com](mailto:jeremihmuuo@gmail.com).

---
