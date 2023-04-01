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

#### **EPIC: Blog view page creation [#Milestone 7](https://github.com/seanj06/P4-Sports-Expert/milestone/4)**

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




























