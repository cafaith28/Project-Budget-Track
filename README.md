Construction Project Budget Tracker

Project Description

For my CISC106 final project, I created a Construction Project Budget Tracker using Python and Drafter. The purpose of this website is to help users keep track of construction material expenses and see how much of their project budget they have spent.

Users can enter a project name and starting budget, then add materials along with their unit prices and quantities. The website calculates the total cost of each material and adds everything together to determine the overall project expenses. It also shows how much money is remaining in the budget or how much the project has gone over budget.

I chose this project because I am studying civil engineering and have experience working in the construction industry. I wanted to create something that connected what I have learned in computer science to something I could potentially use in my career.

Website Features

- Create a Project: Enter a project name and starting budget.
- Add Materials: Enter the name, unit price, and quantity of construction materials.
- Track Expenses: Automatically calculate the total cost of each material and the overall project expenses.
- Monitor Budget: See whether the project is under, over, or exactly on budget.
- Edit Materials: Update previously entered materials if their price or quantity changes.
- Remove Materials: Delete materials that are no longer needed.
- Project Summary: View an overview of the project budget and expenses.

How the Website Works

When the website first opens, the user enters a project name and a total budget. Once that information is submitted, the user is brought to the project dashboard.

From the dashboard, users can add construction materials by entering their name, unit price, and quantity. Each material is assigned a unique ID so that it can be edited or removed individually, even if multiple materials have the same name.

The website uses the entered information to calculate the total cost of each material. It then adds those costs together and compares the total expenses to the original project budget. Any time a material is added, edited, or removed, the displayed expenses and remaining budget are updated.

Programming Concepts Used

Throughout this project, I used several programming concepts we learned in CISC106.

- Dataclasses: Used to organize project information and store individual materials.
- Lists: Used to keep track of all the materials added to the project.
- Functions: Used to perform calculations, find materials, validate inputs, and handle different website actions.
- Loops: Used to go through the material list and calculate the total expenses.
- Conditional Statements: Used to check user inputs and determine whether the project is over or under budget.
- Drafter Routes: Used to create different pages and allow users to navigate between them.
- Unit Tests: Used to check that helper functions return the expected results.

Challenges and What I Learned

One of the biggest challenges I faced was figuring out how to manage information between different pages in Drafter. I needed to make sure that the project name, budget, and list of materials stayed available when the user moved between the dashboard and other pages.

Another challenge was getting the budget calculations to update correctly whenever a material was added, edited, or removed. I worked through this by separating some of the calculations into helper functions and using the material list to calculate the total expenses.

I also ran into errors involving incorrect data types, undefined variables, and website routes. Debugging these issues helped me better understand how different functions work together and how to identify problems in my code.

Finally, I learned how to test my functions and deploy my website using GitHub Pages. This was my first experience creating a website with multiple pages and making it accessible online.

Testing

I created a separate unit_tests.py file to test several of the helper functions used in my project. These tests use assert_equal to compare the actual results of functions with their expected results.

Some of the functions I tested include:

- money() – Formats numbers as dollar amounts.
- total_expenses() – Calculates the total cost of all materials.
- find_material() – Searches for a material using its unique ID.
- valid_number() – Checks whether a user input can be used as a number.
- navigation() – Creates navigation links for the website.

AI Assistance

I used the AI tool provided in CISC106 as a resource while working on this project. I mainly used it to better understand programming concepts, troubleshoot errors, and figure out how to organize different parts of my website.

The AI was helpful when I needed additional explanations or was having trouble understanding an error. I used its responses to work through problems and improve my understanding of how the code worked.

Conclusion

Overall, this project gave me a better understanding of how Python can be used to create an interactive website. It also helped me become more comfortable working with functions, dataclasses, lists, user inputs, and debugging.

I enjoyed being able to connect computer science with construction engineering and create a website that has a practical purpose. Although I ran into several challenges along the way, working through them helped me develop a better understanding of programming and how different parts of a larger project work together.
