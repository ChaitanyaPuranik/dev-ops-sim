# Graph Report - dev-ops-sim  (2026-08-21)

## Corpus Check
- 26 files · ~3,998 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 115 nodes · 220 edges · 11 communities (9 shown, 2 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 37 edges (avg confidence: 0.56)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `c6508912`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- ApplicationServer
- TrafficGenerator
- LoadBalancer
- app.py
- Page
- dev-ops-sim
- node_registry.py
- DevOps Sim

## God Nodes (most connected - your core abstractions)
1. `CanvasNode` - 17 edges
2. `CanvasEdge` - 15 edges
3. `Page()` - 15 edges
4. `ApplicationServer` - 13 edges
5. `Request` - 12 edges
6. `ApplicationServerConfig` - 12 edges
7. `LoadBalancer` - 12 edges
8. `TrafficGeneratorConfig` - 12 edges
9. `TrafficGenerator` - 12 edges
10. `DatabaseConfig` - 11 edges

## Surprising Connections (you probably didn't know these)
- `TrafficGenerator` --uses--> `Request`  [INFERRED]
  src/dev_ops_sim/nodes/traffic_generator.py → src/dev_ops_sim/core/request.py
- `TrafficGeneratorConfig` --uses--> `Request`  [INFERRED]
  src/dev_ops_sim/nodes/traffic_generator.py → src/dev_ops_sim/core/request.py
- `CanvasEdge` --uses--> `ApplicationServerConfig`  [INFERRED]
  src/solara_ui/node_registry.py → src/dev_ops_sim/nodes/application_server.py
- `CanvasNode` --uses--> `ApplicationServerConfig`  [INFERRED]
  src/solara_ui/node_registry.py → src/dev_ops_sim/nodes/application_server.py
- `CanvasEdge` --uses--> `ApplicationServer`  [INFERRED]
  src/solara_ui/node_registry.py → src/dev_ops_sim/nodes/application_server.py

## Import Cycles
- None detected.

## Communities (11 total, 2 thin omitted)

### Community 0 - "ApplicationServer"
Cohesion: 0.14
Nodes (14): Request, ApplicationServer, ApplicationServerConfig, Environment, Store, Configuration for the ApplicationServer., Database, DatabaseConfig (+6 more)

### Community 1 - "TrafficGenerator"
Cohesion: 0.24
Nodes (6): main(), Environment, Store, Configuration for the TrafficGenerator., TrafficGenerator, TrafficGeneratorConfig

### Community 3 - "LoadBalancer"
Cohesion: 0.21
Nodes (6): load_balancing_algorithm(), LoadBalancer, LoadBalancerConfig, Environment, Store, Configuration for the LoadBalancer.

### Community 4 - "app.py"
Cohesion: 0.22
Nodes (4): render_configuration(), render_metrics(), render_topology(), load_styles()

### Community 5 - "Page"
Cohesion: 0.12
Nodes (15): Header(), component, MetricsPanel(), component, NodePalette(), component, NodeRepository, Any (+7 more)

### Community 9 - "node_registry.py"
Cohesion: 0.19
Nodes (16): build_svg(), edge_coordinates(), node_position(), Calculate arrow endpoints on the boundary of source and target node boxes., component, SimulationCanvas(), ConfigurationPanel(), Any (+8 more)

## Knowledge Gaps
- **2 isolated node(s):** `dev-ops-sim`, `Run the app`
  These have ≤1 connection - possible missing edges or undocumented components.
- **2 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `CanvasNode` connect `node_registry.py` to `ApplicationServer`, `TrafficGenerator`, `LoadBalancer`?**
  _High betweenness centrality (0.220) - this node is a cross-community bridge._
- **Why does `run_simulation()` connect `ApplicationServer` to `TrafficGenerator`, `LoadBalancer`, `app.py`?**
  _High betweenness centrality (0.152) - this node is a cross-community bridge._
- **Why does `SimulationCanvas()` connect `node_registry.py` to `Page`?**
  _High betweenness centrality (0.142) - this node is a cross-community bridge._
- **Are the 8 inferred relationships involving `CanvasNode` (e.g. with `ApplicationServer` and `ApplicationServerConfig`) actually correct?**
  _`CanvasNode` has 8 INFERRED edges - model-reasoned connections that need verification._
- **Are the 8 inferred relationships involving `CanvasEdge` (e.g. with `ApplicationServer` and `ApplicationServerConfig`) actually correct?**
  _`CanvasEdge` has 8 INFERRED edges - model-reasoned connections that need verification._
- **Are the 7 inferred relationships involving `Page()` (e.g. with `.add_node()` and `.cancel_connection()`) actually correct?**
  _`Page()` has 7 INFERRED edges - model-reasoned connections that need verification._
- **Are the 4 inferred relationships involving `ApplicationServer` (e.g. with `Request` and `CanvasEdge`) actually correct?**
  _`ApplicationServer` has 4 INFERRED edges - model-reasoned connections that need verification._