## My Cafe Memories

This is a social network site for users to share memories of their cafes.


The goal for the user is to share their cafe memories with other like-minded people, who would like to explore and find an ideal cafe for themselves.
Also, they can look at their cafe memories, go back to their memories, and it's good to see good memories of their cafes.
They can choose either private or public for each memory, so they don't have to be worried about showing all the images they want to store for themselves.

In the future, this will give me an opportunity to ask cafe owners to provide their information by themselves, and also coupon code for their customers.


<ul>
<li>A non-user can browse this website to see everyone's cafe memories.</li>
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
<li>Feature 1 - allows users browsing all the posted memories, by visiting home "Everyone's memories" page</li>
<li>Feature 2 - allows users reading cafe information by clicking the image and name of the cafe </li>
<li>Feature 3 - allows users adding & editing cafe information, cafe memory by filling in the forms</li>
<li>Feature 3 - allows users adding & editing their cafe memory by filling 'Add memory' form</li>
<li>Feature 4 - Auto complete - allows users to search for the area & cafe name by inserting text in the input</li>
<li>Feature 5 - Photos - they can add their photos by adding a link from a photo cloud (such as https://cloudinary.com/)</li>
<li>Feature 6 - Sort - users can sort by date, cafe name, and rating</li>
<li>Feature 7 - Pagination - users can browse cafe memories and cafe informations using pagination, so they can easily navigate through the list</li>
<li></li>
</ul>


For some/all of your features, you may choose to reference the specific project files that implement them, although this is entirely optional.

In addition, you may also use this section to discuss plans for additional features to be implemented in the future:

### Features Left to Implement
- I would like to add more categories
- I would like to add more destinations, and pages for different towns
- I wouuld like to make icon ticked, and display the order on the marker when added to the tour

## Technologies Used

 <ul>
         <li>Javascript</li>
         <li><a href="https://developers.google.com/maps/documentation/javascript/tutorial" rel="nofollow">Google Maps Platform - Maps Javascript API</a> - To display markers, informations
        </li>
        <li><a href="https://developers.google.com/maps/documentation/directions/start" rel="nofollow">Google Maps Platform - Directions API</a> - To display directions on the map, calculate total distance and time by walking
        </li>
        <li>
           <a href="https://getbootstrap.com/" rel="nofollow">Bootstrap</a> - to display a clean responsive layout.
        </li>
        <li><a href="https://fontawesome.com/" rel="nofollow">FontAwesome</a> - The project uses <strong>FontAwesome</strong> to display effective buttons.
        </li>
         <li><a href="https://www.w3schools.com/howto/howto_css_modals.asp" rel="nofollow">W3C Modal Box</a> - The project uses W3c's Modal Box to display destination details.  
        </li> 
       </ul>
       
       
## Testing
This code was tested by using PC, tablet, and android phone, also using Google Chrome's Responsive Tester. This repository was tested by peer code review channel on Code Institute's community on Slack.

Also, this was run through these validators.

<ul>
<li><a href="https://jigsaw.w3.org/css-validator/" target="_blank">CSS Validation Service</a></li>
<li><a href="https://validator.w3.org/" target="_blank">Markup Validation Service</a></li>
<li><a href="https://jshint.com/" target="_blank">JS Hint</a></li>
</ul>

<h3>User Stories</h3>

<ol>
<li>A Google Map with markers on destinations are shown.</li>
<li>Click on a category button to filter markers</li>
<li>Click on a marker to see the popup modal to come up to display the details of the destination</li>
<li>On the dialog, click on  "Add to your tour" button, to see if the destination title is added to the tour, and displayed under "Your Tour" heading.</li>
<li>On the dialog, click on  "Add to your tour" button, to see if the dialog closes.</li>

<li>When an user clicks on "Close" button, it closes the dialog</li>
<li>In "Your Tour", click on the "delete" button to delete the destination from the tour</li>
<li>In "Your Tour", click on the "Move up" button to replace the order of the place with the one before.</li>
<li>In "Your Tour", click on  the "Move up" button to replace the order of the place with the one next.</li>
<li>click on  the "Check Distance" button, it will display the tour map on the map, also calculates total KM, total duration, and calories consumed.</li>
<li>Click on "Remove" button on all destinations to see if it removes all the destinations in the tour, and displays all the markers on the map without issues.</li>
<li>Test 1 to 10 on tablet and mobile phone sizes.</li>
</ol>


## Deployment

My repository can be found on Github. I used HTML, CSS and javascript and no database.

The page is deployed by Github pages. There is only master branch. 

There is no past versions to look at so far. Deployed page is found here:
http://milestone3-data-centric-mlk.herokuapp.com/memories/date/asc?page=2

To run this reponsitory locally, you could
<ul>
<li>Follow the respository link above to the GitHub Dashboard, and click on "Clone" or "Download".</li>
<li>If you "Clone", initialize git on your local environment's folder and clone the file by pasting the copied command on your command line.</li>
<li>If you "Downlowd" expand and copy all the files downloaded into the folder in your chosen development environment.</li>
</ul>


## Credits

### Content
- All the marker icons are made by Machiko Lacey-Kimura.

- Descriptions, address, details are taken from:
https://www.atlasobscura.com/
https://restaurantsbrighton.co.uk
https://www.getawriggleon.com
https://www.brighton-hove.gov.uk/
https://www.atlasobscura.com/places/the-goldstone-hove-england
https://www.google.co.uk/maps
https://www.facebook.com


### Media
- The photos and texts used in this website are taken from:
https://restaurantsbrighton.co.uk
https://www.getawriggleon.com
https://www.brighton-hove.gov.uk/
https://www.atlasobscura.com/places/the-goldstone-hove-england
https://www.facebook.com

- The videos used in this website are taken from:
https://www.youtube.com/


### Acknowledgements

- I received inspiration for this project from a resume project provided by Code Institute.

