## Functional Requirements
1. User Registration
2. User Login
3. User Logout
4. Create Recipe
5. Edit Recipe
6. Delete Recipe
7. View Recipe
8. Search Recipe
9. Rate Recipe
10. Comment on Recipe
11. View User Profile
12. Edit User Profile
13. Save Recipe
14. View All Recipes
15. Filter Recipe

<using the syntax [](images/ui1.png) add images in a folder called images/ and place sketches of your webpages>

## Non-functional Requirements
1. non-functional
2. non-functional

<each of the 14 requirements will have a use case associated with it>
## Use Cases <Add name of who will write (this specific requirement) and implement (in subsequent milestones) the use case below>

1. User Registration (Jhenaro Flores)
- **Pre-condition:** User must be able to access the website successfully.
- **Trigger:** User wants to register an account to the food web app.
- **Primary Sequence:** 
1. The user goes to the website
2. System shows user a login page with a register button under it.
3. User clicks the register button.
4. System takes user into the register page.
5. System asks for user to input a username and password.
6. User inputs a username and password
7. System saves username and password into the databse.
8. System tells user that the account has been registered.

- **Primary Postconditions:** The User has registered.
- **Alternate Sequence:** 
1. The user inputs a username that has already existed in the database.
2. System shows an error message to try to input again.

#
2. User Login (Jhenaro Flores)
- **Pre-condition:** User must have a registered account.
- **Trigger:** User wants to log in to the food web app.
- **Primary Sequence:** 
1. The user goes to the website
2. System shows user a login page
3. User inputs username and password that was registered
4. User clicks the login button
5. System checks if the username and password are registered into the database.
6. System shows user the contents of the food recipe web app.
   
- **Primary Postconditions:** The User has logged into the website and can see the contents of the website.
- **Alternate Sequence:** 
1. The user inputs a wrong username / password.
2. System shows user that they inputted a wrong username / password.

#
3. User Logout (Jhenaro Flores)
- **Pre-condition:** User is logged into the website.
- **Trigger:** User wants to log out of the website.
- **Primary Sequence:** 
1. The user is logged into the food recipe web app.
2. User clicks the logout button.
3. System logs user out of the website.
4. User is taken back to the login page.
   
- **Primary Postconditions:** The User has logged out of the website and is back into the login page.
- **Alternate Sequence:** 
1. Login button does not work

#
4. Create Recipe (Jhenaro Flores)
- **Pre-condition:** User is logged into the website.
- **Trigger:** User wants to create a recipe.
- **Primary Sequence:** 
1. System shows a "Create Recipe" button in the corner of the website.
2. User clicks the "Create Recipe" button
3. The system navigates the user to the create recipe page.
4. User is required to input the details: Title, Ingredients, Steps/Instructions, Cooking Time, and an image of the food item.
5. The user clicks "Save Recipe"
6. System saves the recipe into the data base.
7. System confirms to the user that the recipe has been created.
   
- **Primary Postconditions:** The User was able to create a food recipe.
- **Alternate Sequence:** 
1. The user did not input one of the needed details and tried to save the recipe.
2. The system shows an error message if the user tries to save a recipe with missing details.

#
5. Edit Recipe (Jhenaro Flores)
- **Pre-condition:** User must have recipes saved.
- **Trigger:** User wants to edit a recipe.
- **Primary Sequence:** 
1. User goes into the "Recipes" page.
2. System takes user into the "Recipes" page and shows user their saved recipes.
3. System shows that there is an "Edit Recipe" button into the recipes.
4. User clicks the Edit Recipe button.
5. System takes user into the Edit Recipe page.
6. System shows the details of the recipe that would be editable. (Title, Ingredients, Steps/Instructions, Cooking Time, and an image of the food item.)
5. User inputs the needed details and once done clicks "Save Recipe"
6. System saves the edited recipe into the database and replaces the old one with the edited one.
7. System confirms to the user that the recipe has been saved/edited.
9. System shows user the updated recipe.
   
- **Primary Postconditions:** The User was able to edit the recipe successfully.
- **Alternate Sequence:** 
1. The user does not input one of the needed details.
2. System shows user an error message to complete inputting the details needed.

