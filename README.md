# 🧩 IST105 Assignment 5 — Interactive Treasure Hunt

**Author**: Gustavo Iserte Bonfim  
**Course**: IST105 - Introduction to Programming  
**Assignment**: #5 — CI/CD Pipeline with Django, GitHub, and AWS Auto Scaling

---

## 📦 Project Structure

- **Project Name**: `assignment5`  
- **App Name**: `puzzle`  
- **Form**: `PuzzleForm` with two fields:
  - `number`: Integer input  
  - `text`: Text input (max 100 characters)

---

## 🧠 App Logic

After submitting the form, the app performs:

### 🔢 Number Puzzle
- Checks if the number is even or odd.
- If even → calculates square root.
- If odd → calculates cube.

### 🔤 Text Puzzle
- Converts text to binary.
- Counts the number of vowels.

### 🪙 Treasure Hunt
- Simulates guessing a random number between 1–100.
- If guessed in ≤ 5 attempts → user wins!

---

## 🗂️ GitHub Branches

- `main`: Final version  
- `development`: Integration testing  
- `feature1`: Initial development

---

## 🛠️ Technologies Used

- Python 3.11  
- Django 4.x  
- AWS EC2, Auto Scaling, Load Balancer  
- Git & GitHub

---

## 📄 License

This project is for educational purposes under IST105.  
© 2025 Gustavo Iserte Bonfim