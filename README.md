# Smart Health Kiosk – Intel Unnati Project 2025
This project is a simulation of a Smart Health Kiosk system, developed under the Intel Unnati CoE initiative. The aim is to design a basic healthcare support system that provides emergency handling and localized health suggestions using simple data processing in Python.
---
## Team Members
- **Aishwarya Shanmukh** – 4SO21EC034  
- **Deekshitha P** – 4SO21EC037  
- **Gandla Rupasree** – 4SO21EC045  
**Mentor:** Prof. Sitaram V Yaji
---
## Objective
The purpose of this project is to develop a simple health kiosk simulation that:
- Assists users during medical emergencies
- Suggests health products based on location and season
- Simulates basic wearable sensor data for vitals
- Recommends doctors and tablets based on user symptoms
---
## Features Implemented
1. **Emergency Call Simulation**  
   - Accepts patient name and shows basic medical history  
   - Simulates sending details to the nearest hospital
2. **Location-Based Response**  
   - User selects their city (e.g., Bangalore, Delhi, Chennai)  
   - The system assumes alerting nearby medical services
3. **Pre-Arrival Hospital Alert**  
   - Shares simulated vital data (heart rate and SpO2)  
   - Message is shown that data has been sent in advance
4. **Hyper-Localized Suggestions**  
   - Suggests common medicines/products based on region and season  
   - Uses a CSV file for reference rules
5. **Simulated Wearable Input**  
   - Accepts manual input of heart rate and oxygen level  
   - Detects abnormal values and raises alerts
6. **Doctor and Medicine Recommendation**  
   - Based on symptom entered by the user  
   - Shows doctors and tablet suggestions from a local CSV
---
## Files in the Project
- `app.py` – GUI file (main application)
- `logic.py` – Contains backend logic
- `rules.csv` – Mapping of location + season to suggestions
- `medical_history.csv` – Simulated patient database
- `doctors.csv` – List of doctors with specialties and cities
- `README.md` – Project documentation
---
## Requirements
- Python 3.x  
- `pandas` library  
To install pandas:
```bash
pip install pandas
