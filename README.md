**Real-Time Automated Person Detection and Alert System** 
📌 **Overview**  
This project is designed to assist law enforcement agencies in identifying missing and wanted persons using real-time CCTV surveillance and AI-based facial recognition. The system automates person detection and sends instant alerts to nearby police stations when a match is found.  

🛠️ Features  
✅ Admin Panel (Django) – Police officers can upload photos and details of missing/wanted persons.  
✅ YOLOv8 for Face Detection – Detects faces from live CCTV footage.  
✅ DeepFace for Face Recognition – Matches detected faces with stored records.  
✅ Automated Alerts – Sends email notifications with **location, time, and person details** to the nearest police station.  
✅ Scalable & Real-Time – Works efficiently with multiple CCTV cameras.  

🖥️ Technologies Used  
- Backend: Django  
- Frontend: HTML, CSS  
- Face Detection: YOLOv8  
- Face Recognition: DeepFace  
- Database: SQLite  
- Notification System: Email API  

🚀 How It Works  
1. Admin Panel – Police add photos & details of wanted/missing persons.  
2. CCTV Integration – System runs on CCTV live feed.  
3. Detection & Recognition – Uses YOLOv8 for detecting faces and **DeepFace** for recognition.  
4. Alert System – If a match is found, an email notification is sent to the nearest police station.  

📸 Screenshots  
    ![Screenshot (464)](https://github.com/user-attachments/assets/b0abb4f0-299b-446e-9b20-8a16bdfa3615)
    ![Screenshot (465)](https://github.com/user-attachments/assets/3fb92fcf-d913-4cf9-a129-dc6ec69c497b)

⚙️ Setup & Installation  
1. Clone the Repository 
   git clone https://github.com/dasviolina001/Real-Time-Automated-Person-Detection-And-Alert-System.git
   cd Real-Time-Automated-Person-Detection-And-Alert-System
   
2. Create & Activate Virtual Environment  
   python -m venv venv
   source venv/bin/activate  # For Linux/macOS
   venv\Scripts\activate  # For Windows
   
3. Install Dependencies  
   pip install -r requirements.txt
   
4. Run Django Server  
   python manage.py runserver
   
5. Access Admin Panel  
   Open `http://127.0.0.1:8000/admin/` in your browser.  

📧 Contact & Contribution 
Want to improve this project? Feel free to fork, clone, and submit a pull request! 🚀  
