# 🏠 Smart Home Management System

## 📌 Overview
The **Smart Home Management System** is a Python-based program that helps manage smart home devices, users, and rooms efficiently. It provides a structured approach to controlling energy consumption, device status, and user roles.

---

## 🚀 Features
- ⚡ **Device Management**: Track power consumption and toggle device status.
- 🏠 **Room Management**: Assign devices to specific rooms.
- 👤 **User Roles**: Supports **Admin** (manages rooms and devices) and **Guest** (view-only access).
- 🔋 **Energy Efficiency Tracking**: Determines device efficiency levels based on power consumption.
- 💡 **Smart Devices**:
  - **Smart Lights**: Adjustable brightness settings.
  - **Smart Thermostat**: Temperature control and efficiency ratings.

---

## 🛠 Technologies Used
This project highlights fundamental **Python** concepts such as:
- **Object-Oriented Programming (OOP)**: Utilizes multiple classes (`Device`, `User`, `Room`, `Admin`, `Guest`).
- **Class Inheritance**: `EnergyEfficientDevice` inherits from `Device` to extend functionality.
- **Encapsulation & Properties**: Manages device power status securely.
- **Static & Class Methods**: Used for power safety checks and room limits.
- **Error Handling**: Ensures valid user roles, device statuses, and power thresholds.

---

## 🔹 How to Use
1️⃣ **Clone the Repository**:
   ```bash
   git clone https://github.com/dodginfeds/smart-home-manager.git
   cd smart-home-manager
   ```
2️⃣ **Run the Application**:
   ```bash
   python smart_home_manager.py
   ```

---

## 📌 Example Usage
```python
# Creating a new Smart Light
kitchen_light = SmartLight("Kitchen Lights", "on", 90, 90, 100)
print(kitchen_light.adjust_brightness(80))
```
🔹 **Output:**
```
Brightness level set to 80.
```

```python
# Managing users
admin1 = Admin("Nazir", "Admin", "Living Room")
print(admin1.display_info())
```
🔹 **Output:**
```
Name: Nazir | Role: Admin
```

---

## 🔮 Future Enhancements
- 📱 **Mobile App Interface**: Extend functionality to a smartphone app.
- 🌎 **IoT Integration**: Connect with actual smart home devices.
- 📊 **Energy Consumption Reports**: Detailed analytics on device usage.
- 🎙 **Voice Control**: Add voice command support using AI assistants.



For any inquiries, feel free to reach out via [GitHub](https://github.com/dodginfeds).
