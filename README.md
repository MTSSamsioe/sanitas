# Sanitas Gym
---
Welcome to Sanitas Gym's site, Sanitas is the latin word for health which is our main focus. We are a gym situated in the heart of one of stockholms islands Södermalm. On our site the you can choose a gym subscription of your choice with recurring payments. And even purchase and schedule personal trainer sessions of one hour each. Our subscriptions include all our facilities and classes. The purpose of this site is to bring dynamic e-commerce functionality to an otherwise static business location. To be abel to reach our customers and future customers with services and offers where evere they are is vital for a business today.
We have made efforts in marketing such as paid ads and optimized our site for search engines to make it easy or new customers to find us. 

---
# Features
--- 
## Exisiting Features
---

### Base template
---

 - Logo
    - Here you can see our Gym name and if you click it you will get back to our index page.

 - Shopping bag
    - Here you can see a shopping bag symbol. If you press it you will be taken to our shoppingbag page (only if authenticated). Next to the bag icon you will see the total amount in the cart at the moment. This is makes it possible for you to see your total amount o all pages of the site and open it

 - Members page
    - Here you can see your current delivery information if you have done a previous purchase. Otherwise you can fill in your information and press update. You can also see your previous orders here

 - Navigation 
    All active links in the navbar is underlined so you know which page you are currently on. The colors have been tested for visability with contrast and size

    - Our navigation consist of three main nav-links plus additional options for login and registration.

        - "Home" takes you back to our home page
        - "Gym Subscriptions" takes you to our subscriptions page where you can choose a subscription of your choice.
        - "Personal trainer" takes you to our personal trainer session page. Here you can purchase and schedule sessions with one of our trainers.
    - Login logout and registration
        - If you are logged in you will see a link "Logout" otherwise you will see two links "Register and "Login" This will clearly show you if you are logged in or not. Otherwise the different site pages are going to tell you when you need to be logged in
    - If you click a link where you need to be logged in you will get redirected to the log in page or shown a link that will take you to the login page. This is to promote a good user flow

![picture of navbar](media/nav_sanitas_gym.png)

- Messages
    - Messages are shown when you do certain tasks across the site. So you will receive confirmation that tasks are done Successfully or if an error has occurred. Tasks are shown in green and errors are shown in red. examples of such actions are:
        - Login / Logout 
        - Register an account
        - Add products to shoppingbag
        - Update shoppingbag
        - Delete item from shopping bag
        - Checkout complete
        - Activate subscription
        - Schedule training sessions
        - Update user profile
        - Different types of errors that can occur during these actions
    - Messages are shown under the navbar on all sites

![picture of messages](media/success_message.png)

- Main content
    - Here is the content from our different pages loaded. The navbar and footer are shown on all pages

- Footer
    - Here you ca find a link to our facebook page. The page opens in a new tab

![picture of footer](media/footer_sanitas_gym.png)

### Index page
---

- Hero image
    - Here you can see our hero image with an emerging headline "Sanitas gym". To clearly show you and other users what kind of site you have arrived at.

- Welcome message
    - Here you can see a messagge from us that describes our motto and a little about our gym.

    ![picture of moto](media/home_text_top.png)

- External links
    - Here are some useful external links with tips and tricks all customers
    ![picture of moto](media/home_links.png)
    

- Find Us

    - Here you can find a google map section that shows our location aswell as our adress. This section is located on the ondex page and uses a jump link to scroll down automatically.

    ![picture of Find us section](media/find_us_gym.png)
 
- Newsletter sign up
    - Here you can leave a your email adress to get our newsletter

    ![picture of newsletter signup](media/home_newsletter.png)


### Gym subscriptions
---

- Here you can subscribe to our all inclusive gym subscription. You can cancel at any time so you won't be billed for the folllowing months. If you have an active subscription you will see the red cancel button on the subscription and otherwise you will see the blue subscribe button

![picture of gym subscription](media/subscribe.png) 

![picture of gym subscription](media/subscription_cancel.png) 

### Personal trainer sessions
---

