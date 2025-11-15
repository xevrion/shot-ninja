import os
import datetime
import mss
import mss.tools

# Try importing keyboard, but handle Linux without root
try:
    import keyboard
    KEYBOARD_AVAILABLE = True
except ImportError:
    KEYBOARD_AVAILABLE = False
    print("⚠️  keyboard module not installed")
except Exception:
    KEYBOARD_AVAILABLE = False
    print("⚠️  keyboard module requires root on Linux. Using alternative method.")

# For Linux without root, use pynput instead
if not KEYBOARD_AVAILABLE:
    try:
        from pynput import keyboard as pynput_keyboard
        PYNPUT_AVAILABLE = True
    except ImportError:
        PYNPUT_AVAILABLE = False
        print("⚠️  pynput not installed. Install with: pip install pynput")


def get_save_path():
    """Prompt user for OS and return appropriate save path."""
    print("🖥️  Select your operating system:")
    print("1. Windows")
    print("2. Linux")

    while True:
        choice = input("\nEnter your choice (1 or 2): ").strip()

        if choice == "1":
            # Windows path
            save_path = r"D:\IITJ\Study Sem 3\SNS\neso notes"
            print(f"✅ Using Windows path: {save_path}")
            return save_path, "windows"
        elif choice == "2":
            # Linux path - same structure as Windows
            save_path = "/media/xevrion/DDrive/IITJ/Study Sem 3/SNS/neso notes"
            print(f"✅ Using Linux path: {save_path}")
            return save_path, "linux"
        else:
            print("❌ Invalid choice. Please enter 1 or 2.")


SAVE_PATH, OS_TYPE = get_save_path()
os.makedirs(SAVE_PATH, exist_ok=True)


def take_screenshot():

    now = datetime.datetime.now()
    filename = f"Screenshot {now.strftime('%Y-%m-%d %H%M%S')}.png"
    filepath = os.path.join(SAVE_PATH, filename)

    with mss.mss() as sct:
        monitor = sct.monitors[1]
        sct_img = sct.grab(monitor)
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=filepath)

    print(f"✅ Saved: {filepath}")


if __name__ == "__main__":
    if KEYBOARD_AVAILABLE:
        # Use keyboard module (works on Windows and Linux with root)
        print("🎹 Press SHIFT + S to take a screenshot. Press ESC + B to quit.")
        keyboard.add_hotkey("shift+s", take_screenshot)
        keyboard.wait("esc+b")
    elif PYNPUT_AVAILABLE:
        # Use pynput for Linux without root
        print("🎹 Press SHIFT + S to take a screenshot. Press ESC to quit.")

        current_keys = set()

        should_exit = [False]

        def on_press(key):
            try:
                current_keys.add(key)
            except:
                current_keys.add(key.char if hasattr(key, 'char') else key)

            # Check for Shift + S
            if (pynput_keyboard.Key.shift in current_keys or
                pynput_keyboard.Key.shift_r in current_keys) and \
               pynput_keyboard.KeyCode.from_char('s') in current_keys:
                take_screenshot()

            # Check for ESC to quit
            if key == pynput_keyboard.Key.esc:
                print("\n👋 Exiting...")
                should_exit[0] = True

        def on_release(key):
            try:
                current_keys.discard(key)
            except:
                current_keys.discard(key.char if hasattr(key, 'char') else key)

            if should_exit[0]:
                return False

        with pynput_keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()
    else:
        print("❌ No keyboard library available. Please install pynput: pip install pynput")
