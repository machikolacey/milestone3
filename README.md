## My Cafe Memories

This is a social network site for users to share memories of their cafes.

<img src="https://res.cloudinary.com/machikolacey/image/upload/v1607468359/milestone3/my-cafe-memories-frontend_h1j2ou.png" style="width:100%;"/>

The goal for the user is to share their cafe memories with other like-minded people, who would like to explore and find an ideal cafe for themselves.
Also, they can look at their cafe memories, go back to their memories, and share memories of their cafes.
They can choose either private or public for each memory, so they don't have to be worried about showing all the images they want to store for themselves.

In the future, this will give me an opportunity to ask cafe owners to provide their information by themselves, and also coupon code available for their customers. And also the cafe owner will be able to give them a 'Thank you' coupon code for positive reviewers.


<ul>
<li>An unregistered user can browse this website to see everyone's cafe memories.</li>
<li>If they become an user, they will be able to add their cafe memories.</li>
<li>They can add their memories from "Add memory" page. </li>
<li>They can search the cafe names by auto complete. </li>
<li>They can add cafe name(auto-complete), description, photo link, rating(1 to 5), Date(datepicker).</li>
<li>If they are unable to find the cafe, they can add a cafe from "Add cafe" page.</li>
<li>On "Add cafe" page, they can add area name(auto-complete), cafe name, website, postal address, postcode, photo link, and youtube link(optional).
</li>
<li>They can also browse and edit/ delete cafes from "Manage cafes" page.</li>
</ul>


## Deployed page is available here
http://milestone3-data-centric-mlk.herokuapp.com/


## Wireframe

https://github.com/machikolacey/milestone3/blob/master/pdf/wireframe-ny-cafe-memories.pdf


## UX

If they haven't visited the website (detected by cookie), the homepage displays a modal popup to describe what this website for.
This navigates an user to either registration page or login page, or if they decide not to register, just closes the popup.

The steps:
 
| User Story    | Expected Outcome  |
| ------------- |:---------------:|
| As a first tune user, I want to quickly understand the purpose of the website, and easily navigate to either 'Register' page or go back to the home page.  | I expect the popup explains well and buttons to be prominent.   | 
| As a first tune user, I want to easily create an account.                                                                                                  | I expect I can create my account easily, and quickly navigated to 'profile' page  |
| As a first tune user, After creating my account, I want a user to add my profile image.                                                                    | I expect I can see the profile page straight after creating account, and find 'edit' button for image upload.         | 
| As a first tune user, After adding my profile image, I would like to add a cafe memory at ease.  | I expect to see an intuitive button to 'Add your first cafe memory' button       |   
| As a returning user, I want to browse everyone's memories at ease.  | I expect 'Sorting' section and 'Paging' section works well   | Both sections are working well. |
| As a returning user, I want to login.    | I expect the page direct to 'Your memories' page, and intuitively can choose 'Add your first memory' button.     I expect 'Login' button to be easily found, redirect to 'Your cafe memories' page straight after logging in.        |    
| As a returning user, I want to add a memory with ease.                                                                                             | I expect 'add memory' form is easy to follow. On 'Cafe name', by entering  1 or more letters, it suggests cafes to choose from. The 'photo' section should explain how to add an image. The 'date' section it should open a date picker by clickin on the input field.    |
| As a returning user,  I want to add a cafe with ease.                                                                                               | I  expect 'add cafe' form is easy to follow.  Auto-suggest on 'Area name',  the photo section has a link to Cloudinary.   | 
| As a returning user, I want to edit a memory with ease.                                                                                          | I  expect 'Your memories' page has 'Edit' button, on 'Edit cafe memory' page, I can edit text or the image easily.   | 
| As a returning user, I want to delete a memory with ease.                                                                                          | I  expect 'Your memories' page has 'Delete' button, on 'Edit cafe memory' page, I can delete the memory easily.   | 
| As a returning user, I want to edit a cafe with ease.                                                                                          | I  expect 'Manage cafes' page has 'Edit' button, on 'Edit cafe memory' page, I can edit text or the image easily.   | 
| As a returning user, I want to delete a cafe with ease.     | I  expect 'Edit cafe memory' page has 'Delete' button, on 'Edit cafe memory' page, I can delete the memory easily.   | 




