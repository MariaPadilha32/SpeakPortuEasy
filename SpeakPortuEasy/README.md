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
      - [Epics](#epics)
      - [User Stories](#user-stories)
  - [The-Scope-Plane](#the-scope-plane)
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

**Navigation Menu**

 The Navigation contains links for Home, Bookings, Menus and has allauth options.

The following navigation items are available on all pages:
  * Home -> index.html - Visible to all
  * Bookings (Drop Down):
    * Manage Bookings -> managebookings.html - Visible to logged in users
    * New Booking -> booking.html - Visible to logged in users
  * Menus (Drop Down):
    * View Menus -> menus.html - Visible to all
    * Create Menu -> create_menu.html - Visible to staff
    * Manage Menus -> managemenus - Visible to staff
  * Login -> login.html - Visible to logged out users
  * Register -> signup.html - Visible to logged out users
  * Logout -> logout.html - Visible to logged in users

The navigation menu is displayed on all pages and drops down into a hamburger menu on smaller devices. This will allow users to view the site from any device and not take up too much space on mobile devices.

![Navbar](docs/readme_images/navbar.PNG)

``USER STORY - As a restaurant owner, I would like a home page so that customers can view information on my restaurant``

Implementation:

**Home Page**

The home page contains a hero image of a seaside restaurant and the restaurant information at the top of the page. This will immediately make it evident to the user, what the purpose of the website is.

Under the information section are two buttons, 'Make a booking' and 'View Menus'. These buttons will allow the user a quick way to the respective pages if they wish to make a booking or view the restaurants active menus.

The last section of the home page contains a google map, marking the location of the restaurant and the opening hours of the restaurant. This will allow the user to locate the restaurant and operating times.

![Hero Image](docs/readme_images/hero.PNG)

![Welcome Section](docs/readme_images/welcome.PNG)

![Find Us](docs/readme_images/find-us.PNG)


``USER STORY - As a developer, I need to create the footer with social media links and contact information``

Implementation:

**Footer**

A footer has been added to the bottom of the site, this contains a Twitter and Facebook link so that users can follow the restaurant on social media if they want to keep up to date with special offers not advertised on the website. These icons have aria-labels added to ensure users with assistive screen reading technology know what the purpose of the links are for. They also open in new tabs as they lead users away from the site.

![Footer](docs/readme_images/footer.PNG)

``USER STORY - As a staff user, I want to be able to create a new menu when we have new dishes to offer``

Implementation:

**Create Menu Page**

A create menu page was implemented to allow staff users to create new menus via the UI without having to use the backend admin panel. This will allow staff the ability to quickly update menus when they have made changes to the food being offered.

![Create Menu](docs/readme_images/create-menu.PNG)

``USER STORY -As a user, I would like to be able to view menus so that I can decide if I would like to dine at the restaurant``

Implementation:

**View Menu Page**

A menu page has been implemented to allow users to see the current active menus and decide whether they are interested in the food we offer before booking. This is visible to all users regardless of logged in state as it is not user friendly to restrict core information from users to force them into signing up.

![View Menus](docs/readme_images/menus.PNG)

``USER STORY -As a staff user, I want to be able to edit a menu when updates are needed``

Implementation:

**Edit Menu Page**

On the manage menus page a button was added to allow staff members to edit a menu when changes need to be made.

![Edit Menu](docs/readme_images/edit-menu.PNG)

``USER STORY -As a staff member, I would like to receive feedback when I create or update menus so that I can see they have worked``

Implementation:

**Toasts**

Custom toasts were added on successful creation and deletion of menus which display success messages to the user to enable them to see that the action completed successfully.

![Menu Toasts](docs/readme_images/toast-menu.PNG)

``USER STORY -As a staff user, I want to be able to delete a menu when it is no longer used``

Implementation:

**Delete Menu Page**

On the manage menus page, a delete button has been implemented that will take staff users to a confirmation page to allow them to delete a menu. This will allow staff to delete menus when they are no longer needed

![Delete Menu](docs/readme_images/delete-menu.PNG)

``USER-STORY - As a user, I would like to be able to create a new booking when I want to visit the restaurant``

Implementation:

**Create booking page**

A booking page was implemented with a form that takes in the customer details and enables the user to easily make a booking through the UI. 

Extensive logic was added to the form validation to ensure that not only is there a table available for the users chosen time and date but also that it has enough seats for the amount of guests. If the form is successful with validation on the front end, logic is in place to find the lowest capacity table to seat the guests for the given date and time.

This allows for seat optimisation to ensure we do not have small amounts of guests at tables that could of been booked for larger groups. Ensuring table optimisation and revenue for the restaurant.

![Create Booking](docs/readme_images/create-booking.PNG)

``USER-STORY - As a user, I would like to view my bookings when I need to check the information``

Implementation:

**Manage bookings page**

A manage bookings page was implemented with validation checks on the user. This shows all of the users bookings. This will allow the user to view their upcoming bookings when needed.

For restaurant staff users, all bookings will be available to display so that staff can easily view numbers and future bookings.

![Manage Bookings](docs/readme_images/manage-bookings.PNG)

``USER-STORY - As a user, I would like to be able to edit a booking so that I can make changes when needed``

Implementation:

**Edit Booking Page**

On the manage bookings page an edit button is present that allows the user to direct to a form and update their booking when required. This will allow the user to easily manage their own booking.

For staff users, they can also edit bookings from the manage booking page, even if they did not create the reservation. This will allow restaurant staff to ammend details as needed.

![Edit Booking](docs/readme_images/edit-booking.PNG)

``USER-STORY - As a user, I would like to receive feedback when I create a booking or edit one so I know it was completed successfully``

Implementation:

**Toasts**

Custom toasts were implemented on the successful creation and editing of bookings. This will provide feedback to the user to relay information that the booking was successfully received or updated.

![Booking Toasts](docs/readme_images/booking-toast.PNG)

``USER-STORY - As a staff user, I want to be able to search a booking by reference to save time searching``

Implementation:

**Searchbox**

A search box was added to the manage bookings page that is only visible to staff users. This will allow the staff members to easily locate a booking by reference number if they need to find it quickly.

[Search Boxes](docs/readme_images/search.PNG)

``USER-STORY - As a user I would like to delete a booking when I no longer require it``

Implementation:

**Delete Booking Page**

A delete button was added to the manage bookings page that will allow customers to delete their booking should they no longer require it without the need to call the restaurant.

For staff members, they also have the abaility to delete any booking through the UI as well. This will allow staff to free up table capacity should a customer call to cancel their booking.

![Delete Booking](docs/readme_images/delete-booking.PNG)

Favicon
    * A site wide favicon was implemented.
    * This provides an image in the tabs header to allow the user to easily identify the website if they have multiple tabs open.

![Favicon](docs/readme_images/favicon.PNG)

**Error Pages**

``USER STORY - As a developer, I need to implement a 404 error page to alert users when they have accessed a page that doesn't exist``

Implementation:

**404 Page**

As a developer, I need to implement a 404 error page to redirect users to

A 404 page has been implemented and will display if a user navigates to a broken link.

The 404 page will allow the user to easily navigate back to the main website if they direct to a broken link / missing page, without the need  of the browsers back button.

``USER STORY - As a developer, I need to implement a 403 error page to alert users when accessing a page/view that they do not have permission to view``

Implementation:

**403 Page**

A 403 error page has been implemented to provide feedback to the user when they try to access unauthorized content. Users will be directed to this page if they alter the URL's and attempt to edit, delete or access pages that are restricted. 

This covers:

* Create Menu - Only authorized to staff
* Edit Menu - Only authorized to staff
* Delete Menu - Only authorized to staff
* Edit Booking - Only authorized to the customer who created the booking or a staff member
* Delete booking - Only authorized to the customer who created the booking or a staff member

``USER STORY - As a developer, I need to implement a 500 error page to alert users when an internal server error occurs``

Implementation:

**500 Page**

A 500 error page has been displayed to alert users when an internal server error occurs. The message relays to users that the problem is on our end, not theirs.

**Base Setup User Stories**

The following stories were implemented in order to set up a base structure for all the HTML pages and the core installations and configurations needed to run the application. While these do not show as individual features, they were stories completed that were needed to implement all of the stories above.

``As a developer, I need to create the base.html page and structure so that other pages can reuse the layout``

``As a developer, I need to create static resources so that images, css and javascript work on the website``

``As a developer, I need to set up the project so that it is ready for implementing the core features``

**Favicon**

A favicon was added the website to enable users to easily locate the website in the browser when multiple tabs are open.

### Features Left To Implement
- In a future release I would like to implement a page which displays a table map of the restaurant with information displayed on each table of upcoming bookings. This feature would allow staff to easily see if there are any upcoming bookings on the each table and plan accordingly. 


## The-Skeleton-Plane

### Wireframes

- Home page


![Home Page](docs/wireframes/home.JPG)


- Signup page


![Sign up Page](docs/wireframes/register.JPG)

- Log in

![Login Page](docs/wireframes/login.JPG)

- Log Out

![Logout Page](docs/wireframes/logout.JPG)

- Create Booking

![Create Booking](docs/wireframes/create_booking.JPG)

- Edit Booking 

![Edit Booking](docs/wireframes/edit_booking.JPG)

- Manage Bookings

![Manage Bookings](docs/wireframes/manage_booking.JPG)

- Delete Booking 

![Delete Booking](docs/wireframes/delete_booking.JPG)

- Create Menu 

![Create Menu](docs/wireframes/create_menu.JPG)

- Edit Menu 

![Edit Menu](docs/wireframes/edit_menu.JPG)

- View Menu 

![View Menu](docs/wireframes/view_menu.JPG)


- Manage Menus

![Manage Menu](docs/wireframes/manage_menus.JPG)

- Delete Menu 

![Delete Menu](docs/wireframes/delete_menu.JPG)

- 404 Error 

![404 Error](docs/wireframes/404.JPG)

- 403 Error 

![403 Error](docs/wireframes/403.JPG)

- 500 Error 

![500 Error](docs/wireframes/500.JPG)

**Differences to Design**

On the menu page, the original wireframe was to display the menus in a complete linear format but on larger screens this caused a lot of un-neccessary white space on smaller items like drinks and sides. A change was made to have the drinks and sides sit side-by-side on larger screens and stack as originally planned on mobiles.

### Database-Design

The database was designed to allow CRUD functionality to be available to registered users, when signed in. The user model is at the heart of the application as it is connected the the main booking and menu tables, linked by primary/foreign key relationships.

The Menu Items model holds objects that are linked to the Menu Models by a many to many relationship. This allows for staff to create menus with many menu items on.

Bookings are related to the customer (user) by a Foreign Key which allows the users to be able to view and update bookings attached to their accounts.

Entity relationship diagram was created using [DBVisualizer](https://www.dbvis.com/) and shows the schemas for each of the models and how they are related.

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

- HTML
  - The structure of the Website was developed using HTML as the main language.
- CSS
  - The Website was styled using custom CSS in an external file.
- JavaScript
  - JavaScript was used to make the custom slider on the menu page change and the bootstrap date picker.
- Python
  - Python was the main programming language used for the application using the Django Framework.
- Visual Studio Code
  - The website was developed using Visual Studio Code IDE
- GitHub
  - Source code is hosted on GitHub
- Git
  - Used to commit and push code during the development of the Website
- Font Awesome
  - This was used for various icons throughout the site
- Favicon.io
  - favicon files were created at https://favicon.io/favicon-converter/
- balsamiq
  - wireframes were created using balsamiq from https://balsamiq.com/wireframes/desktop/#
- Canva
  - This was used to create the logo in header 
- TinyPNG
  - This was used to compress the hero image for optimal load times

**Python Modules Used**

* Django Class based views (ListView, UpdateView, DeleteView, CreateView) - Used for the classes to create, read, update and delete
* Mixins (LoginRequiredMixin, UserPassesTestMixin) - Used to enforce login required on views and test user is authorized to perform actions
* messages - Used to pass messages to the toasts to display feedback to the user upon actions
* timedelta, date - Date was used in order to search for objects by date and timedelta for searching date ranges

**External Python Modules**

* cloudinary==1.29.0 - Cloundinary was set up for use but no custom uploads were made, settings remain for future development
* crispy-bootstrap5==0.6 - This was used to allow bootstrap5 use with crispy forms
* cryptography==37.0.2 - Installed as dependency with another package
* defusedxml==0.7.1 - Installed as dependency with another package
* dj-database-url==0.5.0 - Used to parse database url for production environment
* dj3-cloudinary-storage==0.0.6 - Storage system to work with cloudinary
* Django==4.0.5 - Framework used to build the application
* django-admin-rangefilter==0.8.4 - This was used to search bookings in the admin for a range between 2 dates
* django-allauth==0.51.0 - Used for the sites authentication system, sign up, sign in, logout, password resets ect.
* django-crispy-forms==1.14.0 - Used to style the forms on render
* django-model-utils==4.2.0 - Installed as dependency with another package
* gunicorn==20.1.0 - Installed as dependency with another package
* idna==3.3 - Installed as dependency with another package
* oauthlib==3.2.0 - Installed as dependency with another package
* psycopg2==2.9.3 - Needed for heroku deployment
* pycparser==2.21 - Installed as dependency with another package
* PyJWT==2.4.0 - Installed as dependency with another package
* python3-openid==3.2.0 - Installed as dependency with another package
* requests==2.27.1 - Installed as dependency with another package
* requests-oauthlib==1.3.1 - Installed as dependency with another package (allauth authentication)
* six==1.16.0 - Installed as dependency with another package
* sqlparse==0.4.2 - Installed as dependency with another package
* tzdata==2022.1 - Installed as dependency with another package
* urllib3==1.26.9 - Installed as dependency with another package
* whitenoise==6.2.0 - Used to serve static files directly without use of static resource provider like cloundinary

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

The live link can be found here: [Live Site](https://sizzle-and-steak.onrender.com/)

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

## Credits 

The [Hero Image](https://www.pexels.com/photo/people-dining-at-an-al-fresco-restaurant-by-the-sea-6446203/) was taken from pexels.


