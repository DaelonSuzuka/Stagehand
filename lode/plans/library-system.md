# Library System Plan

## Overview

A reusable definition system for Triggers, Filters, Outputs, and Actions. Users create and configure items, then promote them to a library for reuse. Library items are copied when used, not referenced, keeping the implementation simple.

## Core Principles

1. **Bottom-up ethos**: Build in sandbox, promote reusable definitions upward
2. **Copy-on-use**: Simpler than shared references; instances are independent after creation
3. **Minimal UX**: Leverage existing copy/paste infrastructure
4. **Built-in starters**: Ship a small set of useful items for new users

---

# Phase 0: Sidebar Infrastructure

The Library will live in a sidebar panel. Before implementing the Library, we need a proper sidebar system.

## Current State

| Component | Status | Location |
|-----------|--------|----------|
| `StagehandSidebar` | Base class exists | `components.py:50` |
| `PluginSidebar` | Placeholder only | `plugin_sidebar.py` |
| Activity Bar | Partial (static buttons) | `main_window.py:99-104` |
| Splitter | Ready | `main_window.py:70-72` |
| Contribution pattern | Established | `__subclasses__()` everywhere |

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│ MainWindow                                                      │
│ ┌────────┐ ┌─────────────┐ ┌────────────────────────────────────┐│
│ │Activity│ │ Sidebar     │ │ MainTabWidget                      ││
│ │Bar     │ │ Container   │ │                                    ││
│ │        │ │             │ │                                    ││
│ │ [btn1] │ │ ┌─────────┐ │ │                                    ││
│ │ [btn2] │ │ │ Panel 1 │ │ │                                    ││
│ │ [btn3] │ │ └─────────┘ │ │                                    ││
│ │        │ │ (QStacked) │ │                                    ││
│ │        │ │             │ │                                    ││
│ └────────┘ └─────────────┘ └────────────────────────────────────┘│
│     ↑            ↑                                               │
│     │            │                                               │
│   Button ←───── Panel (StagehandSidebar)                         │
│   toggles      one per subclass                                  │
│   visibility                                                     │
└─────────────────────────────────────────────────────────────────┘
```

## Components

### 1. StagehandSidebar (Base Class)

Already exists. Extend with:

```python
class StagehandSidebar(QWidget):
    name = ''           # Unique identifier (class attr)
    icon_name = ''      # qtawesome icon name (class attr)
    
    @classmethod
    def get_subclasses(cls):
        return {c.name: c for c in cls.__subclasses__()}
```

### 2. SidebarContainer (New)

Container that holds all sidebar panels in a QStackedWidget:

```python
class SidebarContainer(QWidget):
    def __init__(self, parent=None):
        self.stack = QStackedWidget()
        self.panels: dict[str, StagehandSidebar] = {}
        
        # Discover all sidebar subclasses
        for cls in StagehandSidebar.__subclasses__():
            panel = cls(parent=self)
            self.panels[panel.name] = panel
            self.stack.addWidget(panel)
        
        # Initially hidden
        self.hide()
    
    def show_panel(self, name: str):
        """Show sidebar and switch to named panel."""
        self.show()
        self.stack.setCurrentWidget(self.panels[name])
    
    def toggle_panel(self, name: str):
        """Toggle visibility, show named panel if becoming visible."""
        if self.isVisible() and self.stack.currentWidget().name == name:
            self.hide()
        else:
            self.show_panel(name)
```

### 3. Activity Bar (Update)

The activity bar needs buttons for each sidebar panel:

```python
def create_activity_bar(self):
    self.activity_bar = BaseToolbar(self, 'activitybar', location='left', size=40)
    self.sidebar_buttons: dict[str, QToolButton] = {}
    
    for name, panel_cls in StagehandSidebar.get_subclasses().items():
        btn = QToolButton(icon=qta.icon(panel_cls.icon_name))
        btn.setCheckable(True)
        btn.clicked.connect(lambda checked, n=name: self.toggle_sidebar(n))
        self.activity_bar.addWidget(btn)
        self.sidebar_buttons[name] = btn
```

### 4. Plugin Contribution

Plugins create sidebars by subclassing:

```python
# In a plugin:
from stagehand.components import StagehandSidebar

class LibrarySidebar(StagehandSidebar):
    name = 'library'
    icon_name = 'mdi.bookshelf'
    
    def __init__(self):
        super().__init__()
        # Build UI...
