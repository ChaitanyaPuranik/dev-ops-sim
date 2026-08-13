from dataclasses import dataclass
from typing import Any, Callable
from uuid import uuid4

from dev_ops_sim.nodes.traffic_generator import (
    TrafficGenerator,
    TrafficGeneratorConfig,
)
from dev_ops_sim.nodes.load_balancer import (
    LoadBalancer,
    LoadBalancerConfig,
)
from dev_ops_sim.nodes.application_server import (
    ApplicationServer,
    ApplicationServerConfig,
)
from dev_ops_sim.nodes.database_node import (
    Database,
    DatabaseConfig,
)


@dataclass(frozen=True)
class NodeDefinition:
    """
    Defines a type of infrastructure node available in the editor.

    A NodeDefinition describes how a node should be identified,
    displayed, configured, and later converted into a simulation
    runtime object. 
    """
    key: str
    """
    Unique identifier for the node type, such as
    "application_server" or "database".
    """
    label: str
    """
    Human-readable name displayed in the node palette
    and on the simulation canvas.
    """
    runtime_class: type
    """
    Simulation class associated with this node type,
    such as ApplicationServer or Database.
    """
    config_factory: Callable[[], Any]
    """
    Function that creates a new default configuration
    object whenever an instance of this node is added
    to the canvas.        
    """
    

@dataclass(frozen=True)
class CanvasNode:
    
    """
    Represents an individual infrastructure node placed on the canvas.

    Each CanvasNode is a separate editor instance of a NodeDefinition.
    Multiple CanvasNode objects may therefore represent the same node
    type while having different IDs and configurations.
    """
    
    id: str
    """
    Unique identifier for this specific canvas node instance.
    """
    
    definition: NodeDefinition
    """
    Describes the type of infrastructure component represented
    by this node.
    """
    
    config: Any


NODE_DEFINITIONS = {
    "traffic_generator": NodeDefinition(
        key="traffic_generator",
        label="Traffic Generator",
        runtime_class=TrafficGenerator,
        config_factory=lambda: TrafficGeneratorConfig(
            rate=10,
            pattern="constant",
            duration=60,
        ),
    ),

    "load_balancer": NodeDefinition(
        key="load_balancer",
        label="Load Balancer",
        runtime_class=LoadBalancer,
        config_factory=lambda: LoadBalancerConfig(
            algorithm="round_robin",
        ),
    ),

    "application_server": NodeDefinition(
        key="application_server",
        label="Application Server",
        runtime_class=ApplicationServer,
        config_factory=lambda: ApplicationServerConfig(
            capacity=1,
            processing_time=0.1,
        ),
    ),

    "database": NodeDefinition(
        key="database",
        label="Database",
        runtime_class=Database,
        config_factory=lambda: DatabaseConfig(
            capacity=1,
            query_time=0.1,
        ),
    ),
}


def create_canvas_node(node_type: str) -> CanvasNode:
    definition = NODE_DEFINITIONS[node_type]

    return CanvasNode(
        id=str(uuid4()),
        definition=definition,
        config=definition.config_factory(),
    )