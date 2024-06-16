# Conway's Game of Life

## Overview

This project is an implementation of Conway's Game of Life, a cellular automaton devised by the mathematician John Horton Conway. The game consists of a grid of cells, each of which can be alive or dead. The state of the grid evolves over discrete time steps according to a set of simple rules.

## Features

- **Interactive Grid**: Easily click to toggle the state of individual cells.
- **Load Structures**: Load and position well-known structures like the Glider, Glider Gun, and more.
- **Control Simulation**:
  - **Start/Pause**: Start or pause the simulation at any time.
  - **Step-by-Step**: Advance the simulation frame by frame while in pause mode.
- **Customizable Grid Size**: Adjust the size of the grid to your preference.
- **Speed Control**: Adjust the speed of the simulation.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/HamzaMPSY/conway.git
   ```
2. Navigate to the project directory:
   ```bash
   cd conway
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```bash
   python main.py
   ```
2. Use the interactive grid to set up your initial configuration.
3. Use the control buttons to start, pause, and step through the simulation.

## How to Load and Position Structures

1. **Select Structure**: From the menu, select the structure you want to add (e.g., Glider, Glider Gun).
2. **Position Structure**: Click on the grid where you want to place the selected structure.
3. **Adjust as Needed**: Move or remove structures by selecting and clicking on the grid.

## Rules of the Game

The evolution of the grid follows these simple rules:

1. Any live cell with fewer than two live neighbors dies (underpopulation).
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies (overpopulation).
4. Any dead cell with exactly three live neighbors becomes a live cell (reproduction).

# TBD

- [] Add full screen mode and re-draw the new grid aka new tile sizes
- [] Add back button and shortcut is ESC
- [] Add bottom menu in game features (Pause/ play buttons, step-by-step while in pause mode)
- [] Add load structures menu (structure will be added after choosing its position using arrow keys)

## Contributing

We welcome contributions! Please read our [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to get involved.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Inspired by John Horton Conway's work on cellular automata.
- Thanks to all contributors and the open-source community for their support.

---

Feel free to customize this README to better fit your project specifics.
