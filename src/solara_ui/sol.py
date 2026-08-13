import solara

from solara_ui.components.canvas import SimulationCanvas
from solara_ui.components.configuration_panel import ConfigurationPanel
from solara_ui.components.header import Header
from solara_ui.components.metrics_panel import MetricsPanel
from solara_ui.components.node_palette import NodePalette
from solara_ui.node_registry import create_canvas_node


@solara.component
def Page():
    """
    Main page for the DevOps simulation editor.

    Owns the shared canvas state and coordinates communication
    between the node palette, simulation canvas, configuration
    panel, and metrics panel.
    """

    nodes = solara.use_reactive([])
    selected_node_id = solara.use_reactive(None)

    def add_node(node_type: str):
        """Create a new node and add it to the canvas."""
        new_node = create_canvas_node(node_type)

        nodes.set([
            *nodes.value,
            new_node,
        ])

        selected_node_id.set(new_node.id)

    def select_node(node_id: str):
        """Select a node currently displayed on the canvas."""
        selected_node_id.set(node_id)

    def delete_node(node_id: str):
        """Remove a node from the canvas."""
        nodes.set([
            node
            for node in nodes.value
            if node.id != node_id
        ])

        if selected_node_id.value == node_id:
            selected_node_id.set(None)

    selected_node = next(
        (
            node
            for node in nodes.value
            if node.id == selected_node_id.value
        ),
        None,
    )

    Header()

    with solara.Row(
        style={
            "width": "100%",
            "height": "70vh",
        }
    ):
        # Node palette
        with solara.Column(
            style={
                "width": "220px",
                "height": "100%",
            }
        ):
            NodePalette(
                on_add_node=add_node,
            )

        # Simulation canvas
        with solara.Column(
            style={
                "flex": "1",
                "height": "100%",
            }
        ):
            SimulationCanvas(
                nodes=nodes.value,
                selected_node_id=selected_node_id.value,
                on_select_node=select_node,
                on_delete_node=delete_node,
            )

        # Selected node configuration
        with solara.Column(
            style={
                "width": "300px",
                "height": "100%",
            }
        ):
            ConfigurationPanel(
                node=selected_node,
            )

    MetricsPanel()