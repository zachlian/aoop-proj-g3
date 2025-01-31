# PvZ Duel
![image](https://github.com/user-attachments/assets/1be69c1b-ebea-47ec-a5d8-aa965b0edd2c)

PvZ Duel is a two-player game where one controls plants, and the other leads zombies.
Developed with Pygame, inspired by the classic "Plants vs. Zombies".

## 🎮 Game Features

- Single Player Mode: Play as plants defending against zombie waves
- Multiplayer Mode: Choose to play as either plants or zombies
- Resource Management: Collect sunlight for plants, accumulate brains for zombies
- Diverse Units:
  - Plants: Sunflower, Peashooter, Wallnut, Squash
  - Zombies: Basic Zombie, Cone-head Zombie, Bucket-head Zombie, Tombstone

## 🛠️ Requirements

- Python 3.10+
- Pygame 2.6.0

## 📥 Installation

1. Clone the repository:
```
bash
git clone https://github.com/zachlian/aoop-proj-g3.git
cd aoop-proj-g3
```

2. Install dependencies:
```
bash
pip install -r requirements.txt
```

3. Run the game:
```
bash
cd src
python src/main.py
```
## 🎯 Controls

### Single Player Mode
- Left Mouse Button: Select and place plants
- Click on sunlight: Collect sun resources

### Multiplayer Mode
Plants:
- Left Mouse Button: Select and place plants
- Click on sunlight: Collect sun resources

Zombies:
- W/S/A/D: Select grid cell
- 1-4: Place zombie type 1-4

## 🏗️ Project Structure
```
src/
├── config/ # Game configurations
├── core/ # Core game logic
├── models/ # Game object models
├── ui/ # User interface
└── main.py # Game entry point
```

## 🎲 Game Mechanics

### Resource System
- Plants: Collect sunlight from Sunflowers and falling sun
- Zombies: Automatically accumulate brain points over time

### Unit Characteristics

Plants:
- Sunflower: Produces sun resources
- Peashooter: Ranged attacker
- Wallnut: High HP defender
- Squash: High melee damage

Zombies:
- Basic Zombie: Standard unit
- Cone-head Zombie: Enhanced HP
- Bucket-head Zombie: High HP
- Tombstone: Stationary defense structure

### Combat System
- Plants attack zombies with projectiles or direct contact
- Zombies move forward and damage plants on contact
- Each unit has unique health points and attack damage

## 📜 License

This project is licensed under the MIT License
