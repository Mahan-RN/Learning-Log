# Learning-Log :snake::earth_americas:
A Python-based web application made with Django that allows users to journal and
track new things that they have learned.

# 1- Introduction
Learning Log is a simple web application that allows users to create an account 
and log their learning activities. It allows users to organize their journal into
different topics, which can then have different learning events associated with them.
This project is based on Python Crash Course (3rd edition) [1].

<img src="readme_resources\learning_log_preview.png" width="700"/>

# 2- User Manual :page_facing_up:
To sign up and create your own learning log:

**1-** Sign up by creating an account

<img src="readme_resources\user_registration.png" width="700"/>

**2-** View topics by clicking on "Topics" on the top left

<img src="readme_resources\selecting_topics.png" width="700"/>

**3-** Log your learnings related to to a new topic by clicking on "Add a new topic"

<img src="readme_resources\new_topic.png" width="700"/>

**4-** You can add new entries to each topic by selecting that topic and clicking 
on "Add new entry". You can edit each entry by selecting "edit entry"

<img src="readme_resources\adding_entries.gif" width="700"/>

**5-** You can logout and sign back in anytime you want!

# 3- Learning & Reflections
Here's what I've learned and what I can improve on in my future projects.
## Learning:
The main purpose of this project was for me to become more familiar with Python and
Django framework. Here I practiced and learned:

- Gained experience with MVT architecture (Model-View-Template) as implemented in Django
- Employed Django’s admin interface to manage app content
- Deployed locally using `runserver` and practiced using virtual environments for dependency management
- Implemented basic user authentication and session management with Django’s built-in tools
- Practiced using template inheritance and Django’s built-in URL routing system
- This project helped me understand the importance of regular commits and tracking changes

## Reflection:
I made this project following Python Crash Course [1] step-by-step guide. As a 
computer science student, these are some things that I think can be improved
and will increase the overall quality of the project:

- **Becoming more familiar with Django:** this was just the tip of the iceberg and there
is so much that I need to read and study to really understand how Django works 
(under the hood) and how I can use it to its full potential

- **Unit tests:** unit tests are critical for any project (any code really)

- **Deployment:** I haven't deployed this project yet. I want to learn best practices
for deploying web applications

- **Database management:** this project uses SQLite. I want to become more familiar
with how to manage databases and other database options.

# 4- Resources
**[1]** Matthes, E. (2023). Python crash course: a hands-on, project-based introduction 
to programming. 3rd edition. No Starch Press.