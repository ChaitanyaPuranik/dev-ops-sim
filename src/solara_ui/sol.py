import solara

from typing import Any
from dataclasses import replace
from solara_ui.components.canvas import SimulationCanvas
from solara_ui.components.configuration_panel import ConfigurationPanel
from solara_ui.components.header import Header
from solara_ui.components.metrics_panel import MetricsPanel
from solara_ui.components.node_palette import NodePalette
from solara_ui.node_registry import (create_canvas_node, create_canvas_edge)


@solara.component
def Page():
    """
    Main page for the DevOps simulation editor.

    Owns the shared canvas state and coordinates communication
    between the node palette, simulation canvas, configuration
    panel, and metrics panel.
    """

    nodes = solara.use_reactive([])
    edges = solara.use_reactive([])
    selected_node_id = solara.use_reactive(None)
    # When not None, the user is currently creating
    # a connection beginning at this node.
    connecting_from_id = solara.use_reactive(None)

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

        edges.set([
            edge
            for edge in edges.value
            if edge.source_id != node_id and edge.target_id != node_id
        ])
        if selected_node_id.value == node_id:
            selected_node_id.set(None)
            
        if connecting_from_id.value == node_id:
            connecting_from_id.set(None)

    def update_node_config(
        node_id: str,
        field_name: str,
        value: Any,
    ):
        """
        Replace the selected node's config with an updated
        dataclass instance.
        """

        updated_nodes = []

        for node in nodes.value:
            if node.id != node_id:
                updated_nodes.append(node)
                continue

            updated_config = replace(
                node.config,
                **{
                    field_name: value,
                },
            )

            updated_node = replace(
                node,
                config=updated_config,
            )

            updated_nodes.append(updated_node)

        nodes.set(updated_nodes)
    
    def start_connection(node_id: str):
        connecting_from_id.set(node_id)

    def cancel_connection():
        connecting_from_id.set(None)

    def complete_connection(target_id: str):
        source_id = connecting_from_id.value

        if source_id is None:
            return

        if source_id == target_id:
            connecting_from_id.set(None)
            return

        # Avoid duplicate directed edges.
        already_exists = any(
            edge.source_id == source_id
            and edge.target_id == target_id
            for edge in edges.value
        )

        if not already_exists:
            edges.set(
                [
                    *edges.value,
                    create_canvas_edge(
                        source_id=source_id,
                        target_id=target_id,
                    ),
                ]
            )

        connecting_from_id.set(None)
    
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