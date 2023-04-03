# **Sports Expert**

## **Overview**

Sports expert is a sports blog website where users can make blog posts about a specific sport, view blog posts by other users and
comment on blog posts. They can also edit their profile and upload their own profile picture aswell as adding information about themselves.

Developed by Sean Johnston for code institute Project Portfolio project 4.

## **Project Goals**

As my fourth project for the [Code Institute](https://codeinstitute.net/) 5P course the goal of the project is to demostrate all of the skills I have learned in the course so far including languages such as HTML, CSS, Javascript and Python. Frameworks such as Django and Boostrap and version control technologies such as Git and Github.

## **UX**

### **The Strategy Plane**

Sports expert was designed to be a site for Sports lovers to share and read their own and other peoples opinions on multiple sports topics. The site was designed in a way that it is easy to navigate, and a homepage U.I that grabs new and returning users attention. Users can upload their own BlogPosts, comment on other users blogposts aswell as editing their own profile which is intended to create a proper website community.

#### **Target Users**

- A user that is a sports fan
- A user that likes to keep up to date with sports news
- A user that wants to create their own blogpost on a sport topic
- A user that wants to join in with the community and comment on other peoples blogposts or start a discussion.

#### **Site Goals**

- For users to be able to create an account, login and logout when they want.
- For users to be able to view blogposts regardless if they have made and account and are signed in or out
- For users to be able to create their own blogposts while logged in.
- For users to be able to comment on their own and other peoples blogposts while logged in
- For users to be able to edit their profile including adding thier own profile picture while logged in.

### **Agile Planning**

This project was built using the Agile method throughout by creating EPIC Miletones which were broken down into smaller user stories with labels "must-have", "should-have", "could-have", and wont have. 

Epics milestones were given Acceptance criterias and the must haves were completed first to complete the milestone. Any user stories that were not completed were moved back into the project backlog.

The Kanban board was created using Github projects and can be located [here](https://github.com/users/seanj06/projects/5/views/1)  and can be viewed to see the completed and backlogged user stories.

![Kanban Board](docs/readme-images/kanban-board.png)

#### **Epics**

Epics were broken down into 9 EPIC Milestones(including backlog)
which include 37 user stories in total. Each Milestone was given acceptance criteria and the milestone was closed when all the criteria had been met / all user stories were completed.
User stories were given tasks, and when each task and the given user stories were completed a comment was left with the commit number underneath the user story. When all tasks were complete the user story was closed.

##### **EPIC: Django Installation and app setup [#Milestone 1](https://github.com/seanj06/P4-Sports-Expert/milestone/1?closed=1)**

This Epic had 3 acceptance criterias

- Acceptance criteria 1: Django insalled to gitpod workspace and new project created

- Acceptance criteria 2: Install postresql database

- Acceptance criteria 3: Create new app inside project

This was the first milestone to be completed as it was needed to install django and the database.

##### **EPIC: First Heroku Deployment [#Milestone 2](https://github.com/seanj06/P4-Sports-Expert/milestone/2?closed=1)**

This Epic included 2 user stories which included installing cloudinary and the setting up the correct env.py variables to successfully deploy the prpject on heroku for the first time.

##### **EPIC: Home page creation [#Milestone 3](https://github.com/seanj06/P4-Sports-Expert/milestone/8)**

This Epic had 4 acceptance criterias

- Acceptance criteria 1: Users are brought to homepage when first entering the site

- Acceptance criteria 2:Users can log in and out from the navbar

- Acceptance criteria 3: What users see on the home page differs depending on if they are logged in or out

- Accpetance criteria 4: Users are shown a list of most recent blogs on page

This epic centred around the site home page and made sure user athentication was set up correctly

##### **EPIC: User profile [#Milestone 4](https://github.com/seanj06/P4-Sports-Expert/milestone/10)**

This Epic had 3 acceptance criterias

- Acceptance criteria 1: Users are able to go to profile section from home page

- Acceptance criteria 2: Users can upload own image for their profile aswell as add a quick bio

- Acceptance criteria 3: Users can see all of their blog posts from profile section

This epic centered around the users profile section including users being able to access profile page from the home page and edit and see their own blog posts from their profile page.

##### **EPIC: Crud Functionality [#Milestone 5](https://github.com/seanj06/P4-Sports-Expert/milestone/5?closed=1)**

This epic had 4 user stories all based around CRUD functionality

- User able to Read a blog post

- User able create a blog post

- User able to update a blog post

- User able to delete a blog post

##### **EPIC: Blog view page creation [#Milestone 6](https://github.com/seanj06/P4-Sports-Expert/milestone/9)**

This Epic had 3 acceptance criterias

- Acceptance criteria 1: Users can access blog page via a button on home page

- Acceptance criteria 2: Users can view blogs by categories or by date

- Acceptance criteria 3: Users can access pages to edit or delete their posts if they are logged in

This milstone was centered around the creation of the blog home page. Note: The filter functionality of accpetance criteria 2 was not completed due to time constraints and the relevant user story was moved into the backlog.

##### **EPIC: U/X [#Milestone 7](https://github.com/seanj06/P4-Sports-Expert/milestone/4)**

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

##### **EPIC: User Functionality [#Milestone 8](https://github.com/seanj06/P4-Sports-Expert/milestone/3?closed=1)

This milestone included 3 user stories which centered around users being able to create an account and comment/ create blog posts.

##### **Backlog [#Milestone 9](https://github.com/seanj06/P4-Sports-Expert/milestone/6)**

There are 4 user stories in the backlog milestone due to not being complete because of time constraints. They are:

- User being able to filter blog posts by category [USER STORY:Filter blog posts by category #18](https://github.com/seanj06/P4-Sports-Expert/issues/18)

- User being able to search for blog posts by author [USER STORY: Search for blog posts by user #20](https://github.com/seanj06/P4-Sports-Expert/issues/20)

- A search bar on the home page [USER STORY:Search bar #16](https://github.com/seanj06/P4-Sports-Expert/issues/16)

- User being able to reset password - [USER STORY:Reset Password #7](https://github.com/seanj06/P4-Sports-Expert/issues/7)

#### **User Stories**

Below is a list of user stories completed In epic milestones.
Comments were left below user stories with commit numbers as per taksks completed.

##### **EPIC: Django Installation and app setup [#Milestone 1](https://github.com/seanj06/P4-Sports-Expert/milestone/1?closed=1)**

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

##### **EPIC: First Heroku Deployment [#Milestone 2](https://github.com/seanj06/P4-Sports-Expert/milestone/2?closed=1)**

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

##### **EPIC: Home page creation [#Milestone 3](https://github.com/seanj06/P4-Sports-Expert/milestone/8)**

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


##### **EPIC: User profile [#Milestone 4](https://github.com/seanj06/P4-Sports-Expert/milestone/10)**

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

##### **EPIC: Crud Functionality [#Milestone 5](https://github.com/seanj06/P4-Sports-Expert/milestone/5?closed=1)**     

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

##### **EPIC: Blog view page creation [#Milestone 6](https://github.com/seanj06/P4-Sports-Expert/milestone/9)**

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

##### **EPIC: U/X [#Milestone 7](https://github.com/seanj06/P4-Sports-Expert/milestone/4)**

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

##### **EPIC: User Functionality [#Milestone 8](https://github.com/seanj06/P4-Sports-Expert/milestone/3?closed=1)**

User Story 1
 - [USER STORY: Add comments to blogs #36](https://github.com/seanj06/P4-Sports-Expert/issues/36)

  This user story had a Should Have label

   - Title:
      - As a user I can comment on blogs so that i can interact with the site community

   - Tasks:
       - Task 1 - Create comment model
       - Task 2 - Link comment model to user profile
       - Task 3 - Link model to blog posts
       - Task 4 - Render comments on template

   - Comments:
       - Comment model created - [7782aa7](https://github.com/seanj06/P4-Sports-Expert/commit/7782aa7a4186c366a56ed280ca8f94c3369a459a)
       - View code added for user to comment on blog post and rendered to template - [a0314ee](https://github.com/seanj06/P4-Sports-Expert/commit/a0314ee4a9396dd76e96165598d44f08c0131944)

User Story 2
 - [USER STORY:Create an account #6](https://github.com/seanj06/P4-Sports-Expert/issues/6)

  This user story had a Must Have label

   - Title:
      - As a User I can create an account so that I can create a blog post

   - Tasks:
       - Task 1 - Install allauth so user can create an account
       - Task 2 - Create Make a post page that user can only access while logged in
       - Task 3 - Set up code so users post is saved to database

   - Allauth installed - [3bd8927](https://github.com/seanj06/P4-Sports-Expert/commit/3bd89275ee6778dd47083f3990bd8ca99a097816)   
   - Add blog page created and code added to ensure only logged in users can access - [77f3686](https://github.com/seanj06/P4-Sports-Expert/commit/77f368639c4b1f4b79e9378bc8966a5f31f12b8b)

User Story 3
 - [USER STORY:Install allauth #13](https://github.com/seanj06/P4-Sports-Expert/issues/13)

  This user story had a Must Have label

   - Title:
       - As a developer I can install allauth so that site users can create an account to log in

   - Tasks:
       - Task 1 - Install allauth in command line
       - Task 2 - add allauth to installed apps

   - Comments:
       - Allauth installed, added to installed apps in settings.py and added login/logout redirect variables - [180640b](https://github.com/seanj06/P4-Sports-Expert/commit/180640b1c523c696066905ab82480eae11793885)    

##### User Stories Not Connected To A Epic Milestone

User Story 1
 - [USER STORY:Create Superuser #10](https://github.com/seanj06/P4-Sports-Expert/issues/10)

  This user story had a Must Have label

   - Title:
       - As a developer I can create a superuser so that i can manage my application from the admin panel

   - Tasks:
       - Task 1 - Create Superuser from command line
       - Task 2 - Install Summernote from command line
       - Task 3 - Run project with /admin added to url to make sure superuser can login

   - Comments:
       - Allauth installed and admin panel checked - [3bd8927](https://github.com/seanj06/P4-Sports-Expert/commit/3bd89275ee6778dd47083f3990bd8ca99a097816)
       - Summernote installed and added to installed apps in settings.py - [f5bb7cd](https://github.com/seanj06/P4-Sports-Expert/commit/f5bb7cd6519192ac6c23c3090fba48489b1eb1d9)

User Story 2
 - [USER STORY: Create Views #9](https://github.com/seanj06/P4-Sports-Expert/issues/9)

  This user story had a Must Have label

   - Title:
       - As a developer I can create views so that the function in the views can render and handle my templates appropriately for users to see
   
   - Tasks:
       - Task 1 - Import class based model from models.py
       - Task 2 - Create class based view

   - Comments:
       - View created for BlogPost model - [23e570f](https://github.com/seanj06/P4-Sports-Expert/commit/23e570f7d3f2b04dd9d2da570f5ce887bfd2e858)

User Story 3
 - [USER STORY: Create Multiple Apps #8](https://github.com/seanj06/P4-Sports-Expert/issues/8)

  This user story had a Should Have label

  - Title:
       - As a developer I can create multiple apps for my project so that my code is kept well organised

   - Tasks:
       - There are no tasks attached to this user story

   - Comments:
       - Multiple apps created to keep code organisation

##### Backlog Incompleted User Stories

User Story 1
 - [USER STORY:Filter blog posts by category #18](https://github.com/seanj06/P4-Sports-Expert/issues/18)

  This user story had a Wont Have label

   - Title:
       - As a user I can filter blog posts so that I can easily find the blogs i am looking for

   - This User story was part of the [Epic: Blog view Creation](https://github.com/seanj06/P4-Sports-Expert/milestone/9) milestone but was moved to the backlog because of time constraints.

User Story 2
 - [USER STORY: Search for blog posts by user #20](https://github.com/seanj06/P4-Sports-Expert/issues/20)

 This user story had a Wont Have label

   - Title:
       - As a user I can search for user specific blog posts so that I can follow my favourite bloggers

   - This User story was part of the [Epic: Blog view Creation](https://github.com/seanj06/P4-Sports-Expert/milestone/9) milestone but was moved to the backlog because of time constraints.      

User Story 3
 - [USER STORY:Search bar #16](https://github.com/seanj06/P4-Sports-Expert/issues/16)

   - Title:
       - As a developer I can implement a search bar into the home page so that users can search for posts by topic

   - This User story was part of the [Epic: Home Page Creation](https://github.com/seanj06/P4-Sports-Expert/milestone/8) milestone but was moved to the backlog because of time constraints. 

User Story 4
 - [USER STORY:Reset Password #7](https://github.com/seanj06/P4-Sports-Expert/issues/7)

   - Title:
       - As a user I can reset my password so that i can retrieve my account if i forget my password

   - This User story was part of the [Epic: CRUD Functionality](https://github.com/seanj06/P4-Sports-Expert/milestone/5) milestone but was moved to the backlog because of time constraints.  

### **Features**

#### **Home Page**

 - Navbar
   
   - The navbar is an element included in the base.html file so is shown to the user on every page of the site
   
   - Navbar desktop
      
      - The navbar Features a clickable site logo at the centre of the screen which directs users back to the home page from anywhere on the site. It also includes navigation links underneath with a blue underline showing users the active page.
      ![Navbar-desktop](docs/features/navbar-desktop.png)
      
      - The navigation links on the navbar change if the user is logged in, giving the user more navigation options such as adding a blog and profile pages. They are also shown a message telling them which account they are signed in as.
      ![Navbar-desktop-logged-in](docs/features/navbar-logged-in-desktop.png)
      

   - Navbar mobile
      
      - On mobile the navbar collapses down to a hamburger menu with the clickable logo moving to the left.
      ![Navbar-mobile](docs/features/navbar-mobile.png)
     
      - As with the desktop navbar the mobile navbar also gives users more options when signed in aswell as a message telling them which account they are signed in as.
      ![Navbar-mobile-logged-in](docs/features/navbar-mobile-logged-in.png)  

 - Bootstrap Carousel
   - This carousel section, built using bootstrap is directly below the navbar in the home page and is likely the first thing that will catch the users eye when they visit the site. 
   - Carousel signed out
      - When a user first visits the site and is logged out the auto sliding carousel will show the user 3 slides.
     
      - 1. Blog page slide 
      ![Carousel-blog](docs/features/carousel-blogs.png)
      
      - 2. Log in slide
      ![Carousel-login](docs/features/carousel-log-in.png)
      
      - 3. Sign up slide
      ![Carousel-signup](docs/features/carousel-sign-up.png)

   - Carousel logged in
      - Like the navbar, whether the user is logged in or not changes what slides are shown. The slides shown when a user is logged in are:
      
      - 1. Add a blog slide
      ![Carousel-addblog](docs/features/carousel-addblog.png)  
      
      - 2. Profile slide
      ![Carousel-profile](docs/features/carousel-profile.png) 
      
      - 3. Blog slide
      ![Logged-in-blog](docs/features/logged-in-blog-slide.png)

 - Site info section
   - This section gives the user a welcome message aswell as a brief overview of the sites purpose with the phrase "Where like minded sports fanatics can share, compare and discuss all things sports
   Whether its GAA, Football or Rugby you can find it all here."  
   ![Info-section-desktop](docs/features/info-section-desktop.png)  

   - The section is placed on the home page just under the navbar to give users info on the purpose of the site as soon as they enter.

 - Footer  
    
   - Like the navbar the footer is also a part of the base.html file so is shown to the user on every page of the site.

   - The footer includes a social media links section with 4 fontawesome clickable icons. Facebook, Twitter, Instagram and Github. All links Open on a new page.

   - The footer also contains a Copyright message at the bottom of the page with the site author name and year of development.

   ![Footer](docs/features/footer-desktop.png) 

#### **Blog Home Page**

 - **Bootstrap cards**

   - The blog home page features bootstrap cards with information on blog posts including an image, the blogpost author, the blogpost title, the blogpost description the date the blogpost was posted and the category.

      - The image on the card changes depending on circumstance.
      
      - If the user uploads no image and chooses "Football" as category:
        ![Blog-Home-football](docs/features/blog-home-football.png)
      
      - If the user uploads no image and chooses "Rugby" as category:
      ![Blog-home-rugby](docs/features/blog-home-rugby.png)

      - If the user uploads no image and chooses "GAA" as category:
      ![Blog-home-gaa](docs/features/blog-home-gaa.png)

      - If the user uploads no image and chooses "Other" as category:
      ![Blog-home-other](docs/features/blog-home-other.png)

      - If the user chooses to upload their own image it is displayed as normal on the card:
      ![Blog-home-user-upload](docs/features/blog-home-user-upload.png)

 - **User Authentication**
     
     - Users are able to access the blog home page regardless of whether they are signed in or not.

      - The buttons on the cards will change depending on if the user is the author or not. If the user is the author they will be shown 3 options To either navigate to the blog, delete the blog or edit the blog
      ![Blog-home-author](docs/features/blog-home-gaa.png) 

      - If the user is not the author they will only be shown 1 button, to navigate onto the blog detail page
      ![Blog-home-not-author](docs/features/blog-home-not-author.png)

 - **Responsiveness**

      - The blog home page is fully responsive to all screen sizes and will change how many cards are shown in a row depending on screen width.

         - For large screen sizes cards are shown in rows of 3 wide.
         ![Blog-home-large-screen](docs/features/blog-home-large-screen.png) 

         - For medium screen sizes cards are shown in rows of 2 wide
         ![Blog-home-medium-screen](docs/features/blog-home-medium-screen.png) 

         - For small screen sizes cards are shown in rows of 1 wide
         ![Blog-home-small-screen](docs/features/blog-home-small-screen.png)

 - **Pagination**

      - The blog cards are paginated by 6 cards per page.

      - The bottom of the home page shows the user 4 buttons, one to navigate to the first page, one for the previous page, one for the next page and one for the last page.

      - There is also. page counter which shows the user which page they are currenty on aswell as the total number of pages

      ![Blog-home-pagination](docs/features/blog-home-pagination.png)            


#### **Blog Detail Page**

 - The blog detail page is navigated to by the user clicking the "Blog" button on the blog home page.

 - The blog detail page includes 3 sections. The "Header" section the blog body section and the comment section with a home button on the bottom of the page to navigate users back to the home page.


 - **Header section**

    - The header section shows the Blogpost details such as the Author, The date posted, the title and either the user uploaded image or the placeholder image. Like the blog home page if the user has not uploaded an image the placeholder image will change depending on category chosen.
    ![Blog-detail-header](docs/features/blog-detail-header.png)

 - **Body section**

    - The body section includes the body text of the blogpost. The body text includes paragraph linebreaks for easy user readability.
    ![Blog-detail-body](docs/features/blog-detail-body.png)

 - **Comment Section**

    - The comment section is placed directly below the body section and allows users to make comments on the blog post if they are logged in. The content of the comment section changes depending on circumstance  

       - If user is logged in and there are no comments
       ![Comments-no-comments-logged-in](docs/features/comments-no-comments-logged-in.png) 

       - If user is not logged in and there are no comments
       ![Comments-no-comments-logged-out](docs/features/comments-no-comments-not-logged.png)

       - If user is logged in and there are comments
       ![Comments-comment-logged-in](docs/features/comment-comment-logged-in.png)

       - If user is not logged in and there are comments
       ![Comments-comment-logged-out](docs/features/comment-comment-logged-in-comments.png) 

#### **Profile Page**

 - The profile page is only accessible by users that have made an account and logged in.

 - Django signals was used so a profile is automatically made for a user as soon as they sign up for an account.

  - **Profile image**

     - Users are able to upload their own profile image to their profile.
     ![Profile-uploaded-image](docs/features/profile-uploaded-image.png)

     - If no profile image is uploaded a placeholder image is displayed
     ![Profile-placeholder](docs/features/profile-placeholder-image.png)

 - **Profile About**

     - The about section shows the users profile information such as their username, full name, about, the date their profile was created and the date it was last edited
     ![Profile-about](docs/features/profile-about.png)

 - The bottom of the profile page has 3 buttons for the user to choose from.
      ![profile-buttons](docs/features/profile-buttons.png)

      - The home button will direct users back to the home page.

      - The Myblogs button will bring users to a page, similiar to the blog home page that shows them all of their created blog posts where they can view, edit and delete them. Or if the user has no created blogs, a message that tells them they dont have any blogs and a button that directs them to the addblog page.

         - User has blogposts
         ![myblogs](docs/features/my-blogs.png)

         - User has no blogposts
         ![myblogs-noblogs](docs/features/myblogs-noblog.png)

      - The edit profile button will bring users to a form page where they can edit and delete their profile.

      - The form was built using django-crispy-forms
      ![Edit-profile](docs/features/edit-profile.png)   

        - From this page the user can edit their name, about section and profile image. **Note**: There is a bug on the image section of the form where it doesnt show the user their current uploaded image. I will address this further in the bugs section of the readme. 

        - If the user presses the confirm edit button and the form is valid they are shown a success message stating "Profile edited successfully" and redirected back to their profile page.
        ![profile-edit-message](docs/features/profile-edit-message.png) 

        - If the user presses the delete profile button they are brought to a page which shows them a message asking if they are sure they would like to delete the profile.
        ![Delete-profile](docs/features/delete-profile.png)
        
          - If they press delete they are logged out and redirected to the home page with a success message stating "Profile deleted successfully"
          ![delete-profile-message](docs/features/profile-delete-message.png)
        

#### **Add A Blog Page**

 - The Add A blog page is accessible from either the navbar or the carousel if the user is logged in.

  - Users are able to Add a blog post by adding a description, a title, their own upload image, the blogpost text body and selecting the category. **Note**: There is a bug on the image section of the form where it doesnt show the user their current uploaded image. I will address this further in the bugs section of the readme.  
  ![add-blog](docs/features/add-blog.png)

  - The form was built using django-crispy-forms

  - When the user presses the submit button if the form is valid they are shown a message stating "Blog post created" and are redirected to the blog home page.
  ![blog-post-message](docs/features/blog-post-message.png)

  - If the form is invalid the user is shown a message telling them which field is invalid or required.
  ![invalid-form](docs/features/invalid-form.png)

      

  
   









     









                      


    


                                  











































