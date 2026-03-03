📂 Folder Watcher Automation (PA-6)

A Python automation project that automatically:

- Monitors a folder
- Detects new CSV files
- Cleans the data
- Saves the cleaned output automatically

This project simulates a real-world automation system used in data processing workflows.

---

🚀 How It Works

1. The program continuously watches a specific folder.
2. When a new CSV file is added:
   - It automatically detects the file.
   - Cleans invalid or missing data.
   - Saves the cleaned file into an output folder.
3. The system keeps running until manually stopped.

---

🛠 Technologies Used

- Python
- Pandas (for data cleaning)
- Watchdog (for folder monitoring)

---

📁 Project Structure

PA-6-Folder-Watcher/
│
├── main.py
├── cleaner.py
├── config.py
├── sample_data/
│     └── dirty_data.csv
│
├── watch_folder/
└── output_folder/

---

📊 Data Cleaning Rules

The system performs the following cleaning steps:

- Removes rows with missing email values
- Keeps only phone numbers with exactly 10 digits
- Keeps only emails that contain "@"

---

⚙️ Installation

Install required libraries:

pip install pandas watchdog

---

▶️ How To Run

1. Run the main script:

python main.py

2. Copy a CSV file into the "watch_folder".

3. The cleaned file will automatically appear in "output_folder".

---

🧠 Learning Outcome

This project demonstrates:

- Real-time folder monitoring
- Automation workflow design
- File handling in Python
- Basic data validation and cleaning

---

📌 Author

Prateek Gupta
Aspiring Python Developer | Automation & Data Projects