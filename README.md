Digitalization of the Hospitality Process for Group Accommodation

Overview
This document provides a comprehensive overview of the web application designed
to digitalize the hospitality process for group accommodation. The application 
facilitates room allocation for groups in hostels, ensuring efficient and logical 
placement based on group and hostel information provided through CSV files.

Objective
The primary objective is to create a web application that allows users to upload
CSV files containing group and hostel information and efficiently allocate rooms 
while adhering to group, capacity, and gender-specific requirements.

Installation:-

1. *Clone the Repository*:
   git clone https://github.com/yourusername/hospitality-process-digitalization.git
   cd hospitality-process-digitalization
   

2. *Install Dependencies*:
   Ensure you have Python installed. Then, install the necessary Python packages using pip:
    pip install -r requirements.txt
   

3. *Run the Application*:
   Start the Flask application by running:
   \\\`
   python app.py
   \\\`

4. *Access the Application*:
   Open your web browser and navigate to \http://127.0.0.1:5000/\.



Steps to run the application:-
1. Upload CSV Files:
   - Open the application in your web browser.
   - Use the provided form to upload the Group Information CSV and the Hostel Information CSV files.
   - Click the \"Upload\" button to submit the files.

2. View Room Allocation:
   - After processing, the application will display the room allocation results on the same page.
   - The results show which group members are allocated to which rooms in the hostels.

3. Download Allocation Details:
   - A link to download the allocation details as a CSV file is provided below the results table.

#File Descriptions
- *index.html*: Main HTML template for the web application.
- *styles.css*: Contains the CSS styles for the web application.
- *app.py*: Main Flask application file.
- *requirements.txt*: Lists the Python dependencies required to run the application.

Logic:-
The web application is designed to efficiently allocate rooms in hostels based on group and hostel information provided in CSV files. Here's a detailed explanation of the logic used:

1. File Upload Handling
   - The application accepts two CSV files: one for group information and one for hostel information.
   - The files are parsed and converted into pandas DataFrames for easy manipulation and processing.

2. Data Validation
   - Validate the structure and content of the CSV files to ensure they contain the necessary columns and correct data types.
   - Ensure group and hostel information are formatted correctly and contain valid data.

3. Room Allocation Algorithm
   - The core of the application is the room allocation algorithm, which follows these steps:
	Step 1: Sort Data
	- Groups: Sort groups by the number of members in descending order to allocate larger groups first, ensuring optimal use of room capacity.
	- Hostels: Sort hostels by room capacity in descending order to allocate larger rooms first.
	
	Step 2: Initialize Allocation Data Structures
	- Prepare lists or dictionaries to track allocated rooms and remaining capacities.
	
	Step 3: Group Allocation
	- Iterate through each group and attempt to allocate them to a suitable room based on the following criteria:
	- Gender Compatibility: Ensure the group and the room's gender requirements match.
	- Capacity Check: Ensure the room has enough capacity to accommodate the entire group.
	- Partial Allocation: If a group cannot be accommodated in a single room, split the group across multiple rooms in the same hostel while maintaining gender and capacity requirements.
	
	Step 4: Record Allocations
	- Track the allocations by recording the group ID, hostel name, room number, and number of members allocated to each room.

4. Output Generation
	- Compile the allocation results into a structured DataFrame.
	- Provide an option to download the results as a CSV file, which includes the allocation details. 

Conclusion:-
This web application provides a streamlined process for allocating rooms to groups
in hostels, ensuring that group members stay together, gender requirements are 
met, and room capacities are not exceeded. The user-friendly interface and 
downloadable output make it an efficient tool for digitalizing the hospitality 
process for group accommodations.