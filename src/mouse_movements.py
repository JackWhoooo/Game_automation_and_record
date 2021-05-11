import keyboard
import mouse


def record() -> None:
    events = []
    mouse.hook(events.append)
    keyboard.wait("esc")
    mouse.unhook(events.append)
    mouse.play(events, include_clicks=True, speed_factor=2.0)


if __name__ == '__main__':
    record()
