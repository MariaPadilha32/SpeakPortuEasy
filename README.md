# SpeakPortuEasy

SpeakPortuEasy is an innovative system designed for teachers to efficiently manage their classes and student information. Once a teacher signs up, they gain access to a comprehensive registration system where all relevant information is stored. This allows teachers to easily edit or delete records as necessary. The primary goal of SpeakPortuEasy is to simplify the process of finding information about enrollments, classes, students, and more, making classroom management straightforward and hassle-free.
You can access the live application at this link: [Live Site - SpeakPortuEay](https://TOBEADD/)

![Mock Up](WEBSITE IMAGE TO BE ADD)

## Table of Contents
- [SpeakPortuEasy](#speakportueasy)
  - [Table of Contents](#table-of-contents)
- [User-Experience-Design](#user-experience-design)
  - [The-Strategy-Plane](#the-strategy-plane)
    - [Site-Goals](#site-goals)
    - [Agile Planning](#agile-planning)
      - [User Stories](#user-stories)
  - [The-Structure-Plane](#the-structure-plane)
    - [Features](#features)
    - [Features Left To Implement](#features-left-to-implement)
  - [The-Skeleton-Plane](#the-skeleton-plane)
    - [Wireframes](#wireframes)
    - [Database-Design](#database-design)
    - [Security](#security)
  - [The-Surface-Plane](#the-surface-plane)
    - [Design](#design)
    - [Colour-Scheme](#colour-scheme)
    - [Typography](#typography)
    - [Imagery](#imagery)
  - [Technolgies](#technolgies)
  - [Testing](#testing)
  - [Deployment](#deployment)
    - [Version Control](#version-control)
    - [Heroku Deployment](#heroku-deployment)
    - [Run Locally](#run-locally)
    - [Fork Project](#fork-project)
  - [Credits](#credits)
  - [Acknowledgements](#acknowledgements)

# User-Experience-Design

## The-Strategy-Plane

### Site-Goals

The site is aimed at helping language teachers, specifically those teaching English or Portuguese. Teachers can enroll students, keep track of their classes, and perform create, read, update, and delete (CRUD) operations on student and class information as needed. This ensures that teachers can easily manage their classrooms and student records efficiently.

### Agile Planning

The project was developed using agile methodologies. However, due to unforeseen circumstances in my family, I had to pause the project, which resulted in a longer-than-expected timeline for completion.

During the active development phases, I used a detailed Kanban board to manage each step of the project. The Kanban board was divided into three sections: Backlog, Pending, and Done. All user stories were meticulously detailed with expectations and acceptance criteria for each step.

The Kanban board, which can be viewed [here](https://github.com/users/MariaPadilha32/projects/6) shows the progress and detailed project cards. Each user story includes specific acceptance criteria to define the functionality required for completion.

![Kanban image](TBEADDD)

### User Stories

#### Initialization and Setup

1. Project Initialization
 - Initialize the project to set up the development environment.

2. Configuration Setup
 - Set up initial configurations to ensure the project structure is properly organized.
 
3. Main App Creation
 - Create the main app to house core functionalities.

#### Template and UI Development

1. Base HTML Template Creation
 - Create a base HTML template to ensure consistent styling across all pages.

2. Index.html Creation
 - Create the index.html page to serve as the landing page.
 
3. Template Integration and Inheritance
 - Implement and integrate templates to ensure proper layout and avoid code duplication.

#### View and URL Configuration

1. View Configuration
 - Configure views to render the correct templates.

2. URL Configuration
 - Configure URLs to route requests to appropriate views.

#### User Authentication

1. Create Login Template and Implement Login Page
 - Create and implement the login page for user authentication.

2. Authentication Features
 - Implement authentication functionalities, including password reset and user control configuration.

#### CRUD Functionalities for Different Models

1. Student Management
 - Enhance the student registration form and implement CRUD functionalities.

2. Teacher Management
 - Implement CRUD functionalities for teachers, including registration, editing, and deletion.

3. Class Management
 - Implement CRUD functionalities for classes, including registration, editing, and deletion.

4. Schedule Management
 - Implement CRUD functionalities for schedules, including registration, editing, and deletion.

5. Parent and Enrollment Management
 - Implement CRUD functionalities for parents and enrollments, including registration, editing, and deletion.

6. Zipcode Management
 - Implement CRUD functionalities for zip codes, including registration, editing, and deletion.

#### Error Handling and Notifications

1. Error Pages
 - Create error pages for 404, 403, and 500 errors to inform users of issues.

2. User Notifications
 - Implement feedback mechanisms for users during CRUD operations to ensure they are informed of successful actions.

#### Static Files and Navigation

1. Static Files Configuration
 - Configure static files to serve CSS and JavaScript correctly.

2. Navigation Links
 - Add navigation links to the nav bar for easy access to different parts of the site.

#### Miscellaneous

1. Query Functions
 - Implement query functions for different models to allow users to search and find specific data.

2. Bug Fixes and Enhancements
 - Address and correct various bugs and enhance existing functionalities to improve user experience.

3. Database Configuration
 - Configure the database to store application data.

4. Documentation
 - Complete README and testing documentation to provide comprehensive information on the project.


## The-Scope-Plane

* Responsive Design - Site should be fully functional on all devices from 320px up
* Ability to perform CRUD functionality on each on "Queries"

## The-Structure-Plane

### Features

``USER STORY - As a developer, I need to create the navbar so that users can navigate the website from any device``

Implementation:

**Navigation Bar**

The navigation menu in SpeakPortuEasy is designed to provide easy access to all major sections of the platform. The menu is available on all pages and adapts to smaller devices by displaying as a hamburger menu.

The following navigation items are available on all pages:
  * SpeakPortuEasy (goes to home) - Visible to all
  * Home (goes to home) - Visible to all
  * Register (Drop Down) - Provides options for registering different entities:
    * Register Student (register-student.html) - Visible to logged in users
    * Register Class (register-class.html) - Visible to logged in users
    * Register Classroom (register-classroom.html) - Visible to logged in users
    * Register Schedule (register-schedule.html) - Visible to logged in users
    * Register Enrollment (register-enrollment.html) - Visible to logged in users
    * Register Teacher (register-teacher.html) - Visible to logged in users
  * Query (Drop Down) - Provides options for querying different entities
    * Query Student (query-student.html) - Visible to logged in users
    * Query Class (query-class.html) - Visible to logged in users
    * Query Classroom (query-classroom.html) - Visible to logged in users
    * Query Schedule (query-schedule.html) - Visible to logged in users
    * Query Enrollment (query-enrollment.html) - Visible to logged in users
    * Query Teacher (query-teacher.html) - Visible to logged in users
  * Login -> login.html - Visible to logged out users
  * Logout -> logout.html - Visible to logged in users

The navigation bar is displayed on all pages and drops down into a hamburger menu on smaller devices. This will allow users to view the site from any device and not take up too much space on mobile devices.

![Navbar](tobeadded)

``USER STORY - As a teacher, I would like a home page that provides an overview of the system and easy access to its features.``

Implementation:

**Home Page**

The home page contains a hero image with the SpeakPortuEasy logo and a brief description of the website's purpose. This section immediately informs the user about the platform's function, which is to assist teachers in managing their classes and student information.

Under the description, users must log in to access the system's features. This ensures that only authenticated users can manage and view class and student information.

The home page is designed to be simple and user-friendly, providing essential information and a clear call to action for logging in.

![Hero Image](tobeadded)

![Welcome Section](tobeadded)

``USER STORY - As a teacher, I want to createa simple footer``

**Implementation:**

**Footer**

A simple footer has been added to the bottom of the site. Since SpeakPortuEasy is a system for teachers to manage their work, the footer only includes essential registration information. It does not contain social media links or additional contact information, maintaining a clean and professional appearance.

![Footer](tobeadded)

``USER STORY - As a teacher, I want to be able to create a new class so that I can organize my teaching schedule.``

**Implementation:**
**Create Class Page**

A create class page was implemented to allow teachers to create new classes via the UI without having to use the backend admin panel. This will enable teachers to quickly add new classes as needed.

![Image](tobeadded)

``USER STORY - As a teacher, I want to be able to view the classes I have created so that I can manage them effectively.``

**Implementation:**
**View Classes Page**

A view classes page has been implemented to allow teachers to see all the classes they have created. This page includes a list of classes with relevant information and options to edit or delete each class.

![Image](tobeadded)

``USER STORY - As a teacher, I want to be able to edit a class when updates are needed so that the information remains current.``

**Implementation:**
**Edit Class Page**

On the view classes page, an edit button was added to allow teachers to update class information when changes need to be made.

![Image](tobeadded)

``USER STORY - As a teacher, I want to be able to delete a class when it is no longer needed so that my class list stays organized.``

**Implementation:**
**Delete Class Page**

On the view classes page, a delete button has been implemented that will take teachers to a confirmation page to allow them to delete a class. This helps maintain an up-to-date list of active classes.

![Image](tobeadded)

``USER STORY - As a teacher, I want to be able to create a new student record so that I can manage student information.``

**Implementation:**
**Create Student Page**

A create student page was implemented with a form that takes in student details, allowing teachers to easily add new students to their classes through the UI.

![Image](tobeadded)

``USER STORY - As a teacher, I want to be able to view student records so that I can keep track of student information.``

**Implementation:**
**View Students Page**

A view students page was implemented to show all student records. Teachers can use this page to see detailed information about each student and manage their records.

![Image](tobeadded)

``USER STORY - As a teacher, I want to be able to edit a student record so that I can update their information as needed.``

**Implementation:**
**Edit Student Page**

On the view students page, an edit button is available that directs teachers to a form where they can update student information.

![Image](tobeadded)

``USER STORY - As a teacher, I want to be able to delete a student record when it is no longer needed so that the student list remains accurate.``

**Implementation:**
**Delete Student Page**

A delete button was added to the view students page, allowing teachers to remove student records they no longer need.

![Image](tobeadded)

``USER STORY - As a teacher, I want to be able to search for a specific class or student so that I can quickly find the information I need.``

**Implementation:**
**Search Box**

A search box was added to the view classes and view students pages. This allows teachers to easily locate a specific class or student by entering relevant keywords.

![Image](tobeadded)

``USER STORY - As a teacher, I want to be notified if I try to register the same information more than once to avoid duplicates.``

**Implementation:**
**Duplicate Entry Notification**

Validation logic was added to notify teachers if they attempt to register duplicate information. This helps maintain a clean and accurate database.

![Image](tobeadded)

**Favicon**
    * A site wide favicon was implemented.
    * This provides an image in the tabs header to allow the user to easily identify the website if they have multiple tabs open.

![Favicon]((tobeadded))

**Error Pages**

``USER STORY - As a developer, I need to implement a 404 error page to alert users when they have accessed a page that doesn't exist``

**Implementation:**
**404 Page**

A 404 error page has been implemented to display whenever a user navigates to a broken link or a missing page. This custom error page provides a user-friendly way to handle such errors, allowing users to easily navigate back to the main website.

The 404 page includes links to the home page and other key sections, so users can continue exploring the site without needing to use the browser's back button.

``USER STORY - As a developer, I need to implement a 403 error page to alert users when they try to access a page/view that they do not have permission to view.``

**Implementation:**
**403 Page**

A 403 error page has been implemented to provide feedback to users when they attempt to access unauthorized content. Users will be redirected to this page if they try to edit, delete, or view pages that are restricted based on their permissions.

This covers:

* Register Class - Only authorized for logged-in users
* Edit Class - Only authorized for logged-in users
* Delete Class - Only authorized for logged-in users
* Register Student - Only authorized for logged-in users
* Edit Student - Only authorized for logged-in users
* Delete Student - Only authorized for logged-in users
* Register Classroom - Only authorized for logged-in users
* Edit Classroom - Only authorized for logged-in users
* Delete Classroom - Only authorized for logged-in users
* Register Schedule - Only authorized for logged-in users
* Edit Schedule - Only authorized for logged-in users
* Delete Schedule - Only authorized for logged-in users
* Register Enrollment - Only authorized for logged-in users
* Edit Enrollment - Only authorized for logged-in users
* Delete Enrollment - Only authorized for logged-in users
* Register Teacher - Only authorized for logged-in users
* Edit Teacher - Only authorized for logged-in users
* Delete Teacher - Only authorized for logged-in users

``USER STORY - As a developer, I need to implement a 500 error page to notify users when an internal server error happens.``

**Implementation:**
**500 Page**

A 500 error page has been created to inform users when an internal server error occurs. This page conveys to users that the issue originates from our side, not theirs, and we are working to resolve it

**Base Setup User Stories**

The following user stories were completed to lay the groundwork for all HTML pages and ensure the necessary installations and configurations were in place to run the application. While these tasks do not stand out as individual features, they were crucial for enabling the implementation of all the functionalities mentioned earlier.

``USER STORY - As a developer, I need to create the base.html page and layout structure so that other pages can reuse the layout.``

``USER STORY - As a developer, I need to create static resources so that images, CSS, and JavaScript function properly on the website.``

``USER STORY - As a developer, I need to set up the project environment to be ready for implementing the core features.``

**Explore More User Stories**

In addition to the stories highlighted here, nearly 300 user stories have been meticulously documented and tracked on our Kanban board(https://github.com/users/MariaPadilha32/projects/6/views/1). These stories encompass the full scope of the project's development, covering all features, enhancements, and bug fixes.

To gain a comprehensive understanding of the project's depth and the full range of functionalities implemented, please explore the complete list of user stories on our Kanban board

**Favicon**

A favicon was added the website to enable users to easily locate the website in the browser when multiple tabs are open.

### Features Left To Implement
For future development, the following features are planned to enhance the functionality and user experience of SpeakPortuEasy:

- **Student Homework Uploads:** Enable students to upload their homework directly to the platform. This feature will streamline the submission process and allow teachers to easily review and grade assignments.

- **User-Friendly Attendance Tracking:** Develop a more intuitive and user-friendly page for teachers to manage student attendance. This will provide teachers with better tools to track and update attendance records efficiently.

- **Online Payment for Classes:** Implement a secure online payment system allowing students to pay for their classes directly through the platform. This feature will simplify the payment process and provide a convenient option for students to manage their class fees.


## Wireframes

- Home page


![Home Page](tobeadded)


- Signup page


![Sign up Page](tobeadded)

- Log in

![Login Page](tobeadded)

- Log Out

![Logout Page](tobeadded)

- Create Booking

![Create Booking](tobeadded)

- Edit Booking 

![Edit Booking](tobeadded)

- Manage Bookings

![Manage Bookings](tobeadded)

- Delete Booking 

![Delete Booking](tobeadded)

- Create Menu 

![Create Menu](tobeadded)

- Edit Menu 

![Edit Menu](tobeadded)

- View Menu 

![View Menu](tobeadded)


- Manage Menus

![Manage Menu](tobeadded)

- Delete Menu 

![Delete Menu](tobeadded)

- 404 Error 

![404 Error](tobeadded)

- 403 Error 

![403 Error](tobeadded)

- 500 Error 

![500 Error](tobeadded)

### Database-Design

The database was designed to allow CRUD functionality to be available to registered users, when signed in. The user model is at the heart of the application as it is connected the the main booking and menu tables, linked by primary/foreign key relationships.

The Menu Items model holds objects that are linked to the Menu Models by a many to many relationship. This allows for staff to create menus with many menu items on.

Bookings are related to the customer (user) by a Foreign Key which allows the users to be able to view and update bookings attached to their accounts.

![Entity Relationship Diagram](docs/readme_images/erd.JPG)

### Security

Views were secured by using the django class based view mixin, UserPassesTextMixin. A test function was created to use the mixin and checks were ran to ensure that the user who is trying to access the page is authorized. Any staff restricted functionality, user edit/delete functionality listed in the features was secured using this method.

Environment variables were stored in an env.py for local development for security purposes to ensure no secret keys, api keys or sensitive information was added the the repository. In production, these variables were added to the heroku config vars within the project.

## The-Surface-Plane
### Design

### Colour-Scheme

The main color schemes for the website are black ( #000000 ) ground. White font (#FFF) and the gold (#8f773c9e) was added to borders, button text and hover affects to add a hint of color to the website.

### Typography

The Roboto font was used throughout the website. This font is from google fonts and was imported into the style sheet.

### Imagery

The Website logo was made using Canva using the Gold colour to match in with the website color scheme.

The hero image was taken from Pexels which is a royalty free image site.


## Technolgies

##  Technology Used

### Html
 - Utilized to structure the content of the website, laying the foundation for all web pages.

### CSS
 - Custom CSS was crafted to style the website as per design specifications and wireframes, ensuring a visually appealing and responsive layout.

### JavaScript
 - Implemented to add interactivity and enhance user experience, such as enabling the menu on the index.html page and setting timeout functions for messages.

### Python
 -  The primary programming language used to handle backend logic, including processing data and handling requests.

### Django
 -  A front-end framework used alongside Django to facilitate design and development, ensuring the website is responsive and mobile-friendly.

### Font Awesome
 -  An icon library integrated into the navigation bar and footer to improve the visual appeal and usability of the website with various icons.

### Bootstrap 
 - A front-end framework used alongside Django to streamline the design and development process, ensuring a responsive and mobile-friendly layout.

### GitHub
 - Used for storing the project's code and managing version control. It also hosted the project's Kanban board to track progress and manage tasks.

### Heroku
 - A cloud platform leveraged to host and deploy the website, making it accessible online.

### ElephantSQL
 - A cloud-based PostgreSQL database service used to store and manage the project's data.

### Git
- A version control system utilized to track changes in the project's source code, enabling collaboration and maintaining a history of modifications.

### AWS S3 and IAM
- Employed to host static and media files for the project, with IAM managing permission-based roles for accessing the S3 buckets.

### Canva
- This was used to create the logo in header 

### Django-Crispy-Forms
- A Django application used to enhance the styling of forms, providing a more user-friendly and aesthetically pleasing form interface.

**Python Modules Used**

* Django Class based views (ListView, UpdateView, DeleteView, CreateView) - Used for the classes to create, read, update and delete
* messages - Used to pass messages to the toasts to display feedback to the user upon actions
* timedelta, date - Date was used in order to search for objects by date and timedelta for searching date ranges

**External Python Modules**

asgiref==3.7.2
* Description: ASGI (Asynchronous Server Gateway Interface) reference implementation. It provides utilities and a reference implementation of the ASGI specification, which is the successor to WSGI for Python web applications. It is used for handling asynchronous web applications.
* Usage: This is often used in Django projects to enable asynchronous capabilities.

dj-database-url==0.5.0
* Description: Allows the configuration of the Django database via a single environment variable.
* Usage: It is useful for setting up database configurations in deployment environments, particularly when working with Heroku.

Django==5.0.2
* Description: A high-level Python web framework that encourages rapid development and clean, pragmatic design.
* Usage: The main framework your application is built on, providing the core functionality and structure.

django-heroku==0.3.1
* Description: Django-Heroku integrates Django with Heroku’s environment settings, including database configuration, static files, and logging.
* Usage: Simplifies the deployment of Django applications on Heroku by automatically configuring settings.

gunicorn==20.1.0
* Description: A Python WSGI HTTP Server for UNIX, which serves your Django application.
* Usage: Used as a production-grade server to run Django applications, especially when deployed on platforms like Heroku.

mysql-connector-python==8.2.0
* Description: MySQL Connector for Python is a standardized database driver for Python platforms and development.
* Usage: Used for connecting to MySQL databases, providing a Pythonic interface to execute SQL commands and manage database connections.

mysqlclient==2.2.4
* Description: A MySQL database connector for Python that is a fork of the MySQLdb library.
* Usage: Another option for connecting to MySQL databases, often preferred for its performance and compatibility with Django.

protobuf==4.21.12
* Description: Protocol Buffers are a method developed by Google for serializing structured data, similar to XML or JSON.
* Usage: Used for serializing structured data, typically for communication protocols, data storage, and more.

psycopg2==2.9.9
* Description: PostgreSQL database adapter for Python.
* Usage: Required for connecting and interacting with PostgreSQL databases from a Django application.

setuptools==69.1.0
* Description: A package development and distribution library. It provides enhancements to the Python standard library’s distutils.
* Usage: Essential for building and distributing Python packages, and often required for installing other Python packages.

sqlparse==0.4.4
* Description: A non-validating SQL parser for Python.
* Usage: Used by Django and other applications for parsing and formatting SQL queries.

tzdata==2023.4
* Description: Time zone database for Python.
* Usage: Provides up-to-date time zone information, used by applications to manage time zones.

whitenoise==6.5.0
* Description: WhiteNoise allows your web app to serve its own static files, making it a self-contained unit that can be deployed anywhere.
* Usage: Simplifies serving static files (like CSS, JavaScript, images) in a Django application, particularly useful in production environments.


## Testing

Test cases and results can be found in the [TESTING.md](TESTING.md) file. This was moved due to the size of the file.

## Deployment

### Version Control

The site was created using the Visual Studio Code editor and pushed to github to the remote repository ‘Gars-Steakhouse’.

The following git commands were used throughout development to push code to the remote repo:

```git add <file>``` - This command was used to add the file(s) to the staging area before they are committed.

```git commit -m “commit message”``` - This command was used to commit changes to the local repository queue ready for the final step.

```git push``` - This command was used to push all committed code to the remote repository on github.

### Heroku Deployment

The site was deployed to Heroku. The steps to deploy are as follows:

- Navigate to heroku and create an account
- Click the new button in the top right corner
- Select create new app
- Enter app name
- Select region and click create app
- Click the resources tab and search for Heroku Postgres
- Select hobby dev and continue
- Go to the settings tab and then click reveal config vars
- Add the following config vars:
  - SECRET_KEY: (Your secret key)
  - DATABASE_URL: (This should already exist with add on of postgres)
  - EMAIL_HOST_USER: (email address)
  - EMAIL_HOST_PASS: (email app password)
  - CLOUNDINARY_URL: (cloudinary api url)
- Click the deploy tab
- Scroll down to Connect to GitHub and sign in / authorize when prompted
- In the search box, find the repositoy you want to deploy and click connect
- Scroll down to Manual deploy and choose the main branch
- Click deploy

The app should now be deployed.

The live link can be found here: [Live Site](TOBEADDED)

### Run Locally

Navigate to the GitHub Repository you want to clone to use locally:

- Click on the code drop down button
- Click on HTTPS
- Copy the repository link to the clipboard
- Open your IDE of choice (git must be installed for the next steps)
- Type git clone copied-git-url into the IDE terminal

The project will now have been cloned on your local machine for use.

### Fork Project

Most commonly, forks are used to either propose changes to someone else's project or to use someone else's project as a starting point for your own idea.

- Navigate to the GitHub Repository you want to fork.

- On the top right of the page under the header, click the fork button.

- This will create a duplicate of the full project in your GitHub Repository.

### Resources
	- The Code Institute "Hello Django and I think Therefore I blog" project was very much relied upon to build this project.

### Acknowledgements

- Most special thanks to Ger Hickey, my father-in-law, who passed away while I was working on this project. He was always an amazing support.

[Back to top](#contents)

