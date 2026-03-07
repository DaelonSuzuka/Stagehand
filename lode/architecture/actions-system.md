# Actions System

## Overview

Actions are the core user-configurable unit. Each Action combines:
- **Trigger**: Event source (keyboard, device, etc.)
- **Filter**: Optional conditions (AND-logic)
- **Output**: Operation to perform

```mermaid
flowchart TB
    subgraph ActionWidget
        Trigger[Trigger Widget]
        Filter[Filter Widget]
        Output[Output Widget]
    end
    
    Trigger -->|activates| Filter
    Filter -->|passes| Output
    Filter -->|fails| X((X))
    
    subgraph TriggerTypes
        KeyboardTrigger
        JoystickTrigger
        DeviceTrigger
        SandboxTrigger
        StartupTrigger
    end
    
    subgraph OutputTypes
        SandboxAction
        KeyboardAction
        OBSAction
        ShellAction
        CyberAction
    end
    
    subgraph FilterTypes
        SandboxFilter
        WindowFilter
        ProgramRunningFilter
    end
    
    TriggerTypes --> Trigger
    OutputTypes --> Output
    FilterTypes --> Filter
```

## Data Model

```json
{
  "name": "My Action",
  "enabled": true,
  "trigger": {
    "enabled": true,
    "trigger_type": "keyboard",
    "trigger": "ctrl+shift+a"
  },
  "filter": {
    "enabled": true,
    "filters": [
      {"filter_type": "sandbox", "filter": "data['mode'] == 'streaming'"}
    ]
  },
  "action": {
    "type": "sandbox",
    "action": "print('Hello!')"
  }
}
```

## Class Hierarchy

```mermaid
classDiagram
    class ActionWidget {
        +name: str
        +enabled: AnimatedToggle
        +trigger: ActionTrigger
        +filter: ActionFilter
        +action: Action
        +run()
        +get_data() dict
        +set_data(data)
    }
    
    class ActionWidgetGroup {
        +actions: list
        +filter: ActionFilter
        +active: bool
        +can_run() bool
        +register(action)
    }
    
    class ActionTrigger {
        +type: QComboBox
        +trigger: TriggerItem
        +set_data(data)
        +get_data() dict
    }
    
    class ActionFilter {
        +filters: list~FilterStack~
        +check_filters() bool
        +open_editor()
    }
    
    class Action {
        +type: QComboBox
        +action: ActionItem
        +run()
    }
    
    ActionWidget --> ActionWidgetGroup
    ActionWidget --> ActionTrigger
    ActionWidget --> ActionFilter
    ActionWidget --> Action
```

## Execution Flow

```mermaid
sequenceDiagram
    participant User
    participant Trigger
    participant ActionWidget
    participant Filter
    participant Sandbox
    participant Output
    
    User->>Trigger: Event (key press, etc.)
    Trigger->>ActionWidget: emit activated
    
    ActionWidget->>ActionWidget: group.can_run()?
    alt Group inactive or filter fails
        ActionWidget-->>Trigger: Ignore
    end
    
    ActionWidget->>Filter: check_filters()
    Filter->>Sandbox: eval(filter_expression)
    Sandbox-->>Filter: bool result
    
    alt Filter returns True
        Filter-->>ActionWidget: True
        ActionWidget->>Sandbox: Set this/source
        ActionWidget->>Output: run()
        Output->>Sandbox: Execute output
        Sandbox-->>Output: Success/Error
    else Filter returns False
        Filter-->>ActionWidget: False
        ActionWidget-->>Trigger: Skip output
    end
```

## Registration Pattern

All trigger/action/filter types register via class inheritance:

```python
# Trigger registration
class MyTrigger(TriggerItem):
    name = 'my_trigger'  # Shown in trigger dropdown
    # Must implement: set_data(), get_data()

# Action registration  
class MyAction(ActionItem):
    name = 'my_action'  # Shown in action dropdown
    # Must implement: set_data(), get_data(), run()

# Filter registration
class MyFilter(FilterStackItem):
    name = 'my_filter'  # Shown in filter dropdown
    # Must implement: set_data(), get_data(), check()
```

Discovery happens via `__subclasses__()` on base classes.