# Ticker

![alt text](https://github.com/yipmunallen/Third-Milestone-Project/blob/master/assets/images/readme/websitemockup.png "Ticker Screenshot")

This is a full-stack site, built using HTML, CSS, JavaScript, Python, Flask framework and MongoDB. It allows users to browse and comment on stocks, as well as build their own watchlists.

Disclaimer: This website is for educational purposes only. Only a selection of stocks have been added in order to demonstrate functionality. Stocks comments are not financial advise.

The live project can be viewed [here](https://third-milestone-project-ticker.herokuapp.com).

## Table of Contents
1. [Ux](#ux)
   1. [Users stories](#users-stories)
   1. [Design](#design)
      1. [Wireframes](#design)
      1. [Final Pages](#final-pages)
      1. [Data Structure](#data-structure)
      1. [Colour Scheme](#colour-scheme)
      1. [Typography](#typography)
1. [Technologies](#technologies-used)
   1. [Languages](#languages)
   1. [Frameworks, Libraries & Programs](#frameworks-libraries-programs)
1. [Testing](#testing)
    1. [Site Goals](#site-goals)
   1. [User stories](#user-stories)
   1. [Additional Functionality](#Additional-Functionality)
   1. [Compatibility](#compatibility)
   1. [Bugs](#bugs)
   1. [Validation](#validation)
1. [Deployment](#deployment)
1. [Credits](#credits)

## UX

### Site Goals

1. Create a visually appealing site with intuitive navigation.
1. Encourage users to sign up by providing additional functionality those logged in
1. Give the logged in users the ability to customise their profiles through watchlists and engage with other users in the comments sections

### Users Stories
As a user I want to:

1. Browse available stocks
1. Easily search for stocks that I am interested in
1. Be able to comment on stocks
1. Be able to edit comments I have submitted
1. Be able to delete comments I have submitted
1. Build my own watchlist so that I can have easy access to my favourite stocks
1. Be able to remove stocks from my watchlist
1. Be able to see comments across all stocks


### Design

- #### Wireframes

  - [Home](https://github.com/yipmunallen/Third-Milestone-Project/blob/master/assets/images/homewireframe.png)
  - [Browse](https://github.com/yipmunallen/Third-Milestone-Project/blob/master/assets/images/ruleswireframe.png)
  - [Stock](https://github.com/yipmunallen/Third-Milestone-Project/blob/master/assets/images/ruleswireframe.png)
  - [Log In / Sign Up](https://github.com/yipmunallen/Third-Milestone-Project/blob/master/assets/images/settingswireframe.png)
  - [Feed](https://github.com/yipmunallen/Second-Milestone-Project/blob/master/assets/images/quizwireframe.png)
  - [Watchlist](https://github.com/yipmunallen/Second-Milestone-Project/blob/master/assets/images/scorewireframe.png)

- #### Final Pages 

  -  [Home](https://github.com/yipmunallen/Third-Milestone-Project/blob/master/assets/images/homepage.png)

  - [Browse](https://github.com/yipmunallen/Third-Milestone-Project/blob/master/assets/images/rulespage.png) -
Shows list of stocks and includes basic information on each stock. Logged in users can see whether the stock is in their watchlist or not. There is a searchbar at the top as well as a filter that users can use to refine their view.

  - [Results](https://github.com/yipmunallen/Third-Milestone-Project/blob/master/assets/images/rulespage.png) -
Shows results of user's stock search 

  - [Stock](https://github.com/yipmunallen/Third-Milestone-Project/blob/master/assets/images/settingspage.png) -
This is an individual stock page. It shows in depth stock information including current price, and price change / percentage change from previous day close. There is a comments section at the bottom of the page.

  - [Log In](https://github.com/yipmunallen/Third-Milestone-Project/blob/master/assets/images/quizpage.png) -
Users can log in on this page

  - [Log In](https://github.com/yipmunallen/Third-Milestone-Project/blob/master/assets/images/quizpage.png) -
Users can sign up on this page

  - [Feed](https://github.com/yipmunallen/Third-Milestone-Project/blob/master/assets/images/scorepage.png) -
This shows the most recent 50 comments either across all stocks, or just on the user's watchlist depending on which filter they choose

  - [Watchlist](https://github.com/yipmunallen/Third-Milestone-Project/blob/master/assets/images/feedbackpage.png) -
Contains all the user's watched stocks

- #### Data Structure

This site uses [__MongoDB__](https://www.mongodb.com//). It's database contains 3 collections: users, stocks and comments. Their structures are as follows:

[alt text](https://github.com/yipmunallen/Third-Milestone-Project/blob/master/assets/images/readme/datastructure.png "Ticker Data Structure")

Registered users are added to the users collection. When they create a new comment, a new document is added to the comments collection, with that comment id added to the comments array of the corresponding stock.

-   #### Colour Scheme
    -   The main colours used for the site are centered around blue and white:
        1. #1A8A94 for heading text
        2. #324B4E for body text
        3. #fff for buttons text

 -   #### Typography
      -   The font used for headings throughout the site is "Rubik". "Roboto" is used for the remainder of text. Sans-serif has been used as the fallback font throughout. These fonts are chosen as they are easy to read.

## Technologies Used

### Languages

- [__HTML5__](https://en.wikipedia.org/wiki/HTML5) - Used to structure and present the website.
- [__CSS__](https://en.wikipedia.org/wiki/CSS) - Used to style the website.
- [__JavaScript__](https://en.wikipedia.org/wiki/JavaScript) - Used to collapse navbars and dynamically show the edit comment forms.
- [__Python__](https://en.wikipedia.org/wiki/Python_(programming_language)) - Used for the backend development.

### Frameworks, Libraries & Programs

- [__Jinja__](https://en.wikipedia.org/wiki/Jinja_(template_engine)) - Templating engine used.

- [__MongoDB__](https://www.mongodb.com/) - Database used for storing and retrieving information.

- [__Cloudinary__](https://cloudinary.com/) - Used to store all stock icons.

- [__Heroku__](https://heroku.com/) - Used to deploy the site.

- [__Flask__](https://en.wikipedia.org/wiki/Flask_(web_framework)) - Used to provide libraries and tools for the site such as Werkzeug.

- [__Yfinance__](https://pypi.org/project/yfinance/) - API used for stock price information.

- [__Mockflow__](https://www.mockflow.com/) - Used to create the wireframes during the planning stage of the project.

- [__Bootstrap Framework__](https://getbootstrap.com/docs/4.5/getting-started/introduction/) - Used for the site design, forms, modals and dropdowns.

- [__JQuery__](https://jquery.com/) - Used to manipulate HTML and CSS properties.

- [__Google Fonts__](https://fonts.google.com/) - Used to import the "Rubik" and "Roboto" fonts used throughout the site.

- [__Font Awesome__](https://fontawesome.com/) - Used to import the icons used for the watchlists.

- [__Favicon__](https://favicon.io/) - Used to created the favicon used on the site. 

- [__Git__](https://git-scm.com/) - Used for version control.

- [__Github__](https://github.com/) - Used to store all website code once pushed from Git.

- [__Google Chrome Developer Tools__](https://developers.google.com/web/tools/chrome-devtools) - Used to inspect page elements, test different CSS styles and debug site issues using the console.

## Testing

In order for the website to pass testing, the following have been tested both whilst in development and on the live website:

1. Functionality in line with user stories
1. Additional functionality required for website building
1. Compatibility with multiple devices and browsers

In addition: 

1. The HTML, CSS, Javascript and Python files have been validated using respective online validators.
1. Bugs have been listed

### User Stories

1. Browse available stocks
    1. 
    2.
1. Easily search for stocks that I am interested in
1. Be able to comment on stocks
1. Be able to edit comments I have submitted
1. Be able to delete comments I have submitted
1. Build my own watchlist so that I can have easy access to my favourite stocks
1. Be able to remove stocks from my watchlist
1. Be able to see comments across all stocks

### Additional Functionality

  - __Allowing single answer__-  This has been tested to ensure that once an answer is clicked, all other answer buttons are disabled other than the Next Question Button

  - __Next Question Button__- This has been tested to ensure that it will appear whenever a selection is made, or when the timer runs out

  - __404 Error__- This has been tested to ensure that the 404 error page will show if the error occurs, with a link that redirects to the home page.

### Compatibility

  - __Devices__ - The website has been viewed and tested on a range of devices including Desktop, Laptop, Iphone 6/7/8/X, Ipad and Samsung Galaxy Tab, retaining structure and functionality.

  - __Browsers__ - The website has been viewed and tested on a range of browsers including Google Chrome, Internet Explorer and Firefox, retaining structure and functionality.

### Validation

  - __CSS__ - Validated using [Jigsaw](https://jigsaw.w3.org/css-validator/#validate_by_input) with no errors found.

  - __HTML__ - Validated using [W3C](https://validator.w3.org/#validate_by_input). Disregarding errors relating to the use to Jinja, there are no errors found.

  - __Javascript__ - Validated using [JSHint Validator](https://jshint.com/) with no errors found.

  - __Python__ - Validated using [PEP 8](https://jshint.com/) with no errors found.
  
### Bugs

  - __Unable To Get Category From API__ - There was a "Musicals and Theatres" category, but the category value was returning an error from the API so it has been removed.


## Deployment

This project is hosted by Github and deployed using heroku.

### Clone this project

In order to clone this project:

1. Log in to Github and find the Github Repository.
1. Click the "code" button and copy the HTTPS link
1. Open Git terminal and type ```git clone``` followed by the link
1. Access the folder in your terminal window and install the application's required modules using the following command: ```pip3 install -r requirements.txt```
1. Create your database in MongoDB.
    1. Signup or login to MongoDB
    2. Create a cluster as well as a database.
    3. Create three collections within your database following this [data structure](#data-structure)
1. Add an env.py file to your workspace to include your environment variables. It will need to contain the following varibles:
    ``` os.environ["PORT"] = "5000" ```
    ``` os.environ["SECRET_KEY"] = "YOUR_SECRET_KEY" ```
    ``` os.environ["DEBUG"] = "True" ```
    ``` os.environ["MONGO_URI"] = "YOUR_MONGODB_URI" ```
    ``` os.environ["MONGO_DBNAME"]= "DATABASE_NAME" ```
1. The Project can be run from the local using the following command in the gitpod CLI ```python3 app.py```

## Credits

### Code

- [Code Institute](https://www.codeinstitute.net/) - Code learnt during the Full Stack Web Developer course has been implemented in this project.

- [MarkHeath](https://markheath.net/post/customize-radio-button-css) - Used post to customise radio button appearance in settings page (referenced in style.css).

### Acknowledgements
- Spencer Barriball - Mentor at Code Institute

