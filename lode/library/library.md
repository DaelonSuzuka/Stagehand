# Library System

## Overview

The Library provides a collection of reusable trigger, filter, output, and action definitions. Items are stored in JSON files and can be copied into action configurations. The library uses a copy-on-use model - when an item is copied, it becomes an independent instance.

## File Structure

```
# Built-in library (shipped with app, read-only)
src/stagehand/library/builtin_library.json

# User library (config directory, editable)
~/.config/stagehand/user_library.json
```

## Data Format

```json
{
  "version": 1,
  "triggers": [
    {"name": "Push-to-Talk Key", "trigger_type": "keyboard", "trigger": "Space", ...}
  ],
  "filters": [
    {"name": "OBS Window Focused", "type": "active window", "window": "OBS", ...}
  ],
  "outputs": [
    {"name": "Toggle OBS Mute", "type": "obs", "action": "toggle_mute", ...}
  ],
  "actions": [
    {"name": "Hello World on Startup", "trigger": {...}, "filter": {...}, "action": {...}, ...}
  ]
}
```

Each category uses the existing serialization format (`get_data()`/`set_data()`) with an added `name` field.

## Components

### Library Manager

**File**: `src/stagehand/library/manager.py`

Manages loading, saving, and accessing library items.

```python
from stagehand.library import get_library

library = get_library()

# Get all items merged (builtin + user)
items = library.get_all_items()

# Add new user item
library.add_item('triggers', {'name': 'My Trigger', ...})

# Delete user item
library.delete_item('triggers', index)

# Rename user item
library.rename_item('triggers', index, 'New Name')
```

### LibrarySidebar

**File**: `src/stagehand/library/sidebar.py`

Sidebar panel with tree view of library items.

```mermaid
classDiagram
    class StagehandSidebar {
        <<abstract>>
        +name: str
        +display_name: str
        +icon_name: str
    }
    
    class LibrarySidebar {
        +name: 'library'
        +display_name: 'Library'
        +icon_name: 'mdi.bookshelf'
        +tree: LibraryTreeWidget
        +refresh()
    }
    
    class LibraryTreeWidget {
        +refresh()
        +show_context_menu(pos)
        +copy_item(category, index)
        +rename_item(category, index)
        +delete_item(category, index)
    }
    
    StagehandSidebar <|-- LibrarySidebar
    LibrarySidebar --> LibraryTreeWidget
```

## Context Menu Actions

| Action | Built-in Items | User Items |
|--------|----------------|------------|
| Copy | ✓ | ✓ |
| Rename | ✗ | ✓ |
| Delete | ✗ | ✓ |

## Built-in Starter Items

| Name | Type | Description |
|------|------|-------------|
| Push-to-Talk Key | Trigger | Keyboard trigger template (key unset) |
| OBS Window Focused | Filter | Active window filter for OBS |
| Toggle OBS Mute | Output | OBS mute toggle action |
| Hello World on Startup | Action | Startup trigger + sandbox print |
| Toggle OBS Mute on F1 | Action | Keyboard F1 trigger + OBS mute |

## Copy Flow

```
1. User right-clicks library item → Copy
2. LibraryTreeWidget.copy_item() puts JSON on clipboard
3. User navigates to ActionWidget
4. Right-click → Paste (existing paste functionality)
5. ActionWidget deserializes via set_data()
```

## Save to Library (Future)

Not yet implemented. Will add:
- "Save Trigger to Library" context menu on TriggerItem
- "Save Filter to Library" context menu on FilterStackItem  
- "Save Output to Library" context menu on ActionItem
- "Save Action to Library" context menu on ActionWidget
- `SaveToLibraryDialog` popup for naming items