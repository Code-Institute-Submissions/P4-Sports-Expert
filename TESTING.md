# **Sports Expert Testing**

## **Overview**
A wide range of testing was carried out during development including, Automated testing, manual testong, user story testing, code validation and bug testing.

## **Automated testing**

100% Of the code was covered throughout the automated testing process.
![coverage-report](docs/unit%20testing/coverage%20report.png)

### **Home App**

The home app only had 1 unit test overall, for the Homeview view function.

![Homeview](docs/unit%20testing/test-home-app.png)

### **Blog App**
The blog app was the first app I tested through unit testing so has by far the most tests out of all the apps as a lot of the same logic in this app is covered in tests here that are also in other app files.

![Test-blog-app](docs/unit%20testing/test-blog-app.png)

#### **Blog Forms**

 - The blog forms file had 6 tests.
   ![Test-blog-forms](docs/unit%20testing/test-blog-forms.png)

#### **Blog Models**

 - The blog models file had 7 tests.
   ![Test-blog-models](docs/unit%20testing/test-blog-models.png)

#### **Blog Views**

 - The blog views file was by far the hardest portion of testing to cover and overall had 16 tests.
   ![Test-blog-views](docs/unit%20testing/test-blog-views.png)

### **Profiles App**

![Test-profile-app](docs/unit%20testing/test-profiles-app.png)

#### **Profiles Models**

 - The profiles model file had 1 test.
   ![Test-profile-models](docs/unit%20testing/test-profiles-models.png)

 - The profile views file had 5 tests
   ![Test-profile-views](docs/unit%20testing/test-profiles-views.png) 

## **Manual Testing**

### **Epic Milestone  Acceptance Criteria Testing**

There were 3 milestones that did no have acceptance criteria. The user stories in these milestones will be tested in the user story section.

#### **EPIC: Django Installation and app setup [#Milestone 1](https://github.com/seanj06/P4-Sports-Expert/milestone/1?closed=1)**

**Acceptance criteria 1** : Django insalled to gitpod workspace and new project created

  - Django was installed at the beginning of the project development

**Acceptance criteria 2** : Install postresql database

  - Postgres sql database was also installed at the start of the project development from the terminal.

**Acceptance criteria 3**: Create new app inside project

 - The "home" app was the first app created at start of development as the base app for the homepage view

#### **EPIC: Home page creation [#Milestone 3](https://github.com/seanj06/P4-Sports-Expert/milestone/8)**

**Acceptance criteria 1**: Users are brought to homepage when first entering the site

 - The blank url for the site leaves users at the index.html page(i.e the home page)

**Acceptance criteria 2** :Users can log in and out from the navbar

 - User are able to log in and out from the navbar at the top of the page. The navbar options will change depending on if the user is logged in or out.

**Acceptance criteria 3**: What users see on the home page differs depending on if they are logged in or out 

 - The navbar and carousel options will change depending on if the user is logged in or out. If the user is logged out they will have access to the log in, sign up, and blog page. If they are logged in they will have access to the log out, blog page, add a blog page and profile page.

#### **EPIC: User profile [#Milestone 4](https://github.com/seanj06/P4-Sports-Expert/milestone/10)**

**Acceptance criteria 1**: Users are able to go to profile section from home page

 - Provided the user is logged in, they are able to navigate to their profile page from both the navbar and carousel on the home page.

**Acceptance criteria 2**: Users can upload own image for their profile aswell as add a quick bio 

 - Users are able to add their own profile picture aswell as enter their full name and add some info about themselves from the edit profile page.

**Acceptance criteria 3**: Users can see all of their blog posts from profile section 

 - Users are able to see all of their blogposts from the myblogs page in the profile section. If the user has no blogs they will be shown a button that will direct them to the add a blog page.

#### **EPIC: Blog view page creation [#Milestone 6](https://github.com/seanj06/P4-Sports-Expert/milestone/9)**

**Acceptance criteria 1** : Users can access blog page via a button on home page

 - Regardless of whether users are signed in or not, they are able to access the blog home page via both the navbar and carousel on the home page.