```

Discovery happens automatically via `StagehandSidebar.__subclasses__()`.

## Implementation Tasks

### Phase 0.1: Sidebar Container ✅
- [x] Create `SidebarContainer` class in `components.py`
- [x] Add QStackedWidget to hold panels
- [x] Discover and instantiate all `StagehandSidebar` subclasses
- [x] Implement `show_panel()` and `toggle_panel()`

### Phase 0.2: Activity Bar Wiring ✅
- [x] Update `create_activity_bar()` in `MainWindow`
- [x] Create buttons dynamically from sidebar subclasses
- [x] Wire buttons to `toggle_sidebar_panel()` method
- [x] Make buttons checkable to show active state

### Phase 0.3: MainWindow Integration ✅
- [x] Replace placeholder `self.sidebar = QWidget()` with `SidebarContainer`
- [x] Update splitter to use new sidebar container
- [x] Ensure panels are created before activity bar buttons

### Phase 0.4: Update Existing Stubs ✅
- [x] Update `PluginSidebar` to have proper `name`, `display_name`, and `icon_name`

### Phase 0.5: Sidebar State Persistence ✅
- [x] Save current sidebar panel to QSettings when toggled
- [x] Restore sidebar state on app startup via `restore_sidebar_state()`

### Phase 1: Library Storage & Loading ✅
- [x] Create `Library` class to manage library data
- [x] Implement `load_library()` for both builtin and user files
- [x] Implement `save_library()` for user library
- [x] Add library files to `OPTIONS.config_dir` and app resource path

### Phase 2: Library Sidebar UI ✅
- [x] Create `LibrarySidebar` widget (QTreeWidget with categories)
- [x] Tree structure: Triggers / Filters / Outputs / Actions
- [x] Display items with visual badge (🔧) for built-in items
- [x] Implement context menu: Copy, Rename, Delete
- [x] Rename/Delete only apply to user library items

### Phase 3: Save to Library (Promotion) ✅
- [x] Add "Save [Item] to Library" to existing context menus for:
  - ActionWidget (saves complete action)
  - TriggerItem widgets (ActionTrigger)
  - FilterStackItem widgets (ActionFilter)
  - ActionItem (output) widgets (Action)
- [x] Create `SaveToLibraryDialog` popup:
  - Name input field
  - Preview of item being saved (JSON)
  - Confirm/Cancel buttons
- [x] Auto-detect category based on item type
- [x] Save to user library only

## File Structure

```
# Shipped with application (read-only)
src/stagehand/library/builtin_library.json

