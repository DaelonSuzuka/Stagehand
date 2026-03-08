"""Library manager for storing and retrieving reusable trigger/filter/output/action definitions."""

import json
from pathlib import Path
from qtstrap import OPTIONS


class Library:
    """Manages built-in and user-defined library items.
    
    Library items are saved definitions that can be copied and reused.
    Built-in items are shipped with the application, user items are
    stored in the config directory.
    """
    
    def __init__(self):
        self.builtin_path = Path(OPTIONS.BASE_PATH) / 'library' / 'builtin_library.json'
        self.user_path = Path(OPTIONS.config_dir) / 'user_library.json'
        
        self.builtin_items: dict[str, list[dict]] = {}
        self.user_items: dict[str, list[dict]] = {}
        
        self.load()
    
    def load(self):
        """Load both builtin and user libraries."""
        self.builtin_items = self._load_file(self.builtin_path, is_builtin=True)
        self.user_items = self._load_file(self.user_path, is_builtin=False)
    
    def _load_file(self, path: Path, is_builtin: bool) -> dict:
        """Load a library file, returning empty structure if missing."""
        default = {
            'triggers': [],
            'filters': [],
            'outputs': [],
            'actions': [],
        }
        
        if not path.exists():
            return default
        
        try:
            with open(path, 'r') as f:
                data = json.load(f)
            
            # Ensure all categories exist
            for category in default:
                if category not in data:
                    data[category] = []
            
            # Mark builtin items
            if is_builtin:
                for category in default:  # Only iterate over known categories
                    if category in data:
                        for item in data[category]:
                            item['_builtin'] = True
            
            return data
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: Failed to load library from {path}: {e}")
            return default
    
    def save_user_library(self):
        """Save user library to disk."""
        self.user_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Remove builtin markers before saving
        data = {}
        for category in ['triggers', 'filters', 'outputs', 'actions']:
            data[category] = [
                {k: v for k, v in item.items() if k != '_builtin'}
                for item in self.user_items.get(category, [])
            ]
        
        with open(self.user_path, 'w') as f:
            json.dump(data, f, indent=2)
    
    def get_all_items(self) -> dict[str, list[dict]]:
        """Get merged list of all library items (builtin + user)."""
        merged = {
            'triggers': self.builtin_items.get('triggers', []) + self.user_items.get('triggers', []),
            'filters': self.builtin_items.get('filters', []) + self.user_items.get('filters', []),
            'outputs': self.builtin_items.get('outputs', []) + self.user_items.get('outputs', []),
            'actions': self.builtin_items.get('actions', []) + self.user_items.get('actions', []),
        }
        return merged
    
    def add_item(self, category: str, item: dict):
        """Add a new item to the user library."""
        if category not in self.user_items:
            self.user_items[category] = []
        self.user_items[category].append(item)
        self.save_user_library()
    
    def delete_item(self, category: str, index: int) -> bool:
        """Delete an item from the user library. Returns True if successful."""
        if category not in self.user_items:
            return False
        if index < 0 or index >= len(self.user_items[category]):
            return False
        self.user_items[category].pop(index)
        self.save_user_library()
        return True
    
    def rename_item(self, category: str, index: int, new_name: str) -> bool:
        """Rename an item in the user library. Returns True if successful."""
        if category not in self.user_items:
            return False
        if index < 0 or index >= len(self.user_items[category]):
            return False
        self.user_items[category][index]['name'] = new_name
        self.save_user_library()
        return True


# Global library instance
_library: Library | None = None


def get_library() -> Library:
    """Get the global library instance, creating it if necessary."""
    global _library
    if _library is None:
        _library = Library()
    return _library


def reload_library():
    """Reload the library from disk. Call after saving new items."""
    global _library
    if _library is not None:
        _library.load()
    return _library


def save_to_library(category: str, data: dict, name: str):
    """Save an item to the user library with the given name.
    
    Args:
        category: One of 'triggers', 'filters', 'outputs', 'actions'
        data: The item data (from get_data())
        name: The name to give the item in the library
    
    Returns:
        True if saved successfully
    """
    library = get_library()
    
    # Create the item with name
    item = {'name': name}
    item.update(data)
    
    library.add_item(category, item)
    return True