**Acceptance criteria 2**: Users can view blogs by categories or by date

 - This criteria was not met due to time constraints and will be talked about further in user stories testing.

**Acceptance criteria 3**: Users can access pages to edit or delete their posts if they are logged in 

 - Providing a user is logged in, they will be shown buttons on the bottom of their blogpost card to either edit or delete the post.

#### **EPIC: U/X [#Milestone 7](https://github.com/seanj06/P4-Sports-Expert/milestone/4)**

**Acceptance criteria 1**: Home page follows U/X design, has navigation links aswell as a small about section.

 - The home page follows the same design to match the rest of the site, like the rest of the site includes a navbar at the top of the page and has an about section below the carousel.

**Acceptance criteria 2**: Blog page follows same design/colour pattern as home page. Blog posts are paginated by 6 posts.
Blog post cards show a title, category, date created, image and a description snippet. 

 - The blog page has the same design as the rest of the site. Blog posts are paginated by 6 posts and features 4 buttons for users to navigate to the next page, previous page, first page and last page.
 The blogpost cards include either a placeholder image depending on category if the user has not uploaded an image, or the user uploaded image, the title, description, date posted and category.

**Acceptance criteria 3**: Add a blog page and edit blog page have similar design to other pages. Success urls should take user back to blog detail page. 

 - The add a blog page and edit blog page follow similar form design to the rest of the forms on the site. After valid form submission the add a blog page will take the user to the blog home page and the edit blog will take the user back to the blog detail page they have just edited.

**Acceptance criteria 4**: Sign up, Log in and Log out pages follow similar design to other pages, success messages do not push down page content. 

 - The sign up and log in pages follow the same crispy-form design as other forms on the site. The log out page has the same design as other single button pages on the site. The success messages has a z-index of 1 so it is placed on top of the other content rather than push it down.

**Acceptance criteria 5**: Profile page follows similar design pattern to other pages. Profile page should show user information aswell as a button to user blogs, date profile created, a button to edit profile, info on when profile last edited. 

 - The profile page has a similar colour scheme and design pattern to the rest of the site. The profile page shows the username, full name is user has entered one, user profile picture if they have uploaded one, date the user joined, date the profile was last edited, a button to edit profile and a button to navigate to myblogs page.

**Acceptance criteria 6**: Active page to be added to navbar.

 - The navbar has an active page feature by a blue underline underneath the active page.

**Acceptance criteria 7**: Footer to be added to base.html with social link icons and name of author and year of creation

 - The footer features 4 social media link icons for Facebook, Twitter, Instagram and Github. It also features a message about site author and year of development.

### **User Story Testing**

Overall there were 33 completed user stories and 4 uncompleted user stories throughout the projects development they will all be tested below to ensure criteria has been met for each story.

#### 1.[USER STORY: First Heroku Deployment #1](https://github.com/seanj06/P4-Sports-Expert/issues/1)

 - As a developer I can deploy my project on Heroku so that it can be seen and used by other users

   - The project was successfully deployed on Heroku and is currently able to be seen and used by all users.

#### 2.[USER STORY:Create new django project and app #2](https://github.com/seanj06/P4-Sports-Expert/issues/2)

 - As a developer I can create a new Django project correctly so that my project can be built in the correct way

   - A new django project was created at the beginning of development.

#### 3.[USER STORY:Django package installation #3](https://github.com/seanj06/P4-Sports-Expert/issues/3)

 - As a developer I can install the needed librarys and packages so that my project is set up correctly

   - All relevant django packages including the postgres database and cloudinary storage were installed at the beginning of development.

#### 4.[USER STORY: Add Models #4](https://github.com/seanj06/P4-Sports-Expert/issues/4)

 - As a developer I can add database models so that the database knows how to handle user data

   - Multiple database models were added throughout development including BlogPost model, Comments Model and Profile Model.

#### 5.[USER STORY:Create Templates #5](https://github.com/seanj06/P4-Sports-Expert/issues/5)

 - As a developer I can create templates so that users can see the website online

   - Multiple templates werw added throughout the development of the project to render all pages of the site.


















