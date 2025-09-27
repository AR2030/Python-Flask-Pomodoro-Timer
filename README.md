# Python Flask Pomodoro Timer

A web-based Pomodoro Timer application built with Flask that helps users manage their time and track productivity through the Pomodoro Technique.

## Features

- **User Authentication**: Secure user registration and login system
- **Project Management**: Create and manage multiple projects
- **Pomodoro Timer**: 25-minute work sessions with 5-minute breaks
- **Cycle Tracking**: Automatic counting of completed Pomodoro cycles
- **History Tracking**: Save and view completed work sessions for each project
- **Responsive Design**: Clean, user-friendly interface using W3.CSS framework

## How It Works

The application follows a simple workflow:

1. **Register** - Create a new user account
2. **Login** - Access your personalized dashboard
3. **Add Project** - Create projects to work on
4. **Select Project** - Choose which project to focus on
5. **Timer** - Start the Pomodoro timer (25 min work, 5 min break)
6. **Save History** - Record completed cycles to track progress

## Technology Stack

- **Backend**: Python Flask
- **Database**: SQLite with Flask-SQLAlchemy ORM
- **Authentication**: Flask-Login with bcrypt password hashing
- **Forms**: Flask-WTF for form handling and validation
- **Frontend**: HTML5, CSS3, JavaScript
- **UI Framework**: W3.CSS with Font Awesome icons
- **Responsive Design**: Bootstrap components

## Project Structure

```
pomodoroTimer/
├── __init__.py          # Flask app initialization
├── models.py            # Database models (User, Project)
├── routes.py            # Application routes and views
├── forms.py             # WTF forms for user input
├── static/
│   ├── css/
│   │   └── main.css     # Custom styles
│   ├── js/
│   │   └── main.js      # Timer functionality
│   └── clock-multi-size.ico
└── templates/           # HTML templates
    ├── index.html       # Home page
    ├── login.html       # Login form
    ├── register.html    # Registration form
    ├── addProject.html  # Add project form
    ├── selectProject.html # Project selection
    ├── timer.html       # Pomodoro timer interface
    └── history.html     # Session history
```

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/AR2030/Python-Flask-Pomodoro-Timer.git
   cd Python-Flask-Pomodoro-Timer
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   
   **Alternative manual installation**:
   ```bash
   pip install flask flask-sqlalchemy flask-bcrypt flask-login flask-wtf wtforms
   ```

4. **Initialize the database** (first time only):
   ```bash
   python3 -c "from pomodoroTimer import app, db; app.app_context().push(); db.create_all()"
   ```

5. **Run the application**:
   ```bash
   python run.py
   ```

6. **Access the application**:
   Open your web browser and navigate to `http://localhost:5000`

## Troubleshooting

### Common Issues

1. **Import Errors**: If you encounter import errors related to Flask-WTF or Werkzeug versions, try:
   ```bash
   pip install Flask==2.2.5 Flask-WTF==1.0.1 Werkzeug==2.3.7
   ```

2. **Database Issues**: If the app fails to start due to database issues, delete the `pomodoroTimer/data.sqlite` file and reinitialize:
   ```bash
   rm pomodoroTimer/data.sqlite
   python3 -c "from pomodoroTimer import app, db; app.app_context().push(); db.create_all()"
   ```

3. **Port Already in Use**: If port 5000 is busy, modify `run.py` to use a different port:
   ```python
   if __name__ == '__main__':
       app.run(debug=True, port=5001)
   ```

## Screenshots

### Home Page
The landing page provides an overview of how the Pomodoro Timer works with a clean, user-friendly interface.

### Timer Interface
- Clean countdown display showing work time (25:00) and break time (05:00)
- Start, Pause, and Reset controls
- Cycle counter to track completed Pomodoro sessions
- Save functionality to record progress

### Project Management
- Add new projects to organize your work
- Select active project before starting timer sessions
- View history of completed cycles per project

## Demo

To quickly test the application:

1. Register a new account with any valid email format
2. Create a test project (e.g., "Learn Flask")
3. Select the project and start your first Pomodoro session
4. Use the timer controls to experience the workflow

## Features in Detail

### Timer Functionality
- **Work Session**: 25-minute focused work period
- **Break Period**: 5-minute rest interval
- **Auto-cycle**: Automatically transitions from work to break
- **Manual Controls**: Start, pause, and reset at any time
- **Progress Tracking**: Visual cycle counter shows completed sessions

### User Management
- **Secure Registration**: Password hashing with bcrypt
- **Session Management**: Flask-Login handles user sessions
- **Form Validation**: Server-side validation for all user inputs
- **Personalized Experience**: Each user has their own projects and history

### Getting Started
1. Visit the homepage and click "Register" to create a new account
2. After registration, log in with your credentials
3. Add your first project by clicking "Add Project"
4. Select the project you want to work on
5. Start your first Pomodoro session!

### Timer Controls
- **Start**: Begin the timer countdown
- **Pause**: Temporarily stop the timer
- **Reset**: Reset timer to default values (25:00 work, 05:00 break)
- **Reset and Save to History**: Complete your session and save progress

### Tracking Progress
- View your completed cycles in the "History" section
- Each project tracks the total number of Pomodoro cycles completed
- Monitor your productivity over time

## Database Models

### User Model
- `id`: Primary key
- `username`: Unique username (2-20 characters)
- `email`: Unique email address
- `password`: Bcrypt hashed password
- `projects`: One-to-many relationship with Project model

### Project Model
- `id`: Primary key
- `title`: Project name
- `cyclesDone`: Number of completed Pomodoro cycles
- `user_id`: Foreign key to User model

## API Endpoints

- `GET /` - Home page
- `GET|POST /register` - User registration
- `GET|POST /login` - User login
- `GET /logout` - User logout
- `GET|POST /addProject` - Create new project
- `GET|POST /selectProject` - Select active project
- `GET|POST /timer` - Pomodoro timer interface
- `GET /history` - View session history
- `POST /saveProjectToHistory` - Save completed cycles (AJAX)

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## About the Pomodoro Technique

The Pomodoro Technique is a time management method developed by Francesco Cirillo in the late 1980s. It uses a timer to break work into intervals, traditionally 25 minutes in length, separated by short breaks. This application implements the classic Pomodoro timing:

- **Work Session**: 25 minutes of focused work
- **Short Break**: 5 minutes of rest
- **Cycle Tracking**: Count completed work sessions

This technique can help improve focus, reduce mental fatigue, and maintain consistent productivity throughout the day.