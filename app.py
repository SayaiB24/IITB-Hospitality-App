from flask import Flask, request, render_template, redirect, url_for, send_from_directory, make_response # type: ignore
import os
import pandas as pd # type: ignore
import csv
from io import StringIO

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_files():
    if 'group_file' not in request.files or 'hostel_file' not in request.files:
        return redirect(request.url)
    
    group_file = request.files['group_file']
    hostel_file = request.files['hostel_file']

    if group_file.filename == '' or hostel_file.filename == '':
        return redirect(request.url)

    group_file_path = os.path.join(app.config['UPLOAD_FOLDER'], group_file.filename)
    hostel_file_path = os.path.join(app.config['UPLOAD_FOLDER'], hostel_file.filename)
    
    group_file.save(group_file_path)
    hostel_file.save(hostel_file_path)

    group_df = pd.read_csv(group_file_path)
    hostel_df = pd.read_csv(hostel_file_path)

    allocation = allocate_rooms(group_df, hostel_df)

    # Save the allocation to a CSV file
    output_csv = generate_csv(allocation)
    
    # Provide a download link
    response = make_response(output_csv.getvalue())
    response.headers["Content-Disposition"] = "attachment; filename=room_allocation.csv"
    response.headers["Content-Type"] = "text/csv"

    return response

def allocate_rooms(group_df, hostel_df):
    allocation = []

    boys_groups = group_df[group_df['Gender'].str.contains('Boys')]
    girls_groups = group_df[group_df['Gender'].str.contains('Girls')]

    boys_hostels = hostel_df[hostel_df['Gender'] == 'Boys']
    girls_hostels = hostel_df[hostel_df['Gender'] == 'Girls']

    allocation.extend(allocate_gender_rooms(boys_groups, boys_hostels, 'Boys'))
    allocation.extend(allocate_gender_rooms(girls_groups, girls_hostels, 'Girls'))

    return allocation

def allocate_gender_rooms(groups, hostels, gender):
    allocation = []

    for _, group in groups.iterrows():
        members = group['Members']
        group_id = group['Group ID']
        
        suitable_rooms = hostels[hostels['Capacity'] >= members]

        if not suitable_rooms.empty:
            room = suitable_rooms.iloc[0]
            hostels = hostels.drop(room.name)
            
            allocation.append({
                'Group ID': group_id,
                'Hostel Name': room['Hostel Name'],
                'Room Number': room['Room Number'],
                'Members Allocated': members
            })

    return allocation

def generate_csv(allocation):
    output = StringIO()
    writer = csv.DictWriter(output, fieldnames=['Group ID', 'Hostel Name', 'Room Number', 'Members Allocated'])
    writer.writeheader()
    writer.writerows(allocation)
    output.seek(0)
    return output

if __name__ == '__main__':
    app.run(debug=True)
