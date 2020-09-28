## My Cafe Memories

This is a social network site for users to share memories of their cafes.

<img src="https://res.cloudinary.com/machikolacey/image/upload/v1601223705/milestone3/MS3_emwjc6.png" style="width:100%;"/>

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
 
 If register:

<ol>
<li>The user can add username and password to register their account</li>
<li>It will navigate the user to "Edit your profile" page</li>
<li>If they want to add their image, they can click on "Edit" button to go to "Edit your profile" page</li>
<li>The user can add their image by adding link to their image</li>
<li>Click on "Save" to go to "Everyone's memories" page</li>
</ol>


 If login:

<ol>
<li>An user can fill in the form to go to "Your cafe memories" page</li>
<li>It will navigate the user to "Edit your profile" page</li>
<li>On the page, they can click on "Add your memory" button to fo to "Add your cafe memory" page</li>
<li>On the page, they can add the cafe name, description, photo link, ratings, and date. Also they can choose if this memory is private(display to the user only)</li>
<li>By clicking on "Save", go to "Your cafe memories" page</li>
<li>The user can see their memory is added on the page</li>
<li>The user can edit or delete the memory by clicking on the buttons</li>
<li>The user can add or edit cafe information</li>
</ol>



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

### PC
I have tested on these browsers:

<ol>
<li>Google Chrome</li>
<li>Firefox</li>
<li>Internet Explorer Edge</li>
</ol>

### Tablet
<ol>
<li>Kindle Fire 8 plus</li>
</ol>

### Mobile 
<ol>
<li>Samsung Galaxy A21s</li>
<li>iPhone 7</li>
<li>HUAWEI Mate 20 lite</li>
</ol>

I also used Google Chrome's device emulator to test on all types of devices.


I have asked on Code Institute's peer review community to test this website and received feedbacks:


Also, this was run through these validators.

<ul>
<li><a href="https://jigsaw.w3.org/css-validator/" target="_blank">CSS Validation Service</a></li>
<li><a href="https://validator.w3.org/" target="_blank">Markup Validation Service</a></li>
<li><a href="https://jshint.com/" target="_blank">JS Hint</a></li>
</ul>


### Test Results

<ol>
<li>Responsive menu was too tall and hiding the content on tablet size - fixed</li>
<li>The modal popup - the content was overflowing - fixed</li>
<li>The overlay was hiding the mobile nav - fixed</li>
<li>Auto Complete was not working on area search. Found the order of the javascript file was wrong - fixed</li>
<li>The content of the memory card was overflowing depends on the description - fixed</li>
<li>On the mobile phone menu there was no lines between links, and no effects on hover - fixed</li>
<li>On registration process it wasn't displaying requirement for the username - fixed</li>
<li>The 'Go back' button was on the front page - fixed</li>
<li>On tablet size, the memory image was not 100% width - fixed</li>
<li>On tablet size, the the header displayed 2 lines and took too much space - fixed</li>
<li>When user photo was not presented, it was causing an error on memory submittion - fixed</li>
<li>'background-color:none' was not validated - used 'background-color:transparent' instead</li>
<li>'border-color:none' was not validated - used border:none instead</li>
</ol>




<h3>How to test this project</h3>

<ol>
<li>On the front page, a welcomo popup will be shown with buttons - press 'Get Started!' button to go to register page</li>
<li>Fill in the form with a username and password, press 'Register' button</li>
<li>It will redirect to "Your Account Information" page</li>
<li>Click on 'Edit' button to display 'Edit your account information' page</li>
<li>Click on 'Save' to go to "Your memories" page</li>
<li>Click on 'Click here' to go to 'Add Your Cafe Memory' page </li>
<li>Fill in the form - add 2 or more characters on 'cafe' field to see auto-complete is working</li>
<li>Click on 'Date' field to see datepicker is working</li>
<li>Submit the form to go to 'Your cafe memories' page</li>
<li>On the top menu, click on 'Home' to go back to 'Everyone's memories' page</li>
<li>Check pagenation is working by clicking on the page numbers</li>
<li>Check 'Sort by' section to see sort is working</li>
<li>Click on 'Your memories' button to see if you can go back to 'Your memories' page</li>
<li>Click on 'Everyone's memories' button to see if you can go back to 'Everyone's memories' page</li>
<li>On the top menu, click on 'Add cafe' to go to 'Add Cafe' page</li>
<li>Fill in the form - test if area auto complete is working</li>
<li>Click on 'Submit' button to go to 'Manage Cafes' to see if the cafe is added on the page</li>
<li>Choose one of the cafes, click on 'Edit' button to edit cafe</li>
<li>Choose one of the cafes, click on 'Delete' button to delete cafe</li>
<li>Click on 'Logout' button to logout</li>
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
/li>

<li>- The videos used in this website are taken from:
https://www.youtube.com/</li>

</ul>


### Acknowledgements

- I received inspiration for this project from a resume project provided by Code Institute.