- Here you can purchase and schedule one hour personal trainer sessions. Add the number of sessions as you need to your shopping bag. After you have purchased sessions you can schedule them on the page. You vill see the available number of sessions you can schedule. All sessions can be canceled or edited up to one hour before it starts

![picture of personal trainer top section](media/pt_top.png)

![picture of personal trainer section](media/pt_session.png)

### Shopping bag page
---

- Here you can see the number of products in your shopping bag. You can update the quantity by using the increment/decrement buttons and press update. If you want to delete an item from your shopping bag you can press the delete button.

- If you are satisfied with the content of your bag you can proceed to the checkout via the "Go to checkout" button

- There is also a back to home page link that takes you back to the index page

![picture of shopping bag](media/bag.png)

### Checkout page
---

- At the top of the page you will see the content of your shopping bag with the individual and total price of a product

- The next section shows a form with the nessecary information to make a purchase. If you have made a previous purchase and checked "Save my information" the fields are already pre populated from information stored in the user profile.

- Form validations
    - "Full name" is required and takes maximum 100 characters
    - "Email" is required and takes maximum 254 characters and must have the corect email format
    - "Adress" is required and takes maximum 100 characters
    - "Post code" is required and takes maximum 20 characters
    - "City" is reuired and takes maximum 100 characters

- Save my personal info to my profile
 - A checkbox that saves the form information to the members profile and is automatically entered the next time you do a purchase

- Card information
    - Here is a field that you can enter your card information
    - Validators
        - If the wrong card information is entered a message is shown below the input that the information is incorrect
- Submit section
    - "Back to shooping bag" button takes you back to the shopping bag page
    - "Submit order" button tries to submit the order to stripe and creates an order instance in the database
     - Validators
        - If the bag is empty an error message is shown
        - If an card error occurs a message will be shown
    - Under the "Submit order" button a text will show how much your card will be chaged
    - In the bottom of the page you will find a link to get back to the home page

![picture of checkout page](media/checkout.png)

### Checkout success page
---

- When a purchase has gone through a checkout success page is shown. It includes order details and ordernumber
![picture of checkout success](media/checkout_success.png)

### Page not found
---
- A custom "page not found" page is shown if a page is not found. A short message and a link back to the index page is shown
![picture of page not found](media/404_page_not_found.png)

### Login Reggister and logout
---

- Register
    - if you don´t have an account you can create one here. The Link will be visible in the navbar if you are not logged in
    - Validators
        - All fields email are required
        - Email fields must have an email format and the confirmation field must match the first email field
        - Password confirm field must match the first pasford field

- Login 
    - Sign in page requires login name and password
    - "Remember me" checkbox is optional if you want the username and password to be saved
    - "Forgot password" link kan be used to reset password if you forget it.
    - You must be logged in to visit members page, add items to shopping bag, subscribe to a gymsubscription and purchase and schedule personal trainer sessions

- Logout
    - Before logging out a message will be promted and asks if you are sure if you want to sign out
        ![picture of login](media/Signin_sanitas.png)

        ![picture of logout](media/sign_out_sanitas.png)
        
        ![picture of register](media/signup_sanitas.png)

### Admin Site
---
- Here an admin user can log in to see an alter orders, user profile, users, products, categories and personal traier sessions 

    - Products handles the personal trainer session offers

    - Orders handles previous orders when purchasing a single payment such as personal trainer session

    - Stripe Customers handles active subscription. And stores the stripe plan and cusstomer id in our database

    - Profile stores saved customer information from previous purchases

    - Appoitments handles scheduled personal trainer sessions

    - Categories handles different product categories if other product types is added in the future 
    ![picture of product admin](media/products_admin.png)

    ![picture of order admin](media/order_admin.png)

    ![picture of appointments"Sessions" admin](media/admin_appointments.png)

## Features left to implement
---

- Ability to choose a specific personal trainer for your session

- Add limitations ffor when in the day you can schedule a training session

- Add more tiers on the subscriptions page to cater to all customers specific needs

- Add a Warning pop-up before cancelling a subscription

