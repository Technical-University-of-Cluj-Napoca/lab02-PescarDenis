import datetime
import os
def smart_log(*args, **kwargs) -> None :
 
    level = kwargs.get("level", kwargs.get("Level", "info")).lower()
    timestamp = kwargs.get("timestamp", kwargs.get("Timestamp", True))
    date = kwargs.get("date", kwargs.get("Date", False))
    save_to = kwargs.get("save_to", kwargs.get("Save_to", None))
    colored = kwargs.get("colored", kwargs.get("color", True))
    

    colors = {
        "info": "\033[94m",     # Blue
        "debug": "\033[90m",    # Gray
        "warning": "\033[93m",  # Yellow
        "error": "\033[91m",    # Red
        "reset": "\033[0m"
    }

    message = " ".join(str(arg) for arg in args)
    
    prefix_parts = []
    if date:
        prefix_parts.append(datetime.datetime.now().strftime("%Y-%m-%d"))
    if timestamp:
        prefix_parts.append(datetime.datetime.now().strftime("%H:%M:%S"))
    if level:
        prefix_parts.append(f"[{level.upper()}]")
    
    prefix = " ".join(prefix_parts)
    full_message = f"{prefix} {message}" if prefix else message
    
    if colored and level in colors:
        full_message_colored = f"{colors[level]}{full_message}{colors['reset']}"
    else:
        full_message_colored = full_message
    
    print(full_message_colored)

    if save_to:
        try:
            os.makedirs(os.path.dirname(save_to), exist_ok=True)
            with open(save_to, "a", encoding="utf-8") as f:
                f.write(full_message + "\n")
        except Exception as e:
            print(f"\033[91m[ERROR] Could not write to log file: {e}\033[0m")

username = "alice"
smart_log("System started successfully.", Level="info")
smart_log("User", username, "logged in", Level="debug", timestamp=True)
smart_log("Low disk space detected!", level="warning", save_to="logs/system.log")
smart_log("Model", "training", "failed!", level="error", color=True, save_to="logs/errors.log") 
smart_log("Process end", Level="info", color=False, save_to="logs/errors.log")