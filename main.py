""" Construction Project Budget Tracker - CISC 106 Drafter Final Project"""

"""Track a sinlge construction project's materials and remaining budget."""

from dataclasses import dataclass, field
from drafter import *

#Websites data will appear on Drafter's About page after its run
set_website_title("Construction Project Budget Tracker")
set_site_information(
    author = "Christopher Faith",
    description = "Track construction material expenses against a project budget.",
    sources = "Drafter documentaion and assistance from ChatGPT (see AI transcripts in repository)",
    planning = "See brainstorm/ and design/ folders in GitHub repository.",
    links = ["https://cafaith28.github.io/Project-Budget-Tracker/"],
    )

@dataclass
class Material:
    material_id: int
    name: str
    unit_cost: float
    quantity: float

@dataclass
class State:
    #giving the fields default values in the begining when making a new State
    project_name: str = ""
    budget: float = 0.0
    materials: list[Material] = field(default_factory = list) #new State starts with it's own empty list of materials
    next_id: int = 1
    message: str = ""

#Helper Function 1
def money(amount: float)-> str:
    """Format a number into dollars and cents."""
    return "$" + format(amount, ".2f")

#Helper Function 2
def total_expenses(materials: list[Material])-> float:
    """Adds the total cost of every material (loop)."""
    total = 0.0
    for material in materials:
        material_cost = material.unit_cost * material.quantity
        total = total + material_cost
    return total

#Helper Function 3
def find_material(materials: list[Material], material_id: int)-> Material | None:
    """
    Uses Find Loop to find a material by its unique ID so that repeat names are not a issue.
    Will return None if material ID does not exist.
    """
    for material in materials:
        if material.material_id == material_id:
            return material
    return None

#Helper Function 4
def valid_number(value: str, positive: bool) -> bool:
    """Checks user input to see if it is a valid positive number."""
    value = value.strip()
    if value.replace(".", "", 1).isdigit():
        number = float(value)
        if positive:
            return number > 0
        else:
            return number >= 0
    return False

#Helper Function 5
def navigation() -> list:
    """Creates the links to the different pages."""
    links = []
    
    links.append(Link("Dashboard", "dashboard"))
    links.append(Link("Add Material", "add_material"))
    links.append(Link("Summary", "summary"))
    return links

@route
def index(state: State)-> Page:
    """Displays the homepage where user can create or update their project information. Includes textboxes and buttons"""
    budget_text = ""
    if state.project_name != "":
        budget_text = str(state.budget)
        
    return Page(state, [
        Header("Construction Project Budget Tracker"),
        "Create a construction project and track material costs.",
        Header("Project Setup", 2),
        
        "Project Name:",
        TextBox("project_name", state.project_name),
        
        "Project Budget ($):",
        TextBox("project_budget", budget_text),
        
        Button("Save Project", "save_project"),
        
        state.message
    ])
        
@route
def save_project(state: State, project_name: str, project_budget: str)-> Page:
    """Saves the projects name and budget if both are valid inputs."""
    if project_name.strip() == "":
        state.message = "Please enter a project name."
        return index(state)
    if not valid_number(project_budget, False):
        state.message = "Please enter a valid budget of $0 or more."
        return index(state)
    state.project_name = project_name.strip()
    state.budget = float(project_budget)
    state.message = "Project saved successfully."
    return dashboard(state)

@route
def dashboard(state: State)-> Page:
    """
    Displays the project's budget, total_expenses, and remaining money.
    Checks to see if the project is over or under budget and shows a table of
    all materials with buttons to edit or remove each specific one.
    """
    if state.project_name == "":
        return index(state)
    
    spent = total_expenses(state.materials)
    remaining = state.budget - spent
    
    if spent > state.budget:
        status = "OVER BUDGET by " + money(-remaining)
    elif spent == state.budget:
        status = "EXACTLY ON BUDGET"
    else:
        status = "UNDER BUDGET by " + money(remaining)
        
    contents = [
        Header("Project Dashboard")
        ]
    
    contents.extend(navigation())
    
    contents.append(Header(state.project_name, 2))
    contents.append("Budget: " + money(state.budget))
    contents.append("Total Expenses: " + money(spent))
    contents.append("Remaining Budget: " + money(remaining))
    contents.append("Budget Status: " + status)
    contents.append(state.message)
    
    contents.append(Button("Add New Material", "add_material"))
    contents.append(Button("Edit Project Budget", "index"))
    
    contents.append(Header("Material List", 2))
    
    if len(state.materials) == 0:
        contents.append("No materials have been added yet.")
        
    else:
        rows = []
        
        for material in state.materials:
            material_total = material.unit_cost * material.quantity
            
            edit_button = Button(
                "Edit", "edit_material",
                [Argument("material_id", material.material_id)]
                )
            
            remove_button = Button(
                "Remove", "remove_material",
                [Argument("material_id", material.material_id)]
                )
            
            row = [
                str(material.material_id),
                material.name,
                money(material.unit_cost),
                str(material.quantity),
                money(material_total),
                edit_button,
                remove_button
                ]
            
            rows.append(row)
            
        headings = [
            "ID", "Material", "Unit Cost",
            "Quantity", "Total", "Edit", "Remove"
        ]
            
        contents.append(Table(rows, headings))
    return Page(state, contents)