- Email verifications

- Email confirmation when signing up or purchasing/ scheduling sessions

- Past sessions will disapear from the list of sessions

- Add sorting of training sessions

# Testing
---

## Manual testing
---

### Navbar and footer
---

- All links work and the page you visit get underlined in the navbar
- Facebook link in footer works and opens up in a new window with rel=noopener atribute

### Home page
---

- Newsletter sign up
    - Signup form from mailchimp has been tested that it stores the mail adress on our mailchimp account
- External links work and opens in a new window with rel=noopener atribute

### Login / Logout and register
---

- A message is shown when successfully logging in and out
- A validation error is shown if email has the wrong format
- A validation error is shown if email and confirm email field does not match
- A validation error is shown if password is to similar to username
- A validation error is shown if the password and passwod conifmation field don´t match

### Gym subscriptions
---

- If you do not have a subscription a button will show in the subscription card that says 'Subscribe' it will take you to a checkout page hosted by stripe. After successful chekout you will be taken back to a sucess page hosted on the santitas site. If you go back to the subscriptions page you will see a new red button that says 'Cancel subscription'

![picture of stripe hosted checkout](media/stripe_checkout.png) 

![picture of cancel subscription](media/subscription_cancel.png)

- If you already have an active subscription and try to run the view 'create_checkout_session' from the url you will be redirected back to subscriptions page and shown an error message

- If don´t have an active subscription and try to run the view 'cancel_sub' from the url you will be redirected back to subscriptions page and shown an error message
    

### Personal Trainer
---

(Please observe that the time zone is set to CET in settings.py and can be changed if used in other time zone)

- Schedule session with personal trainer
    - Form works to submit and a session is saved to the database
    - If you have purchased a sesssion with a personal trainer you can see the available sessions. You can also see how many sessions you have purchased
    - Form validation
        - If you try to schedule a sessions with 0 available sessions you will get a form validation error
        - You try to schedule a session before current time plus one hour you will get a form validation error
        - If you try to schedule a session when you already have a sessionn at that time you will get a form validation error
        ![picture of Validation error](media/pt_val_no_sessions.png)

        ![picture of Validation error](media/pt_val_no_time.png)

        ![picture of Validation error](media/pt_val_double_session.png)

- Edit Session
    - Edit button takes you to the edit page. "Save" button updates the database with new time and date. "Back" button takes you back to the personal trainer page
    - "Cancel session" button shows a modal with the question if you sure. "Cancel" button cancels the session and "Close" button closes the modal
    - On the edit page all form validations are show in the same way as on the create form
    - If a scheduled session is closer in time than one hour you can no longer edit or cancel it

    ![picture of session to close](media/pt_session_to_close.png)

    - If you try to edit another users session via the url you will be taken to a page with a message that you are trying to edit another users session.

    ![picture of Validation error](media/pt_edit_other_user.png)

    - If you try to delete an other users session via the url get shown a message that you are trying to delete another users session

- Purchase personal trainer session
    - increment and decrement buttons changes the value in input window
    - "Add to bag" button works and add the correct quantity to the shopping bag. Adding product again increments the quantity in the shopping bag
    - A message is shown when a product is added to the shopping bag


### Shopping bag page
---

- Increment and decrement buttons changes the value in input window
- "Update bag" and "Delete from bag" links both work as expected
- A messages is shown when an item is deleted or updated in the shopping bag
- "Go to checkout" button takes you to checkout page with the correct shopping bag
- "Back to home page" link works and takes you back to the home page

### Checkout page
---

- The corret product, quantity, price and total is shown
- A validation error is shown if any of the fields "Full name", "Adress", "Post code", "City" is left empty
- A validation error is shown if the email field has the wrong format.
- If checkobox "Save my info to my members page" is unchecked the members profile page don´t get updated
- If an invalig card number is entered an error message is shown below
- If you press the "Submit order" button an order is created in the database, the a purchase is added to stripe and you are taken to the success page
- "Back to shopping bag" takes you to the shoppingbag
- "Back to home page" link works and takes you back to the home page
- "Save my info to my members page" checkbox saves adress to the profile database if it is checked

