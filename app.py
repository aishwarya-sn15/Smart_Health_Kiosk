import tkinter as tk
from tkinter import ttk, messagebox
from logic import *

# Basic window setup
root = tk.Tk()
root.title("Smart Health Kiosk")
root.geometry("600x600")

# --- Patient Name Input ---
tk.Label(root, text="Enter Patient Name:").pack()
name_entry = tk.Entry(root)
name_entry.pack()

# --- Location Dropdown ---
tk.Label(root, text="Select City:").pack()
location_var = tk.StringVar()
location_dropdown = ttk.Combobox(root, textvariable=location_var)
location_dropdown['values'] = ("Bangalore", "Delhi", "Chennai")
location_dropdown.pack()

# --- Season Dropdown ---
tk.Label(root, text="Select Season:").pack()
season_var = tk.StringVar()
season_dropdown = ttk.Combobox(root, textvariable=season_var)
season_dropdown['values'] = ("Summer", "Monsoon", "Winter")
season_dropdown.pack()

# --- Vitals Entry (HR and SpO2) ---
tk.Label(root, text="Heart Rate (bpm):").pack()
hr_entry = tk.Entry(root)
hr_entry.pack()

tk.Label(root, text="SpO2 (%):").pack()
spo2_entry = tk.Entry(root)
spo2_entry.pack()

# --- Output Area ---
output_text = tk.StringVar()
tk.Label(root, textvariable=output_text, fg="darkgreen", wraplength=500, justify="left").pack(pady=10)

# --- Emergency Button Logic ---
def handle_emergency():
    name = name_entry.get()
    patient_info = get_medical_history(name)
    
    if "Error" in patient_info:
        messagebox.showerror("Error", patient_info["Error"])
        return
    
    hr = hr_entry.get()
    spo2 = spo2_entry.get()
    status = check_vitals(hr, spo2)
    
    msg = f"EMERGENCY ALERT\nPatient: {patient_info['Name']}\nAge: {patient_info['Age']}\nCondition: {patient_info['Condition']}\nVitals: {' | '.join(status)}\nAlert sent to hospital."
    output_text.set(msg)

# --- Health Suggestions Logic ---
def show_suggestions():
    city = location_var.get()
    season = season_var.get()
    suggestions = get_health_suggestions(city, season)
    output_text.set("Suggestions for this season:\n" + "\n".join(suggestions))

# --- Doctor Recommendations Logic ---
def show_doctors():
    city = location_var.get()
    issue = issue_entry.get()
    doctors = get_doctor_recommendations(city, issue)
    output_text.set("Suggested Doctors:\n" + "\n".join(doctors))

# --- Buttons ---
tk.Button(root, text="Emergency", command=handle_emergency, bg="red", fg="white").pack(pady=5)
tk.Button(root, text="Get Seasonal Suggestions", command=show_suggestions).pack(pady=5)

# --- Issue Entry for Doctor Suggestion ---
tk.Label(root, text="Symptom or Health Issue:").pack()
issue_entry = tk.Entry(root)
issue_entry.pack()
tk.Button(root, text="Find Doctor", command=show_doctors).pack(pady=5)

root.mainloop()
