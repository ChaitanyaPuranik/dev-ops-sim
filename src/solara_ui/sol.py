import solara

from dataclasses import replace
from solara_ui.components.canvas import SimulationCanvas
from solara_ui.components.configuration_panel import ConfigurationPanel
from solara_ui.components.header import Header
from solara_ui.components.metrics_panel import MetricsPanel
from solara_ui.components.node_palette import NodePalette
from solara_ui.node_repo import (add_node, select_node, delete_node, update_node_config, start_connection, complete_connection, cancel_connection, nodes, edges, selected_node_id, connecting_from_id)


@solara.component
def Page():
    """
    Main page for the DevOps simulation editor.

    Owns the shared canvas state and coordinates communication
    between the node palette, simulation canvas, configuration
    panel, and metrics panel.
    """

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
                edges=edges.value,
                selected_node_id=selected_node_id.value,
                connecting_from_id=connecting_from_id.value,
                on_select_node=select_node,
                on_delete_node=delete_node,
                on_start_connection=start_connection,
                on_complete_connection=complete_connection,
                on_cancel_connection=cancel_connection,
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
                on_update_config=update_node_config,
            )

    MetricsPanel()