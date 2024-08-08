# SpeakPortuEasy

SpeakPortuEasy is an innovative system designed for teachers to efficiently manage their classes and student information. Once a teacher signs up, they gain access to a comprehensive registration system where all relevant information is stored. This allows teachers to easily edit or delete records as necessary. The primary goal of SpeakPortuEasy is to simplify the process of finding information about enrollments, classes, students, and more, making classroom management straightforward and hassle-free.
You can access the live application at this link: [Live Site - SpeakPortuEay](https://speakportueasypp4-342d78e3516e.herokuapp.com/home/)

![Mock Up](https://speakportueasy.s3.amazonaws.com/media/Captura+de+tela+2024-08-08+102458.png)

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

The navigation bar in SpeakPortuEasy is designed to provide easy access to all major sections of the platform. The bar is available on all pages and adapts to smaller devices by displaying as a hamburger menu.

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

![Navbar](https://speakportueasy.s3.amazonaws.com/media/Captura+de+tela+2024-08-08+102502.png)

``USER STORY - As a teacher, I would like a home page that provides an overview of the system and easy access to its features.``

Implementation:

**Home Page**

The home page contains a hero image with the SpeakPortuEasy logo and a brief description of the website's purpose. This section immediately informs the user about the platform's function, which is to assist teachers in managing their classes and student information.

Under the description, users must log in to access the system's features. This ensures that only authenticated users can manage and view class and student information.

The home page is designed to be simple and user-friendly, providing essential information and a clear call to action for logging in.

![Welcome Section](https://speakportueasy.s3.amazonaws.com/media/Captura+de+tela+2024-08-08+102738.png)

``USER STORY - As a teacher, I want to createa simple footer``

**Implementation:**

**Footer**

A simple footer has been added to the bottom of the site. Since SpeakPortuEasy is a system for teachers to manage their work, the footer only includes essential registration information. It does not contain social media links or additional contact information, maintaining a clean and professional appearance.

![Footer](https://speakportueasy.s3.amazonaws.com/media/Captura+de+tela+2024-08-08+102508.png)

``USER STORY - As a teacher, I want to be able to create a new class so that I can organize my teaching schedule.``

**Implementation:**
**Create Class Page**

A create class page was implemented to allow teachers to create new classes via the UI without having to use the backend admin panel. This will enable teachers to quickly add new classes as needed.

![Image](https://speakportueasy.s3.amazonaws.com/media/Captura+de+tela+2024-08-08+102752.png)

``USER STORY - As a teacher, I want to be able to view the classes I have created so that I can manage them effectively.``

**Implementation:**
**View Classes Page**

A view classes page has been implemented to allow teachers to see all the classes they have created. This page includes a list of classes with relevant information and options to edit or delete each class.

![Image](https://speakportueasy.s3.amazonaws.com/media/Captura+de+tela+2024-08-08+103030.png)

``USER STORY - As a teacher, I want to be able to edit a class when updates are needed so that the information remains current.``

**Implementation:**
**Edit Class Page**

On the view classes page, an edit button was added to allow teachers to update class information when changes need to be made.

![Image](https://speakportueasy.s3.amazonaws.com/media/Captura+de+tela+2024-08-08+103037.png)

``USER STORY - As a teacher, I want to be able to delete a class when it is no longer needed so that my class list stays organized.``

**Implementation:**
**Delete Class Page**

On the view classes page, a delete button has been implemented that will take teachers to a confirmation page to allow them to delete a class. This helps maintain an up-to-date list of active classes.

![Image](https://speakportueasy.s3.amazonaws.com/media/Captura+de+tela+2024-08-08+103049.png)

``USER STORY - As a teacher, I want to be able to create a new student record so that I can manage student information.``

**Implementation:**
**Create Student Page**

A create student page was implemented with a form that takes in student details, allowing teachers to easily add new students to their classes through the UI.

![Image](https://speakportueasy.s3.amazonaws.com/media/Captura+de+tela+2024-08-08+102752.png)

``USER STORY - As a teacher, I want to be able to view student records so that I can keep track of student information.``

**Implementation:**
**View Students Page**

A view students page was implemented to show all student records. Teachers can use this page to see detailed information about each student and manage their records.

``USER STORY - As a teacher, I want to be able to edit a student record so that I can update their information as needed.``

**Implementation:**
**Edit Student Page**

On the view students page, an edit button is available that directs teachers to a form where they can update student information.

``USER STORY - As a teacher, I want to be able to delete a student record when it is no longer needed so that the student list remains accurate.``

**Implementation:**
**Delete Student Page**

A delete button was added to the view students page, allowing teachers to remove student records they no longer need.

``USER STORY - As a teacher, I want to be able to search for a specific class or student so that I can quickly find the information I need.``

**Implementation:**
**Search Box**

A search box was added to the view classes and view students pages. This allows teachers to easily locate a specific class or student by entering relevant keywords.

![Image](https://speakportueasy.s3.amazonaws.com/media/Captura+de+tela+2024-08-08+103030.png)

``USER STORY - As a teacher, I want to be notified if I try to register the same information more than once to avoid duplicates.``

**Implementation:**
**Duplicate Entry Notification**

Validation logic was added to notify teachers if they attempt to register duplicate information. This helps maintain a clean and accurate database.

**Favicon**
    * A site wide favicon was implemented.
    * This provides an image in the tabs header to allow the user to easily identify the website if they have multiple tabs open.

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

### Database-Design

The database was designed to allow CRUD (Create, Read, Update, Delete) functionality for registered users, specifically teachers, when signed in.

## The-Surface-Plane

## Design

### Colour-Scheme

- #bbdece (Light Cyan/Teal)

Feelings: Calm, refreshing, soothing.
Description: This color often evokes feelings of tranquility and peace, reminiscent of clear skies or calm waters. It can be very refreshing and is often used to create a sense of cleanliness and purity.

- #feedaa (Light Peach)

Feelings: Warmth, comfort, friendliness.
Description: Light peach is a warm and inviting color. It can create a cozy and welcoming atmosphere, making users feel comfortable and relaxed. It's often associated with a soft, nurturing environment.

- #fff8f5 (Very Light Pink/Off-White)

Feelings: Softness, innocence, simplicity.
Description: This very light pink or off-white color is delicate and subtle. It often gives a sense of purity and simplicity, and can make users feel calm and content. It's a gentle color that doesn't overwhelm, providing a serene background.

- #495551 (Dark Gray-Green)

Feelings: Stability, seriousness, sophistication.
Description: This dark gray-green color is more subdued and can evoke feelings of stability and seriousness. It has a sophisticated and professional feel to it, often used in contexts where a sense of reliability and depth is desired.

### Typography

**The Young Font**
The Young Font is a playful and modern typeface that often conveys a sense of youthfulness, creativity, and fun. It's designed to be easily readable while also adding a touch of personality and flair to the text. This type of font is ideal for projects targeting younger audiences or aiming for a fresh, dynamic feel. It can be used in headings, logos, posters, or any creative work where a more informal and engaging tone is desired. The design of "The Young Font" typically includes:

Rounded edges: To give it a soft and approachable appearance.
Varied stroke widths: Adding to the playful and casual feel.
Unique character shapes: Making it stand out and memorable.
Good readability: Despite its playful design, it remains easy to read.

**Sans-Serif Fonts**
Sans-serif fonts are a category of typefaces that do not have the small projecting features called "serifs" at the end of strokes. These fonts are known for their clean, modern, and straightforward appearance, making them highly versatile and widely used across various mediums. Characteristics of sans-serif fonts include:

Simplicity: The absence of serifs gives these fonts a sleek and minimalistic look.
Readability: They are highly legible, especially on digital screens, making them a popular choice for websites, apps, and user interfaces.
Modernity: Often associated with contemporary design, sans-serif fonts convey a sense of modernity and efficiency.
Versatility: Suitable for a wide range of applications, from body text in books and articles to headings and branding.
Uniform stroke width: Generally, the strokes in sans-serif fonts are more uniform compared to serif fonts, contributing to their clean look.

### Imagery

The Website logo was made using Canva using the Gold colour to match in with the website color scheme.

The hero image was taken from Canva pro which is a royalty free image site.


## Technolgies

##  Technology Used

### Html
 - Utilized to structure the content of the website, laying the foundation for all web pages.

### CSS
 - Custom CSS was crafted to style the website as per design specifications and wireframes, ensuring a visually appealing and responsive layout.

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

Test cases: 

### CSS

![Image](https://speakportueasy.s3.amazonaws.com/media/Captura+de+tela+2024-08-06+223836.png)

### Python

![Image](https://speakportueasy.s3.amazonaws.com/media/Captura+de+tela+2024-08-06+225908.png)
![Image](https://speakportueasy.s3.amazonaws.com/media/Captura+de+tela+2024-08-07+190003.png)
![Image](https://speakportueasy.s3.amazonaws.com/media/Captura+de+tela+2024-08-07+192851.png)
![Image](https://speakportueasy.s3.amazonaws.com/media/Captura+de+tela+2024-08-07+192932.png)
![Image](https://speakportueasy.s3.amazonaws.com/media/Captura+de+tela+2024-08-07+192948.png)
![Image](https://speakportueasy.s3.amazonaws.com/media/Captura+de+tela+2024-08-07+193104.png)
![Image](https://speakportueasy.s3.amazonaws.com/media/Captura+de+tela+2024-08-07+193329.png)

### JS

![Image](https://speakportueasy.s3.amazonaws.com/media/Captura+de+tela+2024-08-06+224609.png)
![Image](https://speakportueasy.s3.amazonaws.com/media/Captura+de+tela+2024-08-06+224945.png)

## Deployment and Local Development
The live deployed version of the website can be found on [Heroku](https://speakportueasypp4-342d78e3516e.herokuapp.com/). The following sections detail the deployment process and the technologies used. Instructions for forking or cloning the repository are also provided.

### ElephantSQL Database

The PostgreSQL Database for this project was was set up using [ElephantSQL](https://www.elephantsql.com),  which you can sign up for using your GitHub account. After signing up, follow these steps:

- Click **Create New Instance** to start a new database.
- Name used: `speakportueasy`.
- Select the **Tiny Turtle (Free)** plan.
- **Tags** can be left blank.
- Normally you select the **Region** and **Data Center** closest to you in this case EU-West-1.
- For my project, I had to select a differnt region (West-US) as this provided a newer Postgres version that was needed for my project requirements.
- Once created, click on the new database name, where you can view the database URL which will be needed for the Heroku Config Vars.

### Amazon AWS

This project uses [Amazon Web Services (AWS)](https://aws.amazon.com) to store its media and static files.

Once you've created an AWS account and logged-in, navigate to the **AWS Management Console** page & follow these series of steps to get your project connected.

#### S3 Bucket

- Search for **S3**.
- Create a new bucket, give it a name (matching your Heroku app name), and choose the region closest to you.
- Uncheck **Block all public access**, and acknowledge that the bucket will be public (required for it to work on Heroku).
- From **Object Ownership**, make sure to have **ACLs enabled**, and **Bucket owner preferred** selected.
- From the **Properties** tab, turn on static website hosting, and type `index.html` and `error.html` in their respective fields, then click **Save**.
- From the **Permissions** tab, paste in the following CORS configuration:

	```shell
	[
		{
			"AllowedHeaders": [
				"Authorization"
			],
			"AllowedMethods": [
				"GET"
			],
			"AllowedOrigins": [
				"*"
			],
			"ExposeHeaders": []
		}
	]
	```

- Copy your **ARN** string.
- From the **Bucket Policy** tab, select the **Policy Generator** link, and use the following steps:
	- Policy Type: **S3 Bucket Policy**
	- Effect: **Allow**
	- Principal: `*`
	- Actions: **GetObject**
	- Amazon Resource Name (ARN): **paste-your-ARN-here**
	- Click **Add Statement**
	- Click **Generate Policy**
	- Copy the entire Policy, and paste it into the **Bucket Policy Editor**

		```shell
		{
			"Id": "Policy1234567890",
			"Version": "2012-10-17",
			"Statement": [
				{
					"Sid": "Stmt1234567890",
					"Action": [
						"s3:GetObject"
					],
					"Effect": "Allow",
					"Resource": "arn:aws:s3:::your-bucket-name/*"
					"Principal": "*",
				}
			]
		}
		```

	- Before you click "Save", add `/*` to the end of the Resource key in the Bucket Policy Editor (like above).
	- Click **Save**.
- From the **Access Control List (ACL)** section, click "Edit" and enable **List** for **Everyone (public access)**, and accept the warning box.
	- If the edit button is disabled, you need to change the **Object Ownership** section above to **ACLs enabled** (mentioned above).

#### IAM

Back on the AWS Services Menu, search for and open **IAM** (Identity and Access Management).
Once on the IAM page, follow these steps:

- From **User Groups**, click **Create New Group**.
	- Name: `speakportueasypp4`
- Tags are optional, but you must click it to get to the **review policy** page.
- From **User Groups**, select your newly created group, and go to the **Permissions** tab.
- Open the **Add Permissions** dropdown, and click **Attach Policies**.
- Select the policy, then click **Add Permissions** at the bottom when finished.
- From the **JSON** tab, select the **Import Managed Policy** link.
	- Search for **S3**, select the `AmazonS3FullAccess` policy, and then **Import**.
	- You'll need your ARN from the S3 Bucket copied again, which is pasted into the "Resource" key on the Policy.

		```shell
		{
			"Version": "2012-10-17",
			"Statement": [
				{
					"Effect": "Allow",
					"Action": "s3:*",
					"Resource": [
						"arn:aws:s3:::your-bucket-name",
						"arn:aws:s3:::your-bucket-name/*"
					]
				}
			]
		}
		```
	
	- Click **Review Policy**.
	- Name: `speakportueasy`
	- Provide a description:
		- "Access to S3 Bucket for speakportueasy static files."
	- Click **Create Policy**.
- From **User Groups**, click `manage-speakportueasy`.
- Click **Attach Policy**.
- Search for the policy you've just created (`speakportueasy`) and select it, then click **Attach Policy**.
- From **User Groups**, click **Add User**.
	- Name: `TOBEADDED`
- For "Select AWS Access Type", select **Programmatic Access**.
- Select the group to add your new user to: `TOBEADDED`
- Tags are optional, but you must click it to get to the **review user** page.
- Click **Create User** once done.
- You should see a button to **Download .csv**, so click it to save a copy on your system.
- If you don't see an option to downlod the CSV file go to IAM and select **Users**
- Select the user for whom you wish to create a CSV file.
- Select the **Security Credentials** tab.
- Scroll to **Access Keys** and click **Create access key**
- Select **Application running outside AWS**, and click next.
- On the next screen, you can leave the **Description tag** value blank. Click **Create Access Key**.
- Click the **Download .csv file** button.
    - **IMPORTANT**: once you pass this page, you cannot come back to download it again, so do it immediately!
	- This contains the user's **Access key ID** and **Secret access key**.
	- `AWS_ACCESS_KEY_ID` = **Access key ID**
	- `AWS_SECRET_ACCESS_KEY` = **Secret access key**
- These will be needed for the Heroku Config Vars.

#### Final AWS Setup

- Follow the steps described later for [Heroku Deployment](#heroku-deployment) and then return here to follow these final AWS steps below.
- If Heroku Config Vars has `DISABLE_COLLECTSTATIC` still, this can be removed now, so that AWS will handle the static files.
- Back within **S3**, create a new folder called: `media`.
- Inside the media file select **Upload** and **Add Files**.
- Select the images from your hard-drive that you wish to upload.
- Under **Manage Public Permissions**, select **Grant public read access to this object(s)**.
- No further settings are required, so click next through to the end and **Upload**.

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com) for deployment to the web. The deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set your environment variables.

| Key | Value |
| --- | --- |
| `AWS_ACCESS_KEY_ID` | user's own value |
| `AWS_SECRET_ACCESS_KEY` | user's own value |
| `DATABASE_URL` | user's own postgres value |
| `DISABLE_COLLECTSTATIC` | 1 (*this is temporary, and can be removed for the final deployment*) |
| `EMAIL_HOST_PASS` | user's own value |
| `EMAIL_HOST_USER` | user's gmail |
| `SECRET_KEY` | user's own value |
| `STRIPE_PUBLIC_KEY` | user's own value |
| `STRIPE_SECRET_KEY` | user's own value |
| `STRIPE_WH_SECRET` | user's own value |
| `USE_AWS` | True |

Heroku needs two additional files in order to deploy properly.

- requirements.txt
- Procfile

You can install this project's **requirements** (where applicable) using:

- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file need to be updated using:

- `pip3 freeze --local > requirements.txt`

Create a **Procfile** at the root level of the project:

- Open the Procfile and enter the following line of code: `web: gunicorn app_name.wsgi:application` and save.
- *replace **app_name** with the name of your primary Django app name; the folder where settings.py is located*.

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either:

- Select **Automatic Deployment** from the Heroku app.

Or:

- Ensure Heroku is installed for these following commands to work.
- If it is not run `curl https://cli-assets.heroku.com/install.sh | sh` in the terminal/CLI.
- Then connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (replace *app_name* with your app name)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`

The project should now be connected and deployed to Heroku!

### Local Development
The steps below describe how to fork or clone the repository if desired.
#### How to Fork
1. Log in to Github.
2. Navigate to the [repository](https://github.com/MariaPadilha32/SpeakPortuEasy) for this website.
3. Click the Fork button in the top right corner.
4. You will be brought to a new page with a short form to be completed.
5. Upon completing, click on the "Create fork" button and this will create a fork of the repository in your personal account.

#### How to Clone
1. Log in to GitHub.
2. Navigate to the [repository](https://github.com/MariaPadilha32/SpeakPortuEasy) for this website.
3. Click on the **Code** button and a modal will appear.
4. Within this modal select the local tab.
5. Within this tab there are HTTPS, SSH, or GitHub CLI tabs.
6. Click on the HTTPS tab and copy the link shown.
7. In your development environment open the terminal.
8. Change the current working directory to the location where you want the cloned directory to be.
9. Type `git clone` into the terminal, then paste the URL you copied in step 6.
10. Press **Enter** to create your local clone.
11. In the terminal install the requirements by using the following: `pip3 install -r requirements.txt`.
12. If you have your own packages that have been installed, then the requirements file needs to be updated using: `pip3 freeze --local > requirements.txt`.
13. Next create the env.py file which tells our project which variables to use.
14. Add env.py the file to a .gitignore file to prevent it from being pushed to github.
15. Start the Django app: `python3 manage.py runserver`.
16. Make migrations by running : `python3 manage.py makemigrations`
17. Then migrate those changes with `python3 manage.py migrate`
18. To view the website type `python3 manage.py runserver` into the terminal and open port 8000.
19. The project is now ready to work on locally and any changes made can viewed using port 8000.

[Back to top](#contents)

## Credits

### Resources
	- The Code Institute "Hello Django and I think Therefore I blog" project was very much relied upon to build this project.

### Acknowledgements

- Most special thanks to Ger Hickey, my father-in-law, who passed away while I was working on this project. He was always an amazing support.

[Back to top](#contents)

