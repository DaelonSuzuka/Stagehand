"""Stagehand services — Python Service subclasses for the Roadie engine.

Services are the Python-side callables injected into QuickJS contexts.
They appear in JS as stagehand.<name>.<method>() via the Proxy.

Each service is a direct Service subclass (no SandboxExtension needed).
"""

from .keyboard_service import KeyboardService, MouseService

__all__ = ['KeyboardService', 'MouseService']