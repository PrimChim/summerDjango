# Blog Application Summer Django class
During the summer of 2023 at Herald College Kathmandu. I created this blog application using Python Django Framework.

To download and use the project on your local machine. Follow below-mentioned steps:
- You can clone the project
  - If the SSH is not set in your local machine and GitHub you can go with option 1 otherwise option 2
    - Option 1
      
    ```
    git clone https://github.com/PrimChim/summerDjango.git summerproject
    ```
    - Option 2

    ```
    git clone git@github.com:PrimChim/summerDjango.git summerproject
    ```
- Set the Environment
  - Go to the folder
  ```
  cd summerproject
  ```
  - Create the isolated environment(virtual environment or venv)
    - You can create the virtualenv with virtualenv [library](https://virtualenv.pypa.io/en/latest/) or python env click [here](https://docs.python.org/3/library/venv.html)
    - Installing the libraries
      - Install from requirements.txt
      ```
      pip install -r requirements.txt
      ```
- Run the project
  - Setting up the environmental variables
    - In the root project create a file named .env you can use code editors like vs code
    - Populate the files with the below-mentioned variables
      - SECRET_KEY=YOUR-SECRET-KEY
      - DATABASE=YOUR-DATABASE-URL
      - EMAIL_HOST_USER=YOUR-EMAIL-ADDRESS
      - EMAIL_HOST_PASSWORD=YOUR-EMAIL-PASSWORD
      
  - Migrate the database
  ```
  python manage.py migrate
  ```
  - Run the project
  ```
  python manage.py runserver
  ```
  
# Main Features
- User Management System
- Dynamic Email Sending
- CRUD operation for the Blog

# Want to Collaborate
- You can add the new features and add to the new branch and send a pull request

  **Have a great day**

  **Bye 👋 Bye 👋**
