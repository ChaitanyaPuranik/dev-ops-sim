import solara

from typing import Any
from solara_ui.node_registry import (create_canvas_node, create_canvas_edge)
from dataclasses import dataclass, replace

@dataclass
class NodeRepository:

    def __init__(self):
        self.nodes = solara.use_reactive([])  # List of CanvasNode instances
        self.edges = solara.use_reactive([])  # List of CanvasEdge instances
        self.selected_node_id = solara.use_reactive(None)  # ID of the currently selected node
        self.connecting_from_id = solara.use_reactive(None)

    def add_node(self, node_type: str):
        """Create a new node and add it to the canvas."""
        new_node = create_canvas_node(node_type)

        self.nodes.set([
            *self.nodes.value,
            new_node,
        ])

        self.selected_node_id.set(new_node.id)

    def select_node(self,node_id: str):
        """Select a node currently displayed on the canvas."""
        self.selected_node_id.set(node_id)

    def delete_node(self, node_id: str):
        """Remove a node from the canvas."""
        self.nodes.set([
            node
            for node in self.nodes.value
            if node.id != node_id
        ])

        self.edges.set([
            edge
            for edge in self.edges.value
            if edge.source_id != node_id and edge.target_id != node_id
        ])
        if self.selected_node_id.value == node_id:
            self.selected_node_id.set(None)
            
        if self.connecting_from_id.value == node_id:
            self.connecting_from_id.set(None)

    def update_node_config(
        self,
        node_id: str,
        field_name: str,
        value: Any,
    ):
        """
        Replace the selected node's config with an updated
        dataclass instance.
        """

        updated_nodes = []

        for node in self.nodes.value:
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

        self.nodes.set(updated_nodes)
    
    def start_connection(self, node_id: str):
        self.connecting_from_id.set(node_id)

    def cancel_connection(self):
        self.connecting_from_id.set(None)

    def complete_connection(self, target_id: str):
        source_id = self.connecting_from_id.value

        if source_id is None:
            return

        if source_id == target_id:
            self.connecting_from_id.set(None)
            return

        # Avoid duplicate directed edges.
        already_exists = any(
            edge.source_id == source_id
            and edge.target_id == target_id
            for edge in self.edges.value
        )

        if not already_exists:
            self.edges.set(
                [
                    *self.edges.value,
                    create_canvas_edge(
                        source_id=source_id,
                        target_id=target_id,
                    ),
                ]
            )

        self.connecting_from_id.set(None)
    