## Features


### Existing Features

<ul>
<li><b>Feature 1 : Browsing all memories</b> - allows users browsing all the posted memories, by visiting home "Everyone's memories" page</li>
<li><b>Feature 2 : Cafe information</b> - allows users reading cafe information by clicking the image and name of the cafe </li>
<li><b>Feature 3 : Add and edit cafes</b> - allows users adding & editing cafe information, cafe memory by filling in the forms</li>
<li><b>Feature 4 : Add and edit memories</b> - allows users adding & editing their cafe memory by filling 'Add memory' form</li>
<li><b>Feature 5 : Auto-complete</b> - Auto complete - allows users to search for the area & cafe name by inserting text in the input</li>
<li><b>Feature 6 : Add photos using Cloudinary </b> - Photos - they can add their photos by adding a link from a photo cloud (such as https://cloudinary.com/)</li>
<li><b>Feature 7 : Sorting</b> - Sort - users can sort by date, cafe name, and rating</li>
<li><b>Feature 8 : Pagination</b> - Pagination - users can browse cafe memories and cafe informations using pagination, so they can easily navigate through the list</li>
</ul>


### Features Left to Implement
- I would like to categorise cafes
- I would like to add more user information and user role - so cafe owner has more privilage to add their cafe information and also coupon code
- I would like to add coupon provided by cafe owners. This will potentially we can provide a package for cafe owners to have their subscriptions, give them ability to add campaigns targeting cafe freaks. 
- I would like to add a facility to give users more coupon code, when they contribute to this website by adding more memories. Hopefully we can provide subscriptions packages for them so they can benefit from sharing their memories.




## Technologies Used


###  Back-end 
<ul>
<li><a href="https://www.python.org/" rel="nofollow">Python</a></li>
<li><a href="https://flask.palletsprojects.com/en/1.1.x/" rel="nofollow">Flask</a> - Python framework For pagination, etc</li>
<li><a href="https://www.dnspython.org/" rel="nofollow">Dnspython</a>-  DNS toolkit for Python</li>
<li><a href="https://www.heroku.com" rel="nofollow">Heroku</a> - Cloud application platform </li>
<li><a href="https://www.mongodb.com/cloud/atlas" rel="nofollow">Mongo DB Atlas</a> - non relational, NO-SQL Database - Cloud based MongoDB server</li>
</ul>


###  Front-end 
<ul>
<li><a href="https://www.javascript.com/" rel="nofollow">Javascript</a> - For auto-complete, navbar, etc</li>
<li><a href="https://jquery.com/" rel="nofollow">Jquery</a> - For auto-complete, navbar, etc</li>
<li><a href="https://materializecss.com/" rel="nofollow">Materialize</a> - for clean front-end design, and also icons</li>
<li><a href="https://www.w3schools.com/howto/howto_css_modals.asp" rel="nofollow">W3C Modal Box</a> - The project uses W3c's Modal Box to display welcome text.</li>
</ul>

### Image Library

This project is using images from <a href="https://cloudinary.com/" rel="nofollow">cloudinary.com</a>, which is used as alternative to image upload facility.

       
## Testing

# User stories
 
# First time user
| User Story    | Expected Outcome  | Outcome | 
| ------------- |:---------------:|:--------------------:|
| I want to quickly understand the purpose of the website, and easily navigate to either 'Register' page or go back to the home page.  | I expect the popup explains well and buttons to be prominent.    | I could understand the information, and quickly navigate to register page, or choose to go back to the front page. |
| I want to easily create an account.                                                                                                  | I expect I can create my account easily, and quickly navigated to 'profile' page  | I could easily add an account, and it promptly redirected to 'Profile' page.                 |
| After creating my account, I want a user to add my profile image.                                                                    | I expect I can see the profile page straight after creating account, and find 'edit' button for image upload.         | Straight after account creation, I was navigated to the profile page, and found 'edit' button.|
| After adding my profile image, I would like to add a cafe memory at ease.  | I expect to see an intuitive button to 'Add your first cafe memory' button       |   After adding an image, it redirected to 'Your cafe memories' page, and I could find 'Add your first memory' button easily.              |


# Returning user
| User Story    | Expected Outcome  | Outcome | 
| ------------- |:---------------:|:--------------------:|
| I want to browse everyone's memories at ease, find my favourite cafe, and enjoy looking at images.  | I expect 'Sorting' section and 'Paging' section works well   | Both sections are working well. |


I have asked on Code Institute's peer review community to test this website and received feedbacks:


Also, this was run through these validators.

<ul>
<li><a href="https://jigsaw.w3.org/css-validator/" target="_blank">CSS Validation Service</a></li>
<li><a href="https://validator.w3.org/" target="_blank">Markup Validation Service</a></li>
<li><a href="https://jshint.com/" target="_blank">JS Hint</a></li>
</ul>


### Test Results

<ol>
<li>Responsive menu was too tall and hiding the content on tablet size 
<p>I reduced the height of the menu by adding media query on CSS.</p>
</li>
<li>The modal popup - the content was overflowing
<p>I added a CSS code to fix the issue.</p>
</li>
<li>On small devices, the overlay was hiding the mobile nav
<p>This was Materialize's overlay. I corrected z-index and it's fixed.</p>
</li>
<li>Auto Complete was not working on area search.
<p>Fixed the order of the javascript file.</p></li>
<li>The content of the memory card was overflowing depends on the description
<p>I have added media query to reduce the size on mobile phones, also reduced the size of the description.</p></li>
<li>On the mobile phone menu there was no lines between links, and no effects on hover
<p>I have added hover effect on CSS.</p></li>
<li>On registration process it wasn't displaying requirement for the username.
<p>Added the requirement on the 'Registration' page.</p></li>
<li>The 'Go back' button was on the front page.
<p>I have added CSS code to remove it on the front page.</p></li>
<li>On tablet size, the memory image was not 100% width.
<p>I have added minimum width for these images to make sure it always covers the area.</p></li>
<li>On tablet size, the the header displayed 2 lines and took too much space.
<p>I have added a CSS code to add martgin top.</p></li>
<li>When user photo was not presented, it was causing an error on memory submittion.
<p>I have dded default photo when an user registers, so there will be an photo displayed by default.</p></li>
<li>'background-color:none' was not validated.
<p>used 'background-color:transparent' instead</p></li>
<li>'border-color:none' was not validated<p>used border:none instead</p></li>
</ol>





## Deployment

This project was developed on Github, using Gitpod as IDE. It has only master branch.
This is pushed and deployed on to heroku.

Deployed project is found here:

https://milestone3-data-centric-mlk.herokuapp.com/

This project utilises Mongo DB to use NO-SQL (non-relational) database.
Before cloning the project:

<ol>
<li>Add a database collection 'brightonCafes' on <a href="https://www.mongodb.com/cloud/atlas" target="_blank">MongoDB Atlas</a></li>
<li>Create a database and these tables: 
   <ul>
   <li>cafes</li>
   <li>areas</li>
   <li>users</li>
   <li>memories</li>
   </ul>
</li>
</ol>

## To run this project on your local repository
This project will be deployed following these steps:
<ol>
<li>Add your own repository on your Github account</li>
<li>Click the green 'Gitpod' button on top-right corner of this repo(If you can't find the button, install 'Gitpod' extension on your Chrome browser</li>
<li>Gitpod launches</li>
<li>Run the following command (Replace the 'USERNAME' and 'REPO' to your username and repo name):</li>
 
```

git remote set-url origin https://github.com/USERNAME/REPO.git

```


<li>Add env.py file on your root folder, add these lines:
 
```
import os

os.environ['SECRET_KEY'] = '- YOUR SECRET KEY - '
os.environ['MONGO_URI'] = '- YOUR MONGO URI -' 

```
</li>
<li>Run this command below to install all the modules on requirements.txt file:

```

pip3 install -r requirements.txt

```
</li>
<li>Run the code by running this code below:
 
```

python3 app.py

```

</li>
</ol>


## Remote Deployment (Run the project on Heroku.com)
If you want to add it to your Heroku account, follow the instructions below:

<ol>
<li>Add an app for this project</li>
<li>Add environment variables 'SECRET_KEY' and 'MONGO_URI' on your app</li> 
<li>Add PORT on your app</li> 
<li>On your Gitpod workspace, login to heroku by running this code below:
 
 
```

heroku login -i

```

</li> 
<li>Select your app by running this code below (Replace '- YOUR APP NAME -' with your own app name):
 
```

git init

heroku git:remote -a  - YOUR APP NAME -

```

</li>
<li>Run this code below to push the code to your Heroku app:

```

git push heroku master

```

</li>
<li>When the app is deployed, click on 'Open App' button to run your app </li>
</ol>


## Data Integration
I used MongoDB for this project as this is requirement for this project. This is a non-relational, documentation database.
It gives me more flexibility and ability to manipulate or change structure of the data when I update this website in the future.
Only user_id, cafe_id, and memory_id need to be related, and it doesn't require complicated relations. 

In my database, I made 4 collections, which are areas, cafes, memories and users.

# users

| Title         | Key in MongoDB  | Form Validation Type | Data Type |
| ------------- |:---------------:|:--------------------:| ---------:|
| Id            | _id             | -                    | ObjectId  |
| User Name     | username        | text                 | String    |
| Password      | password        | text                 | String    |
| Photo         | photo           | text                 | String    |


# areas
This collection is for storing area data related to cafes.

| Title         | Key in MongoDB  | Form Validation Type | Data Type |
| ------------- |:---------------:|:--------------------:| ---------:|
| Id            | _id             | -                    | ObjectId  |
| Name          | name            | text                 | String    |


#cafes

| Title         | Key in MongoDB  | Form Validation Type | Data Type |
| ------------- |:---------------:|:--------------------:| ---------:|
| Id            | _id             | -                    | ObjectId  |
| Cafe Name     | cafe_name       | text                 | String    |
| Website       | website         | text                 | String    |
| Address       | address         | text                 | String    |
| Postcode      | postcode        | text                 | String    |
| Area Name     | area_name       | text                 | String    |
| Photo         | photo           | text                 | String    |
| Youtube Link  | youtube         | text                 | String    |



#memories

| Title         | Key in MongoDB  | Form Validation Type | Data Type |
| ------------- |:---------------:|:--------------------:| ---------:|
| Id            | _id             | -                    | ObjectId  |
| Cafe Name     | cafe_name       | text                 | String    |
| Description   | description     | text                 | String    |
| Photo         | photo           | text                 | String    |
| Date          | date            | text                 | Date      |
| User          | user            | text                 | String    |
| User id       | user_id         | text                 | ObjectId  |
| Ratings       | ratings         | text                 | String    |
| Action        | action          | text                 | String    |
| Cafe id       | cafe_id         | text                 | ObjectId  |




## Defensive Features
<ol>
<li>A new user can not register with a username already taken by existing user. So it checks existing usernames, if there is, it displays a flash message to suggest a different username.</li>
<li>We want a new user to understand that this is a social network service specialising in cafes. I added a popup to explain it and added buttons to choose wheather they register, or not to register.</li>
<li>We didn't want duplicate entries for a single cafe with multiple names, so I added a javascript code to auto-suggest cafe names.</li>
<li>We didn't want duplicate entries for an area, so I added a javascript code to auto-suggest area names.</li>
<li>We display a photo of the user on "Everyone's cafe memories" page. If a user choose not to upload their photo, it will display a default photo to avoid empty <img /> tag to be displayed.</li>
</ol>


## Credits

### Content

<ul>
<li>Memory photos are taken by Machiko Lacey-Kimura, and uploaded to <a href="https://cloudinary.com/" rel="nofollow">https://cloudinary.com/</a></li>
<li>This project is using icons from Materialize.</li>
</ul>

### Media

<ul>
<li>- The photos and texts used in this website are taken from:
<ul>
<li>https://www.google.co.uk/maps</li>
<li>https://www.facebook.com</li>
</ul>


<li>- The videos used in this website are taken from:
https://www.youtube.com/</li>

</ul>


### Acknowledgements

- I received inspiration for this project from several peer student's projects.

