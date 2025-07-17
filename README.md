# 🐢 Turtle Crossing Game (Python)

A fun **Frogger-style arcade game** built with **Python** using the `turtle` graphics module. Guide the turtle across the road while avoiding cars — the speed increases with each level!

---

## 🎮 Gameplay

- Use the **Up arrow key** to move the turtle forward.
- Dodge the cars moving across the screen.
- If you reach the top, you advance to the next level.
- The game gets faster and harder with each level!
- If a car hits the turtle: **Game Over**.

---

## 🚀 Getting Started

### ✅ Requirements

- Python 3.x  
- `turtle` module (comes with standard Python)

### ▶️ Run the Game

1. Clone the repository:

   git clone https://github.com/RamyGarici/TurtleCrossing_python.git
   cd TurtleCrossing_python
Run the main Python file:

python main.py
Use your keyboard arrow keys to play.

📁 Project Structure
File	Description
main.py	Main game loop
player.py	Manages the turtle character
car_manager.py	Controls car creation and movement
scoreboard.py	Displays the current level and game over message

✨ Features
Object-oriented code (modular and readable)

Increasing difficulty (car speed increases each level)

Game over detection

Score tracking (current level shown)

🧠 How It Works
The player controls a turtle that moves upward.

Cars are generated randomly and move horizontally across the screen.

Each time the player crosses the screen successfully, the level increases and cars move faster.

Collision detection ends the game if a car hits the turtle.




Add multiple lives

Save high scores

👨‍💻 Author
Ramy Garici
GitHub: @RamyGarici