# User-defined (config directory, editable)
~/.config/stagehand/user_library.json
```

Both files merge in the UI with visual distinction for built-in items.

## Library Data Format

```json
{
  "version": 1,
  "triggers": [
    {
      "name": "Push-to-Talk Key",
      "type": "keyboard",
      "trigger": "Space"
    }
  ],
  "filters": [
    {
      "name": "OBS Window Focused",
      "type": "active window",
      "window": "OBS"
    }
  ],
  "outputs": [
    {
      "name": "Toggle OBS Mute",
      "type": "obs",
      "action": "toggle_mute"
    }
  ],
  "actions": [
    {
      "name": "Hello World on Startup",
      "trigger": {"enabled": true, "trigger_type": "startup", "trigger": "1000"},
      "filter": {"enabled": true, "filters": []},
      "action": {"type": "sandbox", "action": "print(\"Stagehand ready!\")"},
      "enabled": true
    }
  ]
}
```

Each category uses the existing serialization format (`get_data()` / `set_data()`) with an added `name` field.

## Implementation Phases

### Phase 1: Library Storage & Loading
- [ ] Create `Library` class to manage library data
- [ ] Implement `load_library()` for both builtin and user files
- [ ] Implement `save_library()` for user library
- [ ] Add library files to `OPTIONS.config_dir` and app resource path

### Phase 2: Library Sidebar UI
- [ ] Create `LibrarySidebar` widget (QTreeView with categories)
- [ ] Tree structure: Triggers / Filters / Outputs / Actions
- [ ] Display items with visual badge for built-in items
- [ ] Implement context menu: Copy, Rename, Delete
- [ ] Rename/Delete only apply to user library items

### Phase 3: Save to Library (Promotion)
- [ ] Add "Save to Library" to existing context menus for:
  - ActionWidget (saves complete action)
  - TriggerItem widgets
  - FilterStackItem widgets
  - ActionItem (output) widgets
- [ ] Create `SaveToLibraryDialog` popup:
  - Name input field
  - Preview of item being saved
  - Confirm/Cancel buttons
- [ ] Auto-detect category based on item type
- [ ] Save to user library only

### Phase 4: Copy from Library
- [ ] "Copy" context menu action puts item on clipboard
- [ ] Use existing `action_drop` mime type format
- [ ] Existing paste functionality unchanged

### Phase 5: Integration & Polish
- [ ] Add library sidebar to MainWindow
- [ ] Create default `builtin_library.json` with starter items
- [ ] Ensure actions.json migration still works
- [ ] Test copy/paste flow end-to-end

## Built-in Starter Items

Shipped in `builtin_library.json`:

| Name | Type | Description |
|------|------|-------------|
| "Hello World on Startup" | Action | Startup trigger + sandbox print |
| "Push-to-Talk Key" | Trigger | Keyboard trigger template |
| "OBS Window Focused" | Filter | Active window filter for OBS |
| "Toggle OBS Mute" | Action | Keyboard trigger + OBS toggle mute |

## UI Layout

```
┌─────────────────────────────────────────────────────────────────┐
│ MainWindow                                                      │
│ ┌──────────────┐ ┌────────────────────────────────────────────┐│
│ │ Library      │ │ MainTabWidget                              ││
│ │ Sidebar      │ │ ┌────────────────────────────────────────┐ ││
│ │              │ │ │ Page 1 │ Page 2 │ ...                  │ ││
│ │ Triggers/    │ │ └────────────────────────────────────────┘ ││
│ │   🔧 PTT Key │ │                                            ││
│ │   My Key     │ │ ActionWidget                               ││
│ │ Filters/     │ │ ┌────────────────────────────────────────┐ ││
│ │   🔧 OBS...  │ │ │ [Trigger Widget] [Run]                 │ ││
│ │ Outputs/     │ │ │ [Filter Widget]                        │ ││
│ │   🔧 Toggle..│ │ │ [Output Widget]                        │ ││
│ │ Actions/     │ │ └────────────────────────────────────────┘ ││
│ │   🔧 Hello.. │ │                                            ││
│ │              │ │                                            ││
│ └──────────────┘ └────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────────┘
```

## Key Classes to Create/Modify

### New Classes

| Class | File | Purpose |
|-------|------|---------|
| `Library` | `library/manager.py` | Load/save library data, merge builtin + user |
| `LibrarySidebar` | `library/sidebar.py` | Tree view widget |
| `LibraryTreeModel` | `library/sidebar.py` | QAbstractItemModel for library items |
| `SaveToLibraryDialog` | `library/dialog.py` | Popup for naming library items |

### Modified Classes

| Class | File | Changes |
|-------|------|---------|
| `ActionWidget` | `actions/action_widget.py` | Add "Save Action to Library" context menu |
| `ActionTrigger` | `actions/action_trigger.py` | Add "Save Trigger to Library" context menu |
| `ActionFilter` | `actions/action_filter.py` | Add "Save Filter to Library" context menu |
| `ActionOutput` | `actions/action_output.py` | Add "Save Output to Library" context menu |
| `MainWindow` | `main_window.py` | Add library sidebar dock widget |

## Copy/Paste Flow (Existing Infrastructure)

```
Existing flow:
1. User right-clicks ActionWidget → Copy
2. ActionWidget.get_drag_data() creates mime with 'action_drop' format
3. User navigates to target
4. Right-click → Paste
5. Target deserializes via set_data()

New flow:
1. User right-clicks library item → Copy
2. Library sidebar puts same 'action_drop' format on clipboard
3. User navigates to ActionWidget
4. Right-click → Paste (existing)
5. ActionWidget deserializes (existing)
```

No changes to paste target needed.

## Edge Cases

- **Duplicate names**: Allow (no unique constraint)
- **Empty library**: Still show categories
- **Missing builtin file**: Graceful degradation, show empty sidebar
- **Corrupted user library**: Log warning, create new file
- **Deleting built-in**: Show "Cannot delete built-in item" message

## Future Considerations (Out of Scope)

- Drag-and-drop from library sidebar to action editor
- Library import/export (sharing between users)
- Parameterized templates (slots for user input)
- Library search/filter
- Folders/sub-groups in library