from pyscript import document, display, when # 'when' imports the 'when' 

club_members = ["Josh Joshington", "Adam Adam", "Jane John", "Chris Kyle", "Joseph Joestar", "Tom Pearl", "Palm Beach Pete", "Connor McGregor"]

grade_7 = ["Josh Joshington", "Jane John"]
grade_8 = ["Chris Kyle", "Connor McGregor"]
grade_9 = ["Joseph Joestar", "Adam Adam"]
grade_10 = ["Tom Pearl", "Palm Beach Pete"]

celebacy = grade_7 | grade_8 | grade_9 | grade_10


members_list = "<br>".join(sorted(celebacy))

display(len(f'celebacy'))



# the when used to bind function with the event of submitting the form with id 'candidate-form'
@when("submit", "#candidate-form")
# the function that will be called when the form is submitted
def verify_candidate(event):
	event.preventDefault()
	first_name = document.querySelector("#first-name").value.strip()
	last_name = document.querySelector("#last-name").value.strip()
	candidate_name = f"{first_name} {last_name}".strip()
    # check if the candidate's name is in the list of club members
	is_member = candidate_name in club_members
	messages = {
		True: f"Congratulations {candidate_name}! You are now part of the ICT club.",
		False: f"Sorry {candidate_name}, your name is not on the list.",
	}
	document.querySelector("#result").textContent = messages[is_member]

