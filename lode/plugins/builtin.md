# Built-in Plugins

## Overview

Stagehand includes several built-in plugins in `src/stagehand/plugins/`:

| Plugin | Triggers | Actions | Extensions |
|--------|----------|---------|------------|
| keyboard | KeyboardTrigger | KeyboardAction | KeyboardExtension, MouseExtension |
| joystick | JoystickTrigger | - | JoystickExtension |
| devices/stomp4 | Stomp4Trigger | - | - |
| devices/stomp5 | Stomp5Trigger | - | - |
| devices/click4 | Click4Trigger | - | - |
| devices/rocker | RockerTrigger | - | - |
| obs_core | - | Various | OBS extensions |
| microphone_voter | - | - | Microphone voter |
| web_server | - | - | WebServerExtension |
| shell | - | ShellAction | - |
| cyber | - | CyberAction | - |
| window_filter | WindowFilter | - | - |

## Plugin: keyboard

**Purpose**: Simulate keyboard and mouse input.

### Components

```python
# Trigger: KeyboardTrigger
# Listens for keyboard shortcuts

# Action: KeyboardAction  
# Simulates keyboard key presses/releases

# Extension: KeyboardExtension
keyboard.press('ctrl+a')
keyboard.release('ctrl+a')
keyboard.type('Hello World')

# Extension: MouseExtension
mouse.move(100, 200)
mouse.click('left')
mouse.scroll('down')
```

## Plugin: joystick

**Purpose**: Handle game controller input.

### Components

```python
# Trigger: JoystickTrigger
# Activates on joystick button press

# Extension: JoystickExtension
# Available in sandbox
joystick.get_state()
joystick.get_axis(0)
```

## Plugin: obs_core

**Purpose**: Control OBS Studio via websocket.

### Capabilities

- Scene switching
- Source visibility
- Recording control
- Streaming control
- Source settings
- Text source updates

### Sandbox Extensions

```python
obs.set_current_scene('Game')
obs.set_source_visibility('Webcam', True)
obs.start_streaming()
obs.set_text('Title', 'Playing: Minecraft')
```

## Plugin: devices

**Purpose**: Support for physical input devices.

### Stomp4 (4-pedal controller)

```python
# Trigger: Stomp4Trigger
# Activates when pedal pressed

# Each pedal maps to different action
```

### Stomp5 (5-pedal controller)

Similar to Stomp4 with 5 pedals.

### Click4 (4-switch controller)

```python
# Trigger: Click4Trigger
# Activates on switch press
```

## Plugin: microphone_voter

**Purpose**: Automatically switch active microphone based on volume.

### How It Works

1. Monitors all microphones continuously
2. Calculates current volume level
3. Mutes all mics except loudest
4. Unmutes the currently active mic

### Use Case

Streamers with multiple microphones at different positions (desk, workbench, headset) - automatically uses whichever is picking up sound.

## Plugin: web_server

**Purpose**: HTTP API for remote control.

### Extension

```python
# In sandbox:
web_server.route('/api/custom', custom_handler)
web_server.start(port=8080)
```

## Plugin: shell

**Purpose**: Execute shell commands.

### Action: ShellAction

```python
# Configure command to run
# e.g., "notify-send 'Alert' 'Message'"
```

## Plugin: cyber

**Purpose**: Execute Cyberlang scripts.

**Note**: Cyberlang is a custom scripting language for shortcuts/macros.