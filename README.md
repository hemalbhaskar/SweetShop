# SweetShop
# 🍬 Sweet Shop Management System (Python CLI App)

This is a simple, clean, and interactive **Sweet Shop Management System** built using **Python**.  
It follows best practices like **modular code**, **meaningful naming**, and **terminal-based UI**.  
The system allows users to manage sweets inventory, search items, and handle purchases — all via the command line.

---

## 🔧 Features

- ✅ **View all sweets** with ID, name, category, price, and quantity
- ➕ **Add new sweets** with proper category and stock
- ❌ **Remove sweets** by ID
- 🔍 **Search sweets** by:
  - Name
  - Category
  - Price range
- 🛒 **Purchase sweets** with stock check and automatic stock reduction
- 🔁 **Restock sweets** by ID
- 📦 **Terminal-friendly output** using clean table formatting

---

## 📂 Project Structure
SweetShop/
├── main.py # Terminal-based user interface
├── src/
│ └── shop.py # All backend logic and inventory functions
├── tests/ (optional)
│ └── test_shop.py # (If using unit testing later)
└── README.md # Project documentation

---
 Tech Stack
🐍 Python 3.x

📟 Terminal / Command-line

VS Code (recommended IDE)

---
## ▶️ How to Run

1. **Clone this repo** or download ZIP  
2. Open terminal in the project folder  
3. Run the app:

```bash
python main.py
🍬 Sweet Shop System
======================
1. Show Menu
2. Add Sweet
3. Remove Sweet by ID
4. Exit
5. Search Sweets
6. Purchase Sweet
7. Restock Sweet

Enter your choice: 1

🧁 Sweet Shop Menu:
┌────┬────────────┬────────────┬────────┬────────────┐
│ ID │ Name       │ Category   │ Price  │ Quantity   │
├────┼────────────┼────────────┼────────┼────────────┤
│ 1  │ Rasgulla   │ Mithai     │ ₹10    │ 20         │
│ 2  │ Ladoo      │ Mithai     │ ₹8     │ 25         │
└────┴────────────┴────────────┴────────┴────────────┘