### Members/Profile page
---

- User profile is already populated if save checkbox is checked on checkout
- Validation on all field works
- "Update" button works and successfully saves the new user profile
- Order history is shown in the bottom of the page


### If user is not logged in
---

- Members page
    - If you try to click members page you get redirected to login page with a message shown that you need to be logged in.
- Shopping bag page
    - If you try to click the shopping bag you get redirected to login page with a message shown that you need to be logged in.
- Subscriptions page
    - If you enter the subscription page you will see the subscription information but where the button to subscribe or cancel subscription you will see a link to login page
    - If you try to run views 'create_checkout_session' and 'cancel_sub' via the url you get redirected to log in page

    ![picture of Subscriptions not logged in](media/not_auth_subscriptions.png)

- Personal trainer page
    - If you enter the personal trainer page you will see a link to the login page that says you need to be logged in to schedule and purchase sessions
    - If you try to run the views 'edit_appointment' or 'delete_appointment' from url you get redirected to login page

    ![picture of Personal trainer page not logged in](media/not_auth_personal_trainer.png)

### Light house testing 
---

- Lighthouse testing is made on all main pages. All tests passed, however there is a bad test result on performance on the home page. I think it is because of the hero image. I have already compressed the image two times but I only seam to get it down to 1 mb from 4 md. 
    - Home page
        ![picture of lighthouse test home page](media/lighthouse_home_new.png)
    - Subscriptions page
        ![picture of lighthouse test subscriptions page](media/Lighthouse_subscription.png)
    - Personal trainer page
        ![picture of lighthouse test personal trainer page](media/lighthouse_personal%20trainer.png)
    - Shopping bag page
        ![picture of lighthouse test shopping bag page](media/lighthouse_bag.png)
    - Checkout page
        ![picture of lighthouse test checkout page](media/lighthouse_checkout.png)
    - Profile page
        ![picture of lighthouse test Profile page](media/lighthouse_profile.png)

### Validator testing
---

- HTML using https://validator.w3.org/ . All pages passed except for django template variables which produces bad value errors
    - bag.html
    - checkout_success.html
    - checkout.html
    - home_js.html
    - index.html
    - edit_session.html
    - pt_sessions.html
    - profile.html
    - cancel.html
    - stripe_subscriptions.html
    - success.html
    - base.html
    - page_not_found.html
    - server_error.html

- Css using https://jigsaw.w3.org/css-validator/ All pages passed without errors
    - checkout.css
    - home.css
    - style.css
    - subscriptions.css
    
- Python using https://pep8ci.herokuapp.com/ All paes passed without errors
    - bag app
        - admin.py
        - contexts.py
        - models.py
        - urls.py
        - views.py
        - bag_tools.py
    - checkout app
        - admin.py
        - forms.py
        - models.py
        - signals.py
        - urls.py
        - views.py
        - webhook_handler.py
        - webhooks.py
    - home app
        - admin.py
        - models.py
        - urls.py
        - views.py
    - products app
        - admin.py
        - models.py
        - urls.py
        - views.py
        - forms.py
    - profiles app
        - admin.py
        - models.py
        - urls.py
        - views.py
        - forms.py
    - subscriptions app
        - admin.py
        - models.py
        - urls.py
        - views.py
    - sanitas_gym project
        - settings.py
        - urls.py
        - views.py
    - root
        - custom_storages.py
        - manage.py

- Java script using https://jshint.com/ All pages passed with out errors
    - stripe_elements.js
    - quantity_input_script.html (script tags within document)
    - stripe_subscriptions.js



### Unfixed bugs
---

- Affter installing stripe the confirm email function on all auth stopped working. The link for the confirm email page was not apperaring in the console. So email verification was turned of in settings.py

### Fixed bugs
---

- Update cart button did not work.
    - Fix: the session seamed to have something to to with it because when I deleted the session the button started working again.

- Webhooks did not work
    - Fix: ports where set to private instead of public

