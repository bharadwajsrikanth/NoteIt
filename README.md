# NoteIt

This application allows a registered user to be able to add a note, view the notes and delete a note. 
A user can register through their email and log in to the application. Once logged in, user will be able to create new notes, view the old notes, and delete the old notes. 

The application server runs on the local machine on port 5000. User can access the application by going to the URL `http://127.0.0.1:5000/` on their browser.

## Setup

This application can be setup by following these steprs:
1. Clone this repository
2. Install the required packages. The required packages are listed in requirements.txt. Each of them can be installed individually or in a virtual environemt by activating the virtual envoronment and executing `pip install -r requirements.txt`.
3. Run *main.py* `python main.py`.
4. Go to `http://127.0.0.1:5000/`

## Usage
1. Go to `http://127.0.0.1:5000/`
2. First time users need to register with your email id by going to the `Register` page.
3. Once registered, users can log in on the `Login` page.
4. Logged in users can add, view, delete notes on their `Home` page.
5. Logout by clicking the `Logout` button.
