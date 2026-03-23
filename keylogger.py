from pynput import keyboard

text = ""

def on_press(key):
    global text

    if key == keyboard.Key.enter:
        text += "\n"
    elif key == keyboard.Key.tab:
        text += "\t"
    elif key == keyboard.Key.space:
        text += " "
    elif key == keyboard.Key.shift:
        pass
    elif key == keyboard.Key.backspace:
        if len(text) > 0:
            text = text[0:-1]
    elif key == keyboard.Key.esc:
        print("\n--- Final Captured Text ---")
        print(text)
        return False
    elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
        pass
    else:

        text += str(key).strip("'")

# Start the listener
with keyboard.Listener(on_press=on_press) as listener:
    print("Listening... Press ESC to stop and view captured text.")
    listener.join()