#
6. Delete Recipe (Ryan Tang)
- **Pre-condition:** User is logged in and is the owner/editor of the recipe
- **Trigger:** User clicks on the delete button for the selected recipe they want removed
- **Primary Sequence:**
1. System verifies and confirms that user owns recipe
2. User select delete button
3. System displays confirmation dialog for deleting recipe
4. User confirms deletion
5. System deletes recipe from database
6. System displays a success message confirming deletion

- **Primary Postconditions:** Recipe is successfully removed from the system and page is removed
- **Alternate Sequence:**
1. If user cancels confirmation fo wanting to delete, dialog closes and nothing happens
2. If user isn't the owner of the recipe, will show an error message and won't allow deletion

#
7. View Recipe (Ryan Tang)
- **Pre-condition:** Recipe exists in the database
- **Trigger:** User clicks on recipe link or selects a recipe from searching it
- **Primary Sequence:**
1. User searches for certain recipe
2. System checks if recipe data is in the database
3. User clicks on recipe they want displayed
4. System displays recipe details including ingredients, steps, comments, and ratings

- **Primary Postconditions:** User is able to view the recipe in full detail
- **Alternate Sequence:**
1. If recipe doesn’t exist, has been deleted, or isn’t in the database, an error message will occur

#
8. Search Recipe (Ryan Tang)
- **Pre-condition:** User is on main page or is using the search bar
- **Trigger:** User is entering keywords into the search bar
- **Primary Sequence:** 
1. User types recipe name/ingredient into search bar
2. System receives search and filters recipe by keywords(such as recipe name and ingredients)
3. System displays a list of matching recipes accordion what is searched

- **Primary Postconditions:**
1. There are matching recipes being displayed
2. No matching information was displayed
-  **Alternate Sequence:** 
1. A “no results found” message will be displayed if there is no recipe matching keywords

#
9. Rate Recipe (Ryan Tang)
- **Pre-condition:** User is logged in and has viewed a recipe
- **Trigger:** User clicks on a star rating from 1-5 stars
- **Primary Sequence:** 
1. User clicks into a recipe to view recipe details
2. User clicks on the stars between 1-5 stars
3. System takes rating input from user
4. System updates recipe’s average rating in database
5. System confirms that rating was submitted
6. If user decides to change rating, it will re update input from user and update recipe’s average

- **Primary Postconditions:** recipe rating is updated and stored
- **Alternate Sequence:**
1. If user is not logged in, system will tell user to login before rating and will pop up login screen

#
10. Comment on Recipe (Ryan Tang)
- **Pre-condition:** User is logged in and is viewing the recipe
- **Trigger:** User enters a comment into the comment box and clicks “submit”
- **Primary Sequence:**
1. User is on recipe page
2. System captures the comment that has been inputted
3. System stores comment into the database with Username/ID and timestamp
4. System displays new comment in the recipe page

- **Primary Postconditions:** Comment is stored and is visible to other users in the recipe page
- **Alternate Sequence:**
1.User is not logged in and system will pop up login
2. Comment is empty or is longer than the maximum amount of words and will show an error message


#
11. View User Profile
- **Pre-condition:**
- **Trigger:** 
- **Primary Sequence:**
1. 

- **Primary Postconditions:**
- **Alternate Sequence:**
1.

#
12. Edit User Profile
- **Pre-condition:**
- **Trigger:** 
- **Primary Sequence:**
1. 

- **Primary Postconditions:**
- **Alternate Sequence:**
1.

#
13. Save Recipe
- **Pre-condition:**
- **Trigger:** 
- **Primary Sequence:**
1. 

- **Primary Postconditions:**
- **Alternate Sequence:**
1.

#
14. View All Recipes
- **Pre-condition:**
- **Trigger:** 
- **Primary Sequence:**
1. 

- **Primary Postconditions:**
- **Alternate Sequence:**
1.

#
15. Filter Recipe
- **Pre-condition:**
- **Trigger:** 
- **Primary Sequence:**
1. 

- **Primary Postconditions:**
- **Alternate Sequence:**
1.