- Webhooks and success page stopped working for subscriptions
    - Fix the url for the local enviroment had changed so it called the wrong url


## Deployment
---

### Database
---

- Create a new database on ElephantSQL
    - Create a new instance
    - Give it a name
    - Select the free plan "Tiny Turtle"
    - Select region closest to you
    - Copy the data base url from new instance

### Heroku
---

- Create a new app  on Heroku 
    - Pick a name for your app
    - Choose region
    - Delete the Heroku postgres add-on under the resource tab which is added automatically. If you don't it will overwrite your database_url from ElephantSQL (learned that the hard way)
    - Under settings press the button "reveal config vars" add "DATABASE_URL" variabel with key URL from ElephantSQL and all config variables from your env.py file needed to run the app

### Project code preparations and heroku settings
---

- Install packages dj_database and psycopg2 using command "pip3 install dj_database_url==0.5.0 psycopg2"
- Freeze packages to your requirements.txt using command "pip freeze > requirements.txt"
- Changes to settings.py file
    - Import os and import dj_database_url at the top of the file
    - In the DATABASES section
        - Comment out your default database used in local enviroment like sqlite3
        - Connect to new database on Elephantsql using snippet below
            ```
             DATABASES = {
                'default': dj_database_url.parse('your-database-url-here')
                }
            ```
        - Run command "python3 manage.py showmigrations" to show migrations that has not yet been migrated to the new database
        - Run command "python3 manage.py migrate" to migrate to new database
        - Run command "python3 manage.py createsuperuser" to create a new superuser for the new database on Elephantsql
        - Add if statement below to use Elephantsql database when running live version on Heroku and sqlite3 database when running app locally

            ```
            if 'DATABASE_URL' in os.environ:
                DATABASES = {
                    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
                }
            else:
                DATABASES = {
                    'default': {
                        'ENGINE': 'django.db.backends.sqlite3',
                        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
                    }
                }
            ```
        - In ElephantSQL database instance press browse and check that the tables and your new superuser has been added to the data base
