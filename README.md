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


#### **EPIC: User profile [#Milestone 4](https://github.com/seanj06/P4-Sports-Expert/milestone/10)**

User Story 1
 - [USER STORY:View blog posts #29](https://github.com/seanj06/P4-Sports-Expert/issues/29)

  This user story had a Should Have label

   - Title:
       - As a user I can view my blog posts from my profile so that I can keep track of all my blogs on one page

   - Tasks:
       - Task 1 - Link user profile to blog username
       - Task 2 - Create Listview for user created blogs

   - Comments:
       - Blog view created and code added so that user can only see their own blogs from profile - [98fb690](https://github.com/seanj06/P4-Sports-Expert/commit/98fb6902158d10b197cfba266edc7d8b97ad9921)  

User Story 2
 - [USER STORY:Profile Form #31](https://github.com/seanj06/P4-Sports-Expert/issues/31)

  This user story had Must Have label

   - Title:
       - As a user I can add my profile info by filling out a form so that I can save the info to my profile

   - Tasks:
       - Task 1 - Create forms.py file in profiles app
       - Task 2 - Create form that is linked to Profile model
       - Task 3 - Create view for form

   - Comments:
       - User profile automatically added with django signals
       - User able to edit profile with form - [6e704c2](https://github.com/seanj06/P4-Sports-Expert/commit/6e704c2a804bc3b246262e5e331fc1d2f4d789bd)

User Story 3
 - [USER STORY:Upload profile image #28](https://github.com/seanj06/P4-Sports-Expert/issues/28)

  This user story had a Should have label

   - Title:
       - As a user I can upload my own image to my profile so that I can customise my own profile

   - Tasks:
       - Task 1 - Add cloudinary field to user model
       - ask 2 - Add image view to frontend template

   - Comments:
       - Profile user model created with profile image - [e15436](https://github.com/seanj06/P4-Sports-Expert/commit/ee15436a35a218a4488819419efdee4e7a461230)            
              
User Story 4
 - [USER STORY:Delete/Edit blogs from profile page #30](https://github.com/seanj06/P4-Sports-Expert/issues/30)

 This user story had A Could have label

   - Title:
       - As a user I can Delete or Edit my blog posts from my profile page so that I can manage my blogs from one page

   - Tasks:
       - Task 1 - Add deleteview to profile page
       - Task 2 - Add editview to profile page

   - Comments:
       - View created from profile page for user to access own blogs, edit and delete - [98fb690](https://github.com/seanj06/P4-Sports-Expert/commit/98fb6902158d10b197cfba266edc7d8b97ad9921)

User Story 5
 - [USER STORY:Create a profile #27](https://github.com/seanj06/P4-Sports-Expert/issues/27) 

  This user story had a Must Have label

   - Title:
       - As a user I can create a profile so that I can keep track of my blogs

   - Tasks:
       - Task 1 - Create Profile app
       - Task 2 - Add user one to one model
       - Task 3 - Create profile page template
       - Task 4 - Create profile view

   - Comments:
       - Profile app created - [ff680fe](https://github.com/seanj06/P4-Sports-Expert/commit/ff680fedf12222a840dab7cec5859d84b550d024)
       - Django signals added to automatically create profile on account creation - [3abe18b](https://github.com/seanj06/P4-Sports-Expert/commit/3abe18be79adaa7e1948652a90b5ec4b4c7c723a)

#### **EPIC: Crud Functionality [#Milestone 5](https://github.com/seanj06/P4-Sports-Expert/milestone/5?closed=1)**     

User Story 1
 - [USER STORY:Read blog post #22](https://github.com/seanj06/P4-Sports-Expert/issues/22)

  This user story had a Must Have label

   - Title:
       - As a user I can view my blog post so that i can check i am happy with it

   - Tasks:
       - Task 1 - Create a detail view page for user to view blog post
       - Task 2 - Style detail view page

   - Comments:
       - Detail view page created - [c6c29b2](https://github.com/seanj06/P4-Sports-Expert/commit/c6c29b2335978cb67be0681a085291c5edd82b26)
       - Minimum style added to detail page. Will expand in U/X milestone - [df0e93e](https://github.com/seanj06/P4-Sports-Expert/commit/df0e93e6e287348f0bee9322f6623c5cedff8140)

User Story 2
 - [USER STORY:Delete Blog Post #24](https://github.com/seanj06/P4-Sports-Expert/issues/24)

  This user story had a Must Have label

   - Title:
       - As a user I can delete my blog post so that I can remove any posts i no longer want

   - Tasks:
       - Task 1 - Create delete button on detail view page
       - Task 2 - Ensure only logged in users can access delete button
       - Task 3 - Write code to ensure when delete button is pressed, data is removed from database

   - Comments:
       - Delete button created - [bbd7f84](https://github.com/seanj06/P4-Sports-Expert/commit/bbd7f8446630401079884be201e6f981b2eba69e)
       - Code written to ensure only logged users who own the post can delete - [00ff7de](https://github.com/seanj06/P4-Sports-Expert/commit/00ff7dec021e75e53f9eb5ec1033e6be3af40088)

User Story 3
 - [USER STORY:Update blog post #23](https://github.com/seanj06/P4-Sports-Expert/issues/23)

  This user story had a Must Have label

   - Title:
       - As a user I can update my blog post so that I can change anything i am not happy with

   - Tasks:
       - Task 1 - Create edit button on detail view page
       - Task 2 - Ensure only logged in users can access edit button
       - Task 3 - Create edit page

   - Comments:
       - Edit page created - [eac5000](https://github.com/seanj06/P4-Sports-Expert/commit/eac5000dffe191feb93aa60124712638eb9e7d0a)
       - Edit button created - [0c9b230](https://github.com/seanj06/P4-Sports-Expert/commit/0c9b2304da1d228b85d389027b3e63f248c91f4e)
       - Code added to make sure only logged in users can edit own posts - [b5bea5a](https://github.com/seanj06/P4-Sports-Expert/commit/b5bea5aa75074becedb4270a1db0bcb2841f1158)

User Story 4
 - [USER STORY:Create a blog post #21](https://github.com/seanj06/P4-Sports-Expert/issues/21) 

  This user story had a Must Have label

   - Title:
       - As a user I can create a blog post so that others can see my blog posts online

   - Tasks:
       - Task 1 - Create a django form for users to create a blog post

   - Comments:
       - Django form created and linked to model - [77f3686](https://github.com/seanj06/P4-Sports-Expert/commit/77f368639c4b1f4b79e9378bc8966a5f31f12b8b)

#### **EPIC: Blog view page creation [#Milestone 6](https://github.com/seanj06/P4-Sports-Expert/milestone/9)**

User Story 1
 - [USER STORY:Add image to blog post #19](https://github.com/seanj06/P4-Sports-Expert/issues/19)

  This user story had a Should Have label

   - Title:
       - As a user I can add an image to my blog post so that I can make my post stand out

   - Tasks:
       - This user story had no tasks attached to it

   - Comments:
       - Code added to let user add image to blog post - [c50ed39](https://github.com/seanj06/P4-Sports-Expert/commit/c50ed39cbd3c9b53fa6b06c332e59fe913daea80)    

User Story 2
 - [USER STORY: Django Forms #17](https://github.com/seanj06/P4-Sports-Expert/issues/17)

  This user story had a Must Have label

   - Title:
       - As a developer I can create django forms so that user database input can be validated and handled correctly

   - Tasks:
       - Task 1 - Create forms.py file
       - Task 2 - Create a form linking to database model
       - Task 3 - Define which fields are needed from model

   - Comments:
       - Django form created for BlogPost model - [d4f3d2d](https://github.com/seanj06/P4-Sports-Expert/commit/d4f3d2d430b247432f4452299f3fa187031e6bfb)

User Story 3
 - [USER STORY: Add Models #4](https://github.com/seanj06/P4-Sports-Expert/issues/4)

  This user story had a Must Have label

   - Title:
       - As a developer I can add database models so that the database knows how to handle user data

   - Tasks:
       - Task 1 - Import appropriate librarys at top of models.py file
       - Task 2 - Create a class based model
       - Task 3 - Add meta class to class based model
       - Task 4 - MIgrate changes to database

   - Comments:
       - BlogPost model created and changes migrated to database - [e815114](https://github.com/seanj06/P4-Sports-Expert/commit/e815114a3ccd09361eaacd54f98bd86a7327199b)

#### **EPIC: U/X [#Milestone 7](https://github.com/seanj06/P4-Sports-Expert/milestone/4)**

User Story 1
 - [USER STORY:Custom error pages #37](https://github.com/seanj06/P4-Sports-Expert/issues/37)

  This user story had a Must Have label

   - Title:
       - As a developer I can create custom error pages so that they match the theme of the site

   - Tasks:
       - Task 1 - Create custom 404, 403 and 500 page templates
       - Task 2 - Style templates

   - Comments:
       - Custom templates created - [539c8be](https://github.com/seanj06/P4-Sports-Expert/commit/539c8be88ecbab9b8a88e1792c9d67bd21ededde)
       - Custom styling added to templates - [540dd70](https://github.com/seanj06/P4-Sports-Expert/commit/540dd703d590f834c08e28f7dcb290f725080bdb)

User Story 2
 - [USER STORY:Forms #33](https://github.com/seanj06/P4-Sports-Expert/issues/33)

  This user story had a Must Have label

   - Title:
       - As a developer I can style the user forms so that they match the design of the rest of the site

   - Tasks:
       - Task 1 - Ensure sign up, log in ,log out edit blog and add blog pages design matches rest of site
       - Task 2 - Ensure success messages dont push down content
       - Task 3 - Ensure all success urls bring user to reverse page

   - Comments:
       - All forms styled to match site design - [2e6381f](https://github.com/seanj06/P4-Sports-Expert/commit/2e6381f1341bb9a685dbcdf6607186fe49201bde)
       - Absolute position given to success messages so messages dont push down content - [b08a1ca](https://github.com/seanj06/P4-Sports-Expert/commit/b08a1cafb441b857770ef0b828c78cece10b6405)
       - Code added in editprofile view to take user back to previous page - [9b52ed5](https://github.com/seanj06/P4-Sports-Expert/commit/9b52ed5d07222b266ac72c82100f8c6f7001788b)
       - Code added in deletecomment view to take user back to previous page - [41ca8fc](https://github.com/seanj06/P4-Sports-Expert/commit/41ca8fc661c4cff8cc4c0fbac9176c56b433a830)

User Story 3
 - [USER STORY:Profile page #34](https://github.com/seanj06/P4-Sports-Expert/issues/34)

  This user story had a Should Have label

   - Title:
       - As a developer I can style the user profile page so that all of the correct user information is displayed and the design matches the rest of the site

   - Tasks:
       - Task 1 - Ensure profile page design matches rest of website
       - Task 2 - All user information is displayed correctly

   - Comments:
       - Profile page re styled to match rest of site - [426ff3f](https://github.com/seanj06/P4-Sports-Expert/commit/426ff3f6dbacf072ec60e064669f984071a7c19f)
       - Code changed so user upload image displays instead of placeholder - [63008eb](https://github.com/seanj06/P4-Sports-Expert/commit/63008eb3e4ca4fca835cabe5f92d8c0fc7d28dfc)

User Story 4
 - [USER STORY:Blog Page #32](https://github.com/seanj06/P4-Sports-Expert/issues/32)

  This user story had a Should Have label

   -  Title:
       - As a developer I can style the blog page so that the user gets a good u/x experience

   - Tasks:
       - Task 1 - Add code so only 6 blogs are shown per page
       - Task 2 - Ensure blog cards have correct information shown
       - Task 3 - Change placeholder image depending on category

   - Comments:
       - Pagination added to blog page - [17009b5](https://github.com/seanj06/P4-Sports-Expert/commit/17009b58d23dc2ed6417f3b6de8ab4c66cd9bfdf)
       - Added Date created and category fields to blog card - [5532c09](https://github.com/seanj06/P4-Sports-Expert/commit/5532c09233cf2370e25d83ea820af3c95e89e7f3)
       - Placeholder image changes depending on user picked category - [f0e5caf](https://github.com/seanj06/P4-Sports-Expert/commit/f0e5caf54d707d3dfb40b9fc44197edbafc02e38)

User Story 5
 - [USER STORY: Home Page styling #15](https://github.com/seanj06/P4-Sports-Expert/issues/15)

  This user story had a Should Have label

   - Title:
       - As a developer I can style the home page so that it is visually appealing for new and frequent users

   - Tasks:
       - Task 1 -Style homepage using bootstrap
       - Task 2 - Add custom fonts using google fonts
       - Task 3 - Add introduction section
       - Task 4 - Add active class to navbar

   - Comments:
       - Introduction section added to home page - [da21efe](https://github.com/seanj06/P4-Sports-Expert/commit/da21efe386567615d9f1db82882058d69f08d2e4)
       - Active class added to navbar - [e6bd695](https://github.com/seanj06/P4-Sports-Expert/commit/e6bd69547f43dcd1c508931f99630f59b0dbba19)

User Story 6
 - [USER STORY:Footer #35](https://github.com/seanj06/P4-Sports-Expert/issues/35)

  This user story had a Must Have label

   - Title:
       - As a developer I can add a footer to my website so that I can display social media links and creation information

   - Tasks:
       - Task 1 - Add footer to base.html
       - Task 2 - Add font awesome social media icons
       - Task 3 - Add creation information

   - Comments:
       - Footer added with font awesome links and creation information - [eefb81b](https://github.com/seanj06/P4-Sports-Expert/commit/eefb81b48fb504884b8f9493e8634512ad5ac608)
       - Footer styled - [e8b77c7](https://github.com/seanj06/P4-Sports-Expert/commit/e8b77c7d1783d13ef19e7fcb74bff3ca7a1dd9f7)

User Story 7
 - [USER STORY:User Messages #26](https://github.com/seanj06/P4-Sports-Expert/issues/26)

  This user story had a Should Have label

   - Title:
       - As a developer I can add custom user messages so that the user knows the action they performed has been successfull or failed

   - Tasks:
       - Task 1 - Import messages in files where needed
       - Task 2 - Add message tags to settings.py
       - Task 3 - Add messages to html files where needed
       - Task 4 - Add. javascript timeout function

   - Messages imported and message tags added in settings.py - [7b40c7d](https://github.com/seanj06/P4-Sports-Expert/commit/7b40c7d42f6e4c6e430841c4a6f42336d5be682d)
   - Messages container added to base.html - [fcdd141](https://github.com/seanj06/P4-Sports-Expert/commit/fcdd14186a3d378be58bf943785ab9eb5a34cd3f)
   - Javascript timeout function added to bottom of base.html - [0725c89](https://github.com/seanj06/P4-Sports-Expert/commit/0725c8992c90d2f4d91f996e98addb074617485c)
   - Success messages added to All class based views - [09fa19b](https://github.com/seanj06/P4-Sports-Expert/commit/09fa19be637ac0f9f1aea8a2d9839eadc6296bdc)

User Story 8
 - [USER STORY:Style account creation pages #25](https://github.com/seanj06/P4-Sports-Expert/issues/25)

  This user story had a Must Have label  

   - Title:
       - As a developer I can style the log in, log out and sign up pages so that the UI matches the rest of the website pages

   - Tasks:
       - Task 1 - Import allauth pages from commnd line and add them to templates folder
       - Task 2 - Add custom styling to pages

   - Comments:
       - Sign up, Login and logout pages styled - [4b1c4f9](https://github.com/seanj06/P4-Sports-Expert/commit/4b1c4f9dd229d56c84ad95b8917b4564c8a878d1)  



                      


    


                                  











































