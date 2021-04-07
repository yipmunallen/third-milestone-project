# Quiz Website

<!-- ![alt text](https://github.com/yipmunallen/Second-Milestone-Project/blob/master/assets/images/quizscreenshot.png "Ticker Screenshot") -->

This is a full-stack site, built using HTML, CSS, JavaScript, Python, Flask framework and MongoDB. It allows users to browse and comment on stocks, as well as build their own watchlists.

<!-- The live project can be viewed [here](https://yipmunallen.github.io/third-milestone-project/). -->

## Table of Contents
1. [Ux](#ux)
   1. [Users stories](#users-stories)
   1. [Design](#design)
      1. [Wireframes](#design)
      1. [Final Pages](#final-pages)
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
1. Give the user the ability to customise their profile through watchlists and engage with other users in the comments section
1. Provide a means of user feedback to enable user-driven development

### Users Stories
As a user I want to:

1. Be able to comment on stocks
1. Be able to edit comments I have submitted
1. Be able to delete comments I have submitted
1. Build my own watchlist so that I can have easy access to my favourite stocks
1. Be able to remove stocks from my watchlist
1. Easily search for stocks that I am interested it

<!-- ### Design

- #### Wireframes

  - [Home](https://github.com/yipmunallen/Second-Milestone-Project/blob/master/assets/images/homewireframe.png)
  - [Rules](https://github.com/yipmunallen/Second-Milestone-Project/blob/master/assets/images/ruleswireframe.png)
  - [Settings](https://github.com/yipmunallen/Second-Milestone-Project/blob/master/assets/images/settingswireframe.png)
  - [Quiz](https://github.com/yipmunallen/Second-Milestone-Project/blob/master/assets/images/quizwireframe.png)
  - [Score](https://github.com/yipmunallen/Second-Milestone-Project/blob/master/assets/images/scorewireframe.png)

- #### Final Pages 

  -  [Home](https://github.com/yipmunallen/Second-Milestone-Project/blob/master/assets/images/homepage.png)

  - [Log In](https://github.com/yipmunallen/Second-Milestone-Project/blob/master/assets/images/rulespage.png) -
Outlines the quiz rules

  - [Sign Up](https://github.com/yipmunallen/Second-Milestone-Project/blob/master/assets/images/settingspage.png) -
Allows user to apply settings to quiz

  - [Browse](https://github.com/yipmunallen/Second-Milestone-Project/blob/master/assets/images/quizpage.png) -
Main quiz page, where users can select answers and get visual feedback on their choices

  - [Watchlist](https://github.com/yipmunallen/Second-Milestone-Project/blob/master/assets/images/scorepage.png) -
Displays user's score at the end of each game

  - [Stocks](https://github.com/yipmunallen/Second-Milestone-Project/blob/master/assets/images/feedbackpage.png) -
Contains a form that allows users to quickly and easily contact the site owner without having to navigate away from the page

-   #### Colour Scheme
    -   A dark grey background is contrasted with a range of brightly coloured buttons across the site. The same colours are used for buttons that perform similar actions (i.e "Start" , "Quiz Me" , "Play Again") in order to guide the user. The text is white is order to make it easy to read against the background.

 -   #### Typography
      -   The font used for headings throughout the site is "Staatliches". "Fredoka One" is used for the questions and buttons in order to make them stand out. The remainder of the text uses "Open Sans". Sans-serif has been used as the fallback font throughout. These fonts are chosen as they are easy to read but also provide a fun look for the quiz.

## Technologies Used

### Languages

- [__HTML5__](https://en.wikipedia.org/wiki/HTML5) - Used to structure and present the website.
- [__CSS__](https://en.wikipedia.org/wiki/CSS) - Used to style the website.
- [__JavaScript__](https://en.wikipedia.org/wiki/JavaScript) - Used to provide functionality across the site, including on click button fuctions, applying settings, populating the quiz data using the [__Trivia DB__](https://opentdb.com/) API and enabling feedback via the [__EmailJS__](https://www.emailjs.com//) API.

### Frameworks, Libraries & Programs

- [__Mockflow__](https://www.mockflow.com/) - Used to create the wireframes during the planning stage of the project.

- [__Bootstrap Framework__](https://getbootstrap.com/docs/4.5/getting-started/introduction/) - Used for the form on the feedback page.

- [__JQuery__](https://jquery.com/) - Used to manipulate HTML and CSS properties.

- [__Google Fonts__](https://fonts.google.com/) - Used to import the "Staatliches","Fredoka One" and "Open Sans" fonts used throughout the site.

- [__Font Awesome__](https://fontawesome.com/) - Used to import the icons used on the buttons throughout.

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

1. The HTML, CSS and Javascript files have been validated using respective online validators.
1. Bugs have been listed

### User Stories

1. Easily understand the rules of the quiz
    1. A rules page containing a list of rules for the quiz has been added to the site
    2. This page is easily accesible from the homepage using a button
2. Be able to customise my experience, by choosing the category and difficulty of each round
   1. The "Settings" page gives the user the option to choose from a range of categories, or to select "No Category" whereby they will be given a random selection
   2. The "Settings" page allows the user to choose from three difficulties: Easy, Medium and Hard.
   3. This has been tested to ensure that if a difficulty is not selected, an error will appear asking the user to select one
1. Know whether I got the question correct or incorrect
   1. Once an answer is selected, testing confirms the answer will turn green if correct.
   1. Once an answer is selected, testing confirms the answer will turn red if incorrect
1. Learn the correct answer if I got a question wrong so that I can learn
   1. If the user selects the incorrect answer, their chosen answer will turn red, but the correct answer will turn green
1. See my score at the end of each game
   1. The score is tallied up during the quiz and shown to the user at the end of each game on the "Score" page
   1. Testing confirms that if the correct answer is selected, the score will increase by one.
   1. If the incorrect answer is selected, the score will not increase.
1. Be able to give feedback on my experience
   1. The user can click on the "Submit Feedback" button at the end of each game to redirect to the "Feedback" page
   1. From the "Feedback" page, the user can input their Name, Email and Message to be submitted using the EmailJS API
   1. If the "submit" button is selected with some fields left unfilled, an error will appear asking the user to complete the unfilled fields. Similarly, if an email address is inputted without an "@" sign, an error will also appear, stating that this is not a valid email
    1. Once the user clicks the "Submit" button, an alert appears, thanking the user for their feedback. The form also clears allowing for further feedback.

### Additional Functionality

  - __Allowing single answer__-  This has been tested to ensure that once an answer is clicked, all other answer buttons are disabled other than the Next Question Button

  - __Next Question Button__- This has been tested to ensure that it will appear whenever a selection is made, or when the timer runs out

  - __404 Error__- This has been tested to ensure that the 404 error page will show if the error occurs, with a link that redirects to the home page.

### Compatibility

  - __Devices__ - The website has been viewed and tested on a range of devices including Desktop, Laptop, Iphone 6/7/8/X, Ipad and Samsung Galaxy Tab, retaining structure and functionality.

  - __Browsers__ - The website has been viewed and tested on a range of browsers including Google Chrome, Internet Explorer and Firefox, retaining structure and functionality.


### Validation

  - __CSS__ - Validated using [Jigsaw](https://jigsaw.w3.org/css-validator/#validate_by_input) with no errors found.

  - __HTML__ - Validated using [W3C](https://validator.w3.org/#validate_by_input) with no errors found.

  - __Javascript__ - Validated using [JSHint Validator](https://jshint.com/) with no major issues.
  
  1. Moved goToNextQuestion function outside if statement to fix errors.
  1. Remaining warnings regarding the use of cont as available in ES6

### Bugs

  - __Unable To Get Category From API__ - There was a "Musicals and Theatres" category, but the category value was returning an error from the API so it has been removed.


## Deployment

### Github Pages

This project has been deployed to Github Pages using the following steps:

1. Log in to Github and find the Github Repository.
1. Locate the repository settings.
1. Locate the GitHub Pages Section.
1. Below "Source", click the dropdown headed "None" and select the "Master Branch" and then "Save".
1. Once the page refreshes, scroll back down to the same section, and the site link is now available.

## Credits

### Code

- [Code Institute](https://www.codeinstitute.net/) - Code learnt during the Full Stack Web Developer course has been implemented in this project.

- [MarkHeath](https://markheath.net/post/customize-radio-button-css) - Used post to customise radio button appearance in settings page (referenced in style.css).

### Acknowledgements
- Spencer Barriball - Mentor at Code Institute
 -->
