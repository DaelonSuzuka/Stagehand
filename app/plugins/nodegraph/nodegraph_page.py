from qtstrap import *
from stagehand.components import StagehandPage


from NodeGraphQt import NodeGraph, PropertiesBinWidget, NodesTreeWidget, NodesPaletteWidget
from .nodes import basic_nodes, custom_ports_node, group_node, widget_nodes


class NodeGraphPage(StagehandPage):
    page_type = 'Node Graph'
    changed = Signal()

    def __init__(self, name='', changed=None, data=None):
        super().__init__()
        self.name = name
        self.icon_name = 'mdi.graph'

        self.label = LabelEdit(f'Graph {name}', changed=self.changed)

        graph = NodeGraph()
        graph.set_context_menu_from_file('app/plugins/nodegraph/hotkeys/hotkeys.json')

        self.graph = graph

        graph.clear_selection()
        graph.fit_to_selection()

        graph.register_nodes(
            [
                basic_nodes.BasicNodeA,
                basic_nodes.BasicNodeB,
                custom_ports_node.CustomPortsNode,
                group_node.MyGroupNode,
                widget_nodes.DropdownMenuNode,
                widget_nodes.TextInputNode,
                widget_nodes.CheckboxNode,
            ]
        )

        self.properties_bin = PropertiesBinWidget(node_graph=graph)
        self.properties_bin.setWindowFlags(Qt.Tool)

        def display_properties_bin(node):
            if not self.properties_bin.isVisible():
                self.properties_bin.show()

        # wire function to "node_double_clicked" signal.
        graph.node_double_clicked.connect(display_properties_bin)

        self.nodes_tree = NodesTreeWidget(node_graph=graph)
        self.nodes_tree.set_category_label('nodeGraphQt.nodes', 'Builtin Nodes')
        self.nodes_tree.set_category_label('nodes.custom.ports', 'Custom Port Nodes')
        self.nodes_tree.set_category_label('nodes.widget', 'Widget Nodes')
        self.nodes_tree.set_category_label('nodes.basic', 'Basic Nodes')
        self.nodes_tree.set_category_label('nodes.group', 'Group Nodes')

        self.nodes_palette = NodesPaletteWidget(node_graph=graph)
        self.nodes_palette.set_category_label('nodeGraphQt.nodes', 'Builtin Nodes')
        self.nodes_palette.set_category_label('nodes.custom.ports', 'Custom Port Nodes')
        self.nodes_palette.set_category_label('nodes.widget', 'Widget Nodes')
        self.nodes_palette.set_category_label('nodes.basic', 'Basic Nodes')
        self.nodes_palette.set_category_label('nodes.group', 'Group Nodes')

        if changed:
            self.changed.connect(changed)

        if data is not None:
            self.set_data(data)

        with CVBoxLayout(self, margins=0) as layout:
            with layout.hbox(margins=0):
                layout.add(QWidget())
                layout.add(self.label)
            with layout.split(orientation='h'):
                layout.add(self.nodes_palette)
                layout.add(graph.widget)

    def get_name(self):
        return self.label.text()

    def on_change(self):
        self.changed.emit()

    def set_data(self, data: dict) -> None:
        self.data = data

        self.label.setText(data.get('name', self.name))

        if 'session' in data:
            self.graph.deserialize_session(data['session'])

        self.graph.clear_selection()
        self.graph.fit_to_selection()

    def get_data(self) -> dict:
        data = {'page_type': self.page_type, 'name': self.label.text(), 'session': self.graph.serialize_session()}
        return data