@route
def add_material(state: State)-> Page:
    """
    Displays a page where the user can enter a new construction material with all its fields,
    ie. name, cost per unit, and quantity.
    """
    
    if state.project_name == "":
        return index(state)
    
    contents = [
        Header("Add Construction Material")
        ]
    
    contents.extend(navigation())
    
    contents.append("Material Name:")
    contents.append(TextBox("material_name"))
    
    contents.append("Cost per Unit ($):")
    contents.append(TextBox("unit_cost"))
    
    contents.append("Quantity:")
    contents.append(TextBox("quantity"))
    
    contents.append(Button("Save Material", "save_material"))
    
    contents.append(state.message)
    
    return Page(state, contents)

@route
def save_material(state: State, material_name: str, unit_cost: str, quantity: str)-> Page:
    """Check the user's material information and add the new material to the project if all inputs are valid."""
    if material_name.strip() == "":
        state.message = "Please enter a material name."
        return add_material(state)
    
    if not valid_number(unit_cost, False):
        state.message = "Please enter a valid cost."
        return add_material(state)
    
    if not valid_number(quantity, True):
        state.message = "Please enter a quantity greater than zero."
        return add_material(state)
    
    name = material_name.strip()
    cost = float(unit_cost)
    amount = float(quantity)
    
    new_material = Material(state.next_id, name, cost, amount)
    
    state.materials.append(new_material)
    state.next_id = state.next_id + 1
    state.message = "Material added successfully!"
    
    return dashboard(state)

@route
def edit_material(state: State, material_id: int)-> Page:
    """Dispalys a page where the suer can edit the name, cost, and quantitiy of an existing material in their project."""
    material = find_material(state.materials, material_id)
    
    if material is None:
        state.message = "Material not found."
        return dashboard(state)
    
    contents = [
        Header("Edit Material")
        ]
    contents.extend(navigation())
    
    contents.append("Material Name:")
    contents.append(TextBox("material_name", material.name))
    
    contents.append("Cost per Unit ($):")
    contents.append(TextBox("unit_cost", str(material.unit_cost)))
    
    contents.append("Quantity:")
    contents.append(TextBox("quantity", str(material.quantity)))
    
    save_button = Button(
        "Save Changes",
        "update_material",
        [Argument("material_id", material.material_id)]
        )
    
    contents.append(save_button)
    contents.append(Button("Cancel", "dashboard"))
    contents.append(state.message)
    
    return Page(state, contents)

@route
def update_material(state: State, material_id: int, material_name: str, unit_cost: str, quantity: str)-> Page:
    """Finds an already existing material and updates all of its fields after checking that the user inputs are all valid."""
    material = find_material(state.materials, material_id)
    
    if material is None:
        state.message = "Material not found."
        return dashboard(state)
    
    if material_name.strip() == "":
        state.message = "Please enter a material name."
        return edit_material(state, material_id)
    
    if not valid_number(unit_cost, False):
        state.message = "Please enter a valid cost."
        return edit_material(state, material_id)
    
    if not valid_number(quantity, True):
        state.message = "Please enter a quantity greater than zero."
        return edit_material(state, material_id)
    
    material.name = material_name.strip()
    material.unit_cost = float(unit_cost)
    material.quantity = float(quantity)
    
    state.message = "Material updated successfully!"
    
    return dashboard(state)

@route
def remove_material(state: State, material_id: int)-> Page:
    """
    Find a material using it's unique ID and then removing it from the projects material list.
    Then it will display a message confirming that the material had been succesfully removed.
    """
    material = find_material(state.materials, material_id)
    
    if material is None:
        state.message = "Material not found."
        return dashboard(state)
    
    state.materials.remove(material)
    state.message = "Material removed successfully!"
    
    return dashboard(state)

@route
def summary(state: State)-> Page:
    """
    Displays the entire summary of the project including it's budget, total expenses, remanining money,
    and number of materials. Also shows if the project went over or under the original budget.
    """
    if state.project_name == "":
        return index(state)
    
    spent = total_expenses(state.materials)
    remaining = state.budget - spent
    number_of_materials = len(state.materials)
    
    if spent > state.budget:
        status = "Over Budget"
    elif spent == state.budget:
        status = "Right on Budget"
    else:
        status = "Under Budget!"
        
    contents = [
        Header("Project Summary")
        ]
    contents.extend(navigation())
    
    contents.append(Header(state.project_name, 2))
    contents.append("Project Budget: " + money(state.budget))
    contents.append("Total Expenses: " + money(spent))
    contents.append("Remaining Budget: " + money(remaining))
    contents.append("Number of Materials: " + str(number_of_materials))
    contents.append("Budget Status: " + status)
    
    contents.append(Button("Return to Dashboard", "dashboard"))
    
    return Page(state, contents)

#Will run our code if python file is being run directly
if __name__ == "__main__":
    start_server(State())
                              
    
