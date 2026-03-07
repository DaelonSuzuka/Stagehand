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
| generic | - | HttpAction | HttpExtension, SocketsExtension |

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

## Plugin: generic

**Purpose**: Utility extensions for sandbox scripts.

### HttpExtension

**Purpose**: Make HTTP requests from sandbox scripts using httpx.

```python
# Available in sandbox as: http

# Simple GET request
response = http.get('https://api.example.com/data')
print(response.text)

# POST with JSON body
response = http.post('https://api.example.com/users', 
    json={'name': 'Alice', 'email': 'alice@example.com'})

# With headers
response = http.get('https://api.example.com/protected',
    headers={'Authorization': 'Bearer token123'})

# Access response
data = response.json()
status = response.status_code

# All HTTP methods
http.get(url, **kwargs)
http.post(url, **kwargs)
http.put(url, **kwargs)
http.patch(url, **kwargs)
http.delete(url, **kwargs)
```

### HttpAction

**File**: `plugins/generic/http_action.py`

**Purpose**: Make HTTP requests from action triggers (UI).

**Status Bar**: Shows "HTTP:8080" when server is running, "HTTP: Off" when stopped.

### HttpTrigger

**File**: `plugins/generic/http_trigger.py`

**Purpose**: Trigger actions when HTTP requests are received.

**How it works**:
1. Start the HTTP server from status bar or settings page
2. Create an action with HTTP trigger
3. Set method filter (ANY, GET, POST, etc.) and optional path filter
4. External requests to `http://localhost:PORT/path` trigger the action

**UI**: Status bar shows "HTTP:8080" when running. Right-click to start/stop or open settings.

**Settings** (in status bar context menu):
- Start/Stop HTTP server
- Configure port (default 8080)

**Settings Page**: "HTTP Server Settings" singleton page with:
- Port configuration
- Start/Stop buttons
- Status display
- Test endpoint info

**Usage in Actions**:
1. Create new action
2. Select "http" from trigger dropdown
3. Choose method filter: ANY, GET, POST, PUT, PATCH, DELETE
4. Set path filter (e.g., "/webhook") or leave empty for all paths
5. Configure action output

**Example**: Webhook trigger
- Method: POST
- Path: /webhook
- External service sends POST to `http://localhost:8080/webhook`
- Action fires, runs configured output

### SocketsExtension

**Purpose**: Raw socket utilities (currently stub).

### HttpAction

**File**: `plugins/generic/http_action.py`

**Purpose**: Make HTTP requests from action triggers.

**UI Components**:
- Method dropdown (GET, POST, PUT, PATCH, DELETE)
- URL input field
- JSON body editor (shown for POST/PUT/PATCH)
- Edit button for multiline editor

**Usage in UI**:
1. Create new action
2. Select "http" from action dropdown
3. Choose HTTP method
4. Enter URL
5. For POST/PUT/PATCH, enter JSON body
6. Click run or set up trigger

**Sandbox Example with http extension**:
```python
# Direct sandbox usage
response = http.get('https://api.example.com/data')
data = response.json()

# Using HttpAction (from UI trigger)
# Method: POST
# URL: https://api.example.com/users
# Body: {"name": "Alice"}
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