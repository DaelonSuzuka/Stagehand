from __future__ import annotations

"""
Adapter that wraps SandboxExtension instances as Services.

During migration, this lets the Engine work with existing extensions
without any per-extension changes. Each SandboxExtension is auto-wrapped
so its methods are callable from JS via the stagehand Proxy.

Later, each extension can be swapped from SandboxExtension to Service
directly (one-line parent class change), and the adapter is removed.
"""

import json

from .engine import Service


class ExtensionToServiceAdapter(Service):
    """
    Wraps any SandboxExtension as a Service automatically.

    No changes to extension files needed. Methods are forwarded to the
    wrapped extension via __getattr__. _dispatch() introspects the
    extension and auto-serializes complex return values (dicts/lists).

    Usage:
        from stagehand.sandbox import Sandbox
        from stagehand.roadie import Engine, ExtensionToServiceAdapter

        engine = Engine()
        for ext in Sandbox().extensions.values():
            engine.register_service(ExtensionToServiceAdapter(ext))
    """

    def __init__(self, extension):
        self._extension = extension
        self.name = extension.name if isinstance(extension.name, list) else [extension.name]
        # Simplify: name is always stored as a list for Service.names
        # but Service expects str | list[str], so pass the original
        if isinstance(extension.name, list):
            self.name = extension.name
        else:
            self.name = extension.name

    def __getattr__(self, name: str):
        """Forward any method calls to the wrapped extension."""
        return getattr(self._extension, name)

    def methods(self) -> dict[str, str]:
        """Introspect the wrapped extension for callable methods."""
        result = {}
        for attr_name in dir(self._extension):
            if attr_name.startswith('_'):
                continue
            attr = getattr(self._extension, attr_name)
            if callable(attr) and not isinstance(attr, type):
                result[attr_name] = attr.__doc__ or ''
        return result

    def _dispatch(self, method_name: str, *args):
        """Call the extension method, auto-serialize complex returns."""
        method = getattr(self._extension, method_name)
        result = method(*args)
        if isinstance(result, (dict, list)):
            return json.dumps(result)
        return result