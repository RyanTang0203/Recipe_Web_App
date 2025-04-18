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
- **Trigger:** User clicks on the “delete” button for the selected recipe they want removed
- **Primary Sequence:** 
1. System verifies and confirms that user owns recipe
2. User select delete button
3. System displays confirmation dialog for deleting recipe
4. User confirms deletion
5. System deletes recipe from database
6. System displays a success message confirming deletion
  
- **Primary Postconditions:** Recipe is successfully removed from the system and page is removed
- **Alternate Sequence:** 
1. If user cancels confirmation of wanting to delete, dialog closes and nothing happens
2. If user isn’t the owner of the recipe, will show an error message and won’t allow deletion

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

- **Alternate Sequence:** 
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
1. User is not logged in and system will pop up login
2. Comment is empty or is longer than the maximum amount of words and will show an error message


#
11. View User Profile (Yuzhen Kuang)
- **Pre-condition:** The user must be logged in.
- **Trigger:** The user clicks on the “Profile” or username link.
- **Primary Sequence:**
1. The system retrieves the user’s profile details from the database.
2. The system displays the profile information

- **Primary Postconditions:** The profile page is successfully displayed to the user.
- - **Alternate Sequence:**
1. If the user is not logged in, the system redirects them to the login page.

#
12. Edit User Profile (Yuzhen Kuang)
- **Pre-condition:** The user must be logged in and viewing their own profile.
- **Trigger:** The user clicks the “Edit Profile” button.
- **Primary Sequence:** 
1. The system displays the profile edit form.
2. The user updates their profile fields.
3. The user submits the changes.
4. The system validates and saves the updates.
5. The system shows the updated profile information.

- **Primary Postconditions:** The user's profile is updated in the database.
- - **Alternate Sequence:**
1. If validation fails (invalid email), the system displays an error message and does not save changes.

#
13. Save Recipe (Yuzhen Kuang)
- **Pre-condition:** The user must be logged in and viewing a recipe.
- **Trigger:** The user clicks the “Save” or “Bookmark” button on a recipe.
- **Primary Sequence:**
1. The user clicks the “Save” or “Bookmark” button.
2. The system checks if the user is logged in. 
3. The system adds the recipe to the user’s saved list in the database.
4. The system updates the UI and shows a success message. 

- **Primary Postconditions:** The recipe is saved to the user’s saved recipes collection.
- - **Alternate Sequence:**
1. If the user is not logged in, the system redirects them to the login page.

#
14. View All Recipes (Yuzhen Kuang)
- **Pre-condition:** The user must be logged in and viewing all recipe.
- **Trigger:** The user navigates to the “All Recipes” page or home page.
- **Primary Sequence:** 
1. The system sends a request to the database to fetch all recipe records.
2. The system receives the list of recipes and sorts them by creation date or popularity.
3. The system generates HTML to display recipe cards/titles
4. The system displays a grid of all available recipes.

- **Primary Postconditions:** The user can browse all recipes.
- - **Alternate Sequence:**
1. If there are no recipes, the system displays a message like “No recipes found.”

#
15. Filter Recipe (Yuzhen Kuang)
- **Pre-condition:** The user is on the “All Recipes” page.
- **Trigger:** The user selects a filter. 
- **Primary Sequence:**
1. The user selects one or more filter options. 
2. The system captures the selected filter parameters and sends a query to the backend.
3. The backend filters the recipes from the database based on the selected criteria.
4. The system displays the filtered results. 
5. The user reviews the new set of filtered recipes.

- **Primary Postconditions:** Only recipes matching the filter are shown.
- - **Alternate Sequence:**
1. If no results match the filter, the system displays a message like “No matching recipes found.”
