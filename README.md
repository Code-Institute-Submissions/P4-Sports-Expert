# **Sports Expert**

## **Overview**

Sports expert is a sports blog website where users can make blog posts about a specific sport, view blog posts by other users and
comment on blog posts. They can also edit their profile and upload their own profile picture aswell as adding information about themselves.

Developed by Sean Johnston for code institute Project Portfolio project 4.

## **Project Goals**

As my fourth project for the [Code Institute](https://codeinstitute.net/) 5P course the goal of the project is to demostrate all of the skills I have learned in the course so far including languages such as HTML, CSS, Javascript and Python. Frameworks such as Django and Boostrap and version control technologies such as Git and Github.

## **UX**

## **The Strategy Plane**

Sports expert was designed to be a site for Sports lovers to share and read their own and other peoples opinions on multiple sports topics. The site was designed in a way that it is easy to navigate, and a homepage U.I that grabs new and returning users attention. Users can upload their own BlogPosts, comment on other users blogposts aswell as editing their own profile which is intended to create a proper website community.

### **Target Users**

- A user that is a sports fan
- A user that likes to keep up to date with sports news
- A user that wants to create their own blogpost on a sport topic
- A user that wants to join in with the community and comment on other peoples blogposts or start a discussion.

### **Site Goals**

- For users to be able to create an account, login and logout when they want.
- For users to be able to view blogposts regardless if they have made and account and are signed in or out
- For users to be able to create their own blogposts while logged in.
- For users to be able to comment on their own and other peoples blogposts while logged in
- For users to be able to edit their profile including adding thier own profile picture while logged in.

## **Agile Planning**

This project was built using the Agile method throughout by creating EPIC Miletones which were broken down into smaller user stories with labels "must-have", "should-have", "could-have", and wont have. 

Epics milestones were given Acceptance criterias and the must haves were completed first to complete the milestone. Any user stories that were not completed were moved back into the project backlog.

The Kanban board was created using Github projects and can be located [here](https://github.com/users/seanj06/projects/5/views/1)  and can be viewed to see the completed and backlogged user stories.

![Kanban Board](docs/readme-images/kanban-board.png)

### **Epics**

Epics were broken down into 9 EPIC Milestones(including backlog)
which include 37 user stories in total. Each Milestone was given acceptance criteria and the milestone was closed when all the criteria had been met / all user stories were completed.
User stories were given tasks, and when each task and the given user stories were completed a comment was left with the commit number underneath the user story. When all tasks were complete the user story was closed.

#### **EPIC: Django Installation and app setup [#Milestone 1](https://github.com/seanj06/P4-Sports-Expert/milestone/1?closed=1)**

This Epic had 3 acceptance criterias

- Acceptance criteria 1: Django insalled to gitpod workspace and new project created

- Acceptance criteria 2: Install postresql database

- Acceptance criteria 3: Create new app inside project

This was the first milestone to be completed as it was needed to install django and the database.

#### **EPIC: First Heroku Deployment [#Milestone 2](https://github.com/seanj06/P4-Sports-Expert/milestone/2?closed=1)**

This Epic included 2 user stories which included installing cloudinary and the setting up the correct env.py variables to successfully deploy the prpject on heroku for the first time.

#### **EPIC: Home page creation [#Milestone 3](https://github.com/seanj06/P4-Sports-Expert/milestone/8)**

This Epic had 4 acceptance criterias

- Acceptance criteria 1: Users are brought to homepage when first entering the site

- Acceptance criteria 2:Users can log in and out from the navbar

- Acceptance criteria 3: What users see on the home page differs depending on if they are logged in or out

- Accpetance criteria 4: Users are shown a list of most recent blogs on page

This epic centred around the site home page and made sure user athentication was set up correctly

#### **EPIC: User profile [#Milestone 4](https://github.com/seanj06/P4-Sports-Expert/milestone/10)**

This Epic had 3 acceptance criterias

- Acceptance criteria 1: Users are able to go to profile section from home page

- Acceptance criteria 2: Users can upload own image for their profile aswell as add a quick bio

- Acceptance criteria 3: Users can see all of their blog posts from profile section

This epic centered around the users profile section including users being able to access profile page from the home page and edit and see their own blog posts from their profile page.

#### **EPIC: Crud Functionality [#Milestone 5](https://github.com/seanj06/P4-Sports-Expert/milestone/5?closed=1)**

This epic had 4 user stories all based around CRUD functionality

- User able to Read a blog post

- User able create a blog post

- User able to update a blog post

- User able to delete a blog post

#### **EPIC: Blog view page creation [#Milestone 6](https://github.com/seanj06/P4-Sports-Expert/milestone/9)**

This Epic had 3 acceptance criterias

- Acceptance criteria 1: Users can access blog page via a button on home page

- Acceptance criteria 2: Users can view blogs by categories or by date

- Acceptance criteria 3: Users can access pages to edit or delete their posts if they are logged in

This milstone was centered around the creation of the blog home page. Note: The filter functionality of accpetance criteria 2 was not completed due to time constraints and the relevant user story was moved into the backlog.

#### **EPIC: U/X [#Milestone 7](https://github.com/seanj06/P4-Sports-Expert/milestone/4)**

This Epic had 7 acceptance criterias

- Acceptance criteria 1: Home page follows U/X design, has navigation links aswell as a small about section.

- Acceptance criteria 2: Blog page follows same design/colour pattern as home page. Blog posts are paginated by 6 posts.
Blog post cards show a title, category, date created, image and a description snippet.

- Acceptance criteria 3: Add a blog page and edit blog page have similar design to other pages. Success urls should take user back to blog detail page.

- Acceptance criteria 4: Sign up, Log in and Log out pages follow similar design to other pages, success messages do not push down page content.

- Acceptance criteria 5: Profile page follows similar design pattern to other pages. Profile page should show user information aswell as a button to user blogs, date profile created, a button to edit profile, info on when profile last edited.

- Acceptance criteria 6: Active page to be added to navbar.

- Acceptance criteria 7: Footer to be added to base.html with social link icons and name of author and year of creation

This milestone was centered around U/X design with acceptance criterias broken down by different site pages

#### **EPIC: User Functionality [#Milestone 8](https://github.com/seanj06/P4-Sports-Expert/milestone/3?closed=1)

This milestone included 3 user stories which centered around users being able to create an account and comment/ create blog posts.

### **Backlog [#Milestone 9](https://github.com/seanj06/P4-Sports-Expert/milestone/6)**

There are 4 user stories in the backlog milestone due to not being complete because of time constraints. They are:

- User being able to filter blog posts by category [USER STORY:Filter blog posts by category #18](https://github.com/seanj06/P4-Sports-Expert/issues/18)

- User being able to search for blog posts by author [USER STORY: Search for blog posts by user #20](https://github.com/seanj06/P4-Sports-Expert/issues/20)

- A search bar on the home page [USER STORY:Search bar #16](https://github.com/seanj06/P4-Sports-Expert/issues/16)

- User being able to reset password - [USER STORY:Reset Password #7](https://github.com/seanj06/P4-Sports-Expert/issues/7)

### **User Stories**

Below is a list of user stories completed In epic milestones.
Comments were left below user stories with commit numbers as per taksks completed.

#### **EPIC: Django Installation and app setup [#Milestone 1](https://github.com/seanj06/P4-Sports-Expert/milestone/1?closed=1)**

User Story 1
 - [USER STORY:Create new django project and app #2](https://github.com/seanj06/P4-Sports-Expert/issues/2)

 This user story had a Must Have label
   - Title:
       -  As a developer I can create a new Django project correctly so that my project can be built in the correct way

   - Tasks: 
       - Task 1 - Create new django project from command line
       - Task 2 - Create new app inside project andadd to installed apps on settings.py
       - Task 3 - Migrate all changes to database
       - Task 4 - Run app on server to make sure it was created successfully

   - Comments:
       - Project created and server run to make sure app was correctly installed - [b6338d3](https://github.com/seanj06/P4-Sports-Expert/commit/b6338d35869a468eff9b5bcf4f7d6ad2b46fb3e0) 

User story 2
  - [USER STORY:Django package installation #3](https://github.com/seanj06/P4-Sports-Expert/issues/3)  

  This user story had a Must Have label
   - Title:
       - As a developer I can install the needed librarys and packages so that my project is set up correctly

   - Tasks:
       -  Task 1 - Install Django + Heroku server from command line
       - Task 2 - Install PostgreSql database from command line
       - Task 3 - Install Cloudinary from command line
       -  Task 4 - Create requirements.txt file

   - Comments:
       - All packages installed - [64203e7](https://github.com/seanj06/P4-Sports-Expert/commit/b6338d35869a468eff9b5bcf4f7d6ad2b46fb3e0)  

#### **EPIC: First Heroku Deployment [#Milestone 2](https://github.com/seanj06/P4-Sports-Expert/milestone/2?closed=1)**

User Story 1
 - [USER STORY: First Heroku Deployment #1](https://github.com/seanj06/P4-Sports-Expert/issues/1)

  This user story had a Must Have label

   - Title:
       - As a developer I can deploy my project on Heroku so that it can be seen and used by other users

   - Tasks:
       - Task 1 - Create new app on Heroku
       - Task 2 - Create new instance on ElephantSql dashboard
       - Task 3 - Create env.py file and change settings.py as required
       - Task 4 - Migrate changes to database
       - Task 5 - Add config vars on Heroku
       - Task 6 - Create procfile
       - Task 7 - Deploy Branch in Heroku

   - Comments:
       - App successfully deployed to heroku - [4fc6f57](https://github.com/seanj06/P4-Sports-Expert/commit/4fc6f57ea26811b500bcba6f0907e25e41e3f7b7)

User Story 2
  - [USER STORY:Cloudinary #12](https://github.com/seanj06/P4-Sports-Expert/issues/12)

  This user story had a Should have label

   - Title:
       - As a developer I can install cloudinary so that all my images can still be displayed on my site after being deployed

   - Tasks:
       - Task 1 - Set up cloudinary account to get api var
       - Task 2 - Install cloudnary in workspace
       - Task 3 - add config var to env.py file and heroku
       - Task 4 - Add relevant variables to settings.py

   - Comments:
       - Cloudinary installed and all variables added in settings.py - [8fc3000](https://github.com/seanj06/P4-Sports-Expert/commit/8fc3000810860833ac97b7c881431df88f0a0d71)  

#### **EPIC: Home page creation [#Milestone 3](https://github.com/seanj06/P4-Sports-Expert/milestone/8)**

User Story 1
 - [USER STORY:Site Navigation #11](https://github.com/seanj06/P4-Sports-Expert/issues/11)

  This user story had A Should Have label

   - Title:
       - As a User I can navigate the site easily so that I can easily find what I am looking for

   - Tasks:
       - This user story had no tasks attached

   - Comments:
       - Carousel added to home page for user navigation - [07a7fa1](https://github.com/seanj06/P4-Sports-Expert/commit/07a7fa1f72f7e5391845a93d665873dffeae27a8)

User Story 2
  - [USER STORY:Create Templates #5](https://github.com/seanj06/P4-Sports-Expert/issues/5)    

   This user story had A Must Have label

   - Title:
       - As a developer I can create templates so that users can see the website online    

   - Tasks:
       - Task 1 - Create templates folder
       - Task 2 - Create base.html file to hold base template code
       - Task 3 - Create base html template code
       - Task 4 - Create news urls.py file and enter new path    

   - Comments:
       - Base.html file created and bootstrap content added - [3e84feb](https://github.com/seanj06/P4-Sports-Expert/commit/3e84febb7459482bfeb9db6df4641c0c9f7a82d1) 
       - Url app file created and path added to home page - [5a10cf9](https://github.com/seanj06/P4-Sports-Expert/commit/5a10cf93513f45568466afe5bf1f7f62fc8c1799)

User Story 3
  - [USER STORY:Home page #14](https://github.com/seanj06/P4-Sports-Expert/issues/14)

   This user story had a must have label

   - Title:
       - As a user I can visit the homepage so that I can log into my account and navigate to different parts of the site

   - Tasks:
       - Task 1 - Create view to homepage
       - Task 2 - Create navbar
       - Task 3 - Add sign in/sign up links to navbar  

   - Comments:
       - Homepage created with view - [5a10cf9](https://github.com/seanj06/P4-Sports-Expert/commit/5a10cf93513f45568466afe5bf1f7f62fc8c1799)
       - Bootstrap navbar added with links - [3e84feb](https://github.com/seanj06/P4-Sports-Expert/commit/3e84febb7459482bfeb9db6df4641c0c9f7a82d1)

                    











































