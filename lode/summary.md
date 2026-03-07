# Stagehand Summary

Stagehand is a Python/Qt desktop automation tool for streamers and content creators. It provides an event-driven action system where users configure triggers (keyboard, joystick, device inputs), filters (conditional logic), and outputs (actions) without writing code. The application connects to OBS via websocket, manages microphones, handles physical input devices (pedals, switches), and allows Python script execution in a sandboxed environment.

**Core Architecture**: PySide6-based GUI application using the qtstrap framework. Actions are user-defined workflows combining a trigger, optional filters, and an output. Plugins extend functionality by registering new trigger/filter/action types. The sandbox provides a constrained Python execution environment with persistence (`save()`/`load()`) and extension points.

**Key Technology Stack**: Python 3.10+, PySide6, obs-websocket-py, pygame-ce, pynput, cython, numpy, sounddevice.

**Workspace Dependencies** (tightly integrated custom packages):
- **qtstrap** (v0.7.1): Qt framework providing BaseApplication, layout context managers, persistent widgets, and theme system
- **codex-engine-pyqt** (v0.3.1): Serial device auto-discovery and management via DeviceManager
- **monaco-qt** (v0.2.0): Monaco code editor embedded in Qt for sandbox script editing

**Entry Point**: `stagehand.__main__:main()` creates the Application singleton and MainWindow, which initializes all plugins, the Sandbox, and loads saved action pages from JSON.