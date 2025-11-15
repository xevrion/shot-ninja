# Shot Ninja

A lightweight, cross-platform screenshot utility that captures your screen with a simple keyboard shortcut. Perfect for quickly saving screenshots during lectures, meetings, or any screen recording session.

## Features

- **Quick Screenshot Capture**: Press `Shift + S` to instantly capture your screen
- **Cross-Platform**: Works on both Windows and Linux
- **Automatic Naming**: Screenshots are automatically named with timestamps
- **Flexible Keyboard Support**: Adapts to your system's capabilities (uses `keyboard` or `pynput` library)
- **Root-Free Linux Support**: Works on Linux without requiring root access (using pynput)

## Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/shot-ninja.git
cd shot-ninja
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Quick Start

Run the application:
```bash
python main.py
```

On Linux, if using the `keyboard` library (requires root):
```bash
./run.sh
```

### Keyboard Shortcuts

- **Take Screenshot**: `Shift + S`
- **Exit Application**:
  - With keyboard library: `Esc + B`
  - With pynput library: `Esc`

### First Run

On first run, you'll be prompted to select your operating system:
1. Windows
2. Linux

The application will use the appropriate default save path based on your selection. You can modify the save paths in `main.py` to match your preferences.

## Configuration

To change the default save path, edit the `get_save_path()` function in `main.py`:

```python
def get_save_path():
    # Modify these paths to your preference
    if choice == "1":
        save_path = r"D:\Your\Custom\Path"  # Windows
    elif choice == "2":
        save_path = "/your/custom/path"      # Linux
```

## Dependencies

- **mss**: Multi-platform screenshot library
- **keyboard**: Keyboard event handling (Windows/Linux with root)
- **pynput**: Alternative keyboard library (Linux without root)

See `requirements.txt` for specific versions.

## Platform-Specific Notes

### Windows
- Works out of the box with the `keyboard` library
- No special permissions required

### Linux
- The `keyboard` library requires root access
- Use `pynput` for non-root operation (automatically detected)
- Run `./run.sh` if you want to use the `keyboard` library with sudo

## File Naming Convention

Screenshots are saved with the following format:
```
Screenshot YYYY-MM-DD HHMMSS.png
```

Example: `Screenshot 2025-11-15 143052.png`

## Troubleshooting

### "keyboard module requires root on Linux"
This is expected. The application will automatically fall back to using `pynput`. Alternatively, run with `./run.sh` to use sudo.

### "No keyboard library available"
Install pynput:
```bash
pip install pynput
```

### Screenshots not saving
Check that the save directory exists and you have write permissions. The application creates the directory if it doesn't exist.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with [mss](https://github.com/BoboTiG/python-mss) for cross-platform screenshot capability
- Uses [keyboard](https://github.com/boppreh/keyboard) and [pynput](https://github.com/moses-palmer/pynput) for hotkey support

## Author

Made with ⚡ by [Your Name]