- Preparation for running app on heroku
    - Run command "Pip install gunicorn" to installl gunicorn which will work as a webserver
    - Freeze packages to your requirements.txt using command "pip freeze > requirements.txt"
    - Create a procfile which will tell heroku to create a webdyno which will run Gunicorn and serve our django app. The procfile should contain "web: gunicorn sanitas_gym.wsgi:application"
    - Log in to heroku app using command "heroku login -i" give email adress when prompted and api key fom settings tab in heroku when prompted to enter a password
    - Disable collect static with command " heroku config:set DISABLE_COLLECTSTATIC=1 --app sanitas-gym"
    - In settings.py under ALLOWED_HOSTS add ['sanitas-gym.herokuapp.com', 'localhost'] to allow both heroku app and local enviroment to access
    - Commit changes and push to github
    - Deploy to Heroku using command "git push heroku main". If you initialize your app on the web site you may have to initialize the app remote using command "heroku git:remote -a sanits-gym" before deploying to heroku
    - In Heroku app go to deploy tab. Choose deployment method github and find your repository and click connect
    - Enable automatic deploy so that when a new version is saved the app is deployed automatically
    - Generate a new django secret key using a key generator. Add new secret key to heroku config vars
    - Remove any live credentials from settings.py and instead use a enviroment variable like os.environ.get('SECRET_KEY',) from env.py
    - Add if statement to turn on DEBUG in settings.py if there is an enviroment variable 'DEVELOPMENT'. See example below
        ````
            if os.environ.get('DEVELOPMENT'):
                debug_on = True
            else:
                debug_on = False

            DEBUG = debug_on
        ```
    - Commit and push to github


### Amazon web services and static files
---

- Create an account on amazon web services
- Sign in and enter management console under my account
- Search for service S3
- Create a new bucket and allow public access. Enable ACLs and choose Bucket Owner preferred
- In the new bucket in the properties tab turn on static web site hosting and choose "Use this bucket to host a website". Fill in default values and press save
- In the permissions tab
    - Set CORS configuration. which allows access between heroku app and s3 bucket. Add code below to the CORS field
    ```
            [
        {
            "AllowedHeaders": [
                "Authorization"
            ],
            "AllowedMethods": [
                "GET"
            ],
            "AllowedOrigins": [
                "*"
            ],
            "ExposeHeaders": []
        }
    ]
    ```
    - Go to bucket policy and select policy generator to create a policy. 
        - Choose policy type S3 bucket policy 
        - Allow all principals by ussing a "*"
        - Choose action get object
        - Copy ARN number from policy tab and paste it to arn box at the bottom
        - Click add statement
        - Click generate policy
        - Copy policy in the the policy editor on the permissions tab and add a /* after like resource: .. sanitas-gym/* to allow access to all resources in bucket
        - Choose the following settings in the ACL section: Bucket owner: objects_ [list=x, write=x], BucketACL_ [read=X, write=x] Everyone: Objects_ [list=x ,]

- Go back to services menu and open IAM service
    - Click User Groups
        - Create a new group and name it 
    - Create Policy go to JSON tab and click import managed policy search for S3 and import S3 full access policy
    - Get the bucket ARN number from S3 bucket
    - In the JSON field in IAM paste two rows in a list as the resource value like the example below
    ```
      Resource: ["arn233242342:::sanitas-gym",
        "arn233242342:::sanitas-gym"/*]
    ```
    - Click next, (tags are optional) until you get to review policy. Give it a name and description and click create policy
    - Go back to User Groups and click your created user group go to permissions tab open "add permissions" and click attach polecies select the polecy and click add permission. and attach policy. 
    - Create a user and pick a name. Put user in group
    - Access the user and click security credentials and click access keys to give programaticall access. Create and download the csv file which will include secret credentials keys

- In gitpod install packages boto3 using command "pip install boto3"
- In gitpod install packages django storages using command "pip install django-storages"
- Freeze packages to your requirements.txt using command "pip freeze > requirements.txt"
- Add storages to installed apps in settings.py
- Add the following code snippet to settings.py
```
if 'USE_AWS' in os.environ:
    # Cache control
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }

    # Bucket config 2
    AWS_STORAGE_BUCKET_NAME = 'sanitas-gym'
    AWS_S3_REGION_NAME = 'eu-north-1'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    # Static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    # Static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
    

```
- Add AWS_ACCESS_KEY_ID , AWS_SECRET_ACCESS_KEY to enviromentals variables on heroku settings. Theses can be found in the csv file downloaded from AWS

- Create new file in root level "custom_storages.py" to tell django to fetch static and media files from s3 aswell as uploaded images
    - Add the following code snippet:
    ````
        from django.conf import settings
    from storages.backends.s3boto3 import S3Boto3Storage


    class StaticStorage(S3Boto3Storage):
        location = settings.STATICFILES_LOCATION


    class MediaStorage(S3Boto3Storage):
        location = settings.MEDIAFILES_LOCATION
    ```
- Commit and push to github
- Top of snippet under comment "# cache controle" is added to handle cashing of files to increase user performance
- In S3 bucket create folder called "media" with bucket settings
    - Click upload
    - Choose all images you need to upload
    - Grant public access to objects
    - Click next then upload




## Credits
---

### Borrowed code
---

#### Bag app

- Context.py 
    - All of the strucutre, logic, function and variable names are taken from Code institute project lessons Boutique ado
- views.py 
    - Most of the logic and function, variable names are taken from Code institute project lessons Boutique ado
- urls. py 
    - All of url names is taken from boutique ado walkthrough project
- bag_tools.py
    - All of the strucutre, logic, function and variable names are taken from Code institute project lessons Boutique ado
- bag.html
    - Main structure and variable names are taken from boutique ado walkthrough 

#### Checkout app
- stripe_elements.js
    - all code is taken from stripe documentation and Code institute project lessons Boutique ado
- forms.py
    - class names and method is taken from boutique ado project
- checkout.css
    - Most of the code is taken from Code institute project lessons Boutique ado / stripe documentation
- webhooks.py
    - All code is taken from Code institute project lessons Boutique ado
- webhook_handler.py
    - All code is taken from Code institute project lessons Boutique ado
- Signals.py in checkout app
    - All code is taken from Code institute project lessons Boutique ado
- admin.py in checkout app
    - Most of the structure and variable and class names is from Code institute project lessons Boutique ado
- apps.py in checkout app
    - One line of code is taken from Code institute project lessons Boutique ado
- views.py in checkout app
    - Most of the code structure, logic , class names, variable names and logic is taken from Code institute project lessons Boutique ado
- checkout.html
    - Main structure and some variable names is taken fromm boutique ado

#### Home app

- homs.css
    - hero-image selector is taken from w3 schools https://www.w3schools.com/howto/howto_css_hero_image.asp

#### Products app

- quantity_input_script.html
    - All of the code is taken from boutique ado walkthrough project


#### Profile app

- profile.html
    - Most logic and structure is taken from boutique ado walkthrough project

- models.py 
    - Last part of document rows 24 - 40 are heavily influenced by Code institute project lessons Boutique ado
- Views.py
    - Structure and logic are taken from Code institute project lessons Boutique ado
- forms.py
    - class method row 20-33 is taken from boutique ado project

#### Subscriptions app
- models.py
    - code is taken from https://testdriven.io/blog/django-stripe-subscriptions/
- stripe_subscriptions.js
    - code is taken from https://testdriven.io/blog/django-stripe-subscriptions/
- views.py
    - most of the logic, variable names and structure is taken from https://testdriven.io/blog/django-stripe-subscriptions/
- urls. py
    - most of the logic, variable names and structure is taken from https://testdriven.io/blog/django-stripe-subscriptions/


#### Misc
- index.html
    - Hero image is taken from https://www.w3schools.com/howto/howto_css_hero_image.asp
- Google maps section
    - code is taken from Code institute lessons on apis
- Mailchimp newsletter sugnup section is taken from https://mailchimp.com

- timer java script function in base.html is taken from a Code institute lesson


## Content
---

- The site is styled with bootstrap and css

- Icons are taken from fontawsome

- Font 'Robot condensed' is taken from google fonts 

- Google maps section is provided by google

- Newsletter signup is provided by mailchimp

- Mockups is made with https://balsamiq.cloud/

- Data base models schema is made with https://lucid.app/


### Media
---

- Images are taken from pexels.com

# Business plan 
---

- Business goals
    - Even thou we have a physical location for our gym we see the importance of incorporating e-commerce in our business model. We have a B2C strategy and focuses on customers in södermalm part of Stockholm Sweden. To be able to reach our customers and offer extra services from our gym such as classes and personal trainer sessions. We also want our customers to be able to manage their gym subscriptions from our web application. We also want them to be able to purchase and schedule sessions with our personal trainers from home. It is easier to reach customers and get them to convert in the comfort of their own home. 

## Marketing
---

- Social media

    - Facebook
        - We have a facebook page where we are hoping to grow our comunity organically. This is a solid and free marketing option.
        You can see som imagges below
        ![picture of facebook page](media/sanitas_facebook.png)
        ![picture of facebook page](media/sanitas_facebook2.png)

    - Social media ads
       - We are using paid soccial media ads that is shown mainly on instagram and facebook. The ads have teritory restrictions so they only target potential customers in the vicinety of our location

    - Newsletter 
        - On our main page there is a section for leaving your email adress to stay up to date with new offers, classes and subscriptions. This is also a free and great way to stay in contact with your members and create customer retention.

- Googgle seo
    - Efforts have been made to optimize our landing page to match key words of our choice to create organic trafic.
    This is also a great and free way to get new customers 

### Seo 
---

#### Key words
- Short tail keywords
    - Gym
    - Affordable gym
- Longtail keywords
    - Gym södermalm
    - Best gym södermalm
    - Gym with fitness classes
    - Personal trainer
    - Gym with sauna
    - Gym with pool

- Choice of keywords:
    - For short tail keywords I have choosen a general term "Gym" and "Affordable gym". But i think it still works since we only have one gym location and google knows where you are so the results felt relevat anyway . Googel will present you with the closest options. An auto complete option that google presented me with was "Affordable gym" which had less searches on it and felt more competative.

    - For long tail key words i have choosen two key words that includes södermalm which is the part of stockholm where the gym i situated. Another suggestion by google where "best gym södermalm". To be more competative the rest of the keywords focus on our services and facileties. Local competitors does not offer the same services. "Gym with fitness classes" and "gym with sauna and pool" have ok search volume and are more competative than broader search terms.

    - In my analysis I have taken in to consideration relevance authority and volume aswell as competition.
    I wanted to use a service like wordtracker.com but Sweden was not an option for teritory unfortunately.


# Data models schema
---

- Appointments
    - Has two fields Date_time and one foreign key to the user model. That way you can store at what time the sessions is scheduled for each user.
- Subscriptions
    - Has three fields with customer , subscription id and has a foreign key to the user model. To keep track of what subscription is tied to what customer and user.
- Products
    - products has 5 fields with standard product info such as price, name decription. It also has a foreign key to the model categories. Today there are only one category of product but in the future as more is added the setup with categories is already set.
- Categories
    - This is a simple model with two fields for name and friendly name with no foreign keys
- Orders
    - Has fields for customer info like adress, name, email etc. With one foreign key to Profile so you can connect a user profile with an order and save your customer info to your profile..
- Order items
    - Are all the information about the purchased items such as quantity, order total, products. It has three foreign keys:
        - Foreignkey to "User model" to connect purchased items to a user. In this case it is needed to calculate the number of purchased personal trainer sessions for a user.
        - Foreignkey to "Products model" to connect a product to order items instance.
        - Foreignkey to "Order model" every order items insctance is tied to a an order so that you know which order number and date etc is connected to purchased items 
- Profile
    - Consists of fields that is saved customer info that is prepopulated in the checkout if it is previuosly saved.

- Below you can find a schema of the all database model relationships
![Datamodel schema](media/data_models_schema.png)



# Responsiveness
---

- All pages are tested that they are responsive on all modern screens min width 320px 
    - Home
    ![picture of home page mobile](media/home_mobile_top.png)
    ![picture of ](media/home_mobile_find_news.png)
    - Subscriptions page
    ![picture of subscriptions page mobiel](media/subscription_cancel.png)
    - Personal trainer page
    ![picture of personal trainer page mobile](media/pt_mobile_bottom.png)
    - Shopping bag page
    ![picture of shopping bag page mobile](media/bag_mobile.png)
    - Chechout page
    ![picture of checkout page mobile](media/checkout_mobile.png)
    - Profile
    ![picture of profile page mobile](media/profile_mobile.png)


# Design
---
- The design for the site is kept simple with the navbar always showing. The navigation links is turned in to a button on smaller screens.
The navigation links is underlined so you as a user know where on the site you are. We have picked a blue color palette for the site which represent trust, stability and calmness. Buttons are colored clearly in a geen color to proceed with an action and red to cancel, or reverse an action. We have choosen a black color for all fonts to give sufficient contrast to the background making it easy to read.
External links are opened in new tab on the browser with a noopener attribute. In the footer we choose to only have our facebookpage link to encourage you to visit out community because it is a vital part of our marketing. Below you can find images of our design mockups.  

## Mockups
---

- This is mockups created on balsamic.com
    - Home
    ![picture of mockups home page](media/mockup_home.png)
    - Subscriptions page
    ![picture of mockups subscription page ](media/mockup_sub.png)
    - Personal trainer page
    ![picture of mockups personal trainer page ](media/mockup_pt.png)
    - Shopping bag page
    ![picture of mockup shopping page ](media/mockup_bag.png)
    - Chechout page
    ![picture of mockup checkout page ](media/mockup_checkout.png)
    - Profile
    ![picture of mockup profile page ](media/mockup_profile.png)
