# Graph Report - .  (2026-08-11)

## Corpus Check
- cluster-only mode — file stats not available

## Summary
- 61 nodes · 93 edges · 9 communities (8 shown, 1 thin omitted)
- Extraction: 94% EXTRACTED · 6% INFERRED · 0% AMBIGUOUS · INFERRED: 6 edges (avg confidence: 0.5)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `2ea63238`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- Request
- TrafficGenerator
- ApplicationServer
- LoadBalancer
- app.py
- run_simulation
- dev-ops-sim

## God Nodes (most connected - your core abstractions)
1. `Request` - 12 edges
2. `run_simulation()` - 10 edges
3. `ApplicationServer` - 9 edges
4. `TrafficGenerator` - 8 edges
5. `TrafficGeneratorConfig` - 8 edges
6. `ApplicationServerConfig` - 8 edges
7. `LoadBalancer` - 8 edges
8. `Database` - 7 edges
9. `DatabaseConfig` - 7 edges
10. `LoadBalancerConfig` - 6 edges

## Surprising Connections (you probably didn't know these)
- `ApplicationServer` --uses--> `Request`  [INFERRED]
  src/dev_ops_sim/nodes/application_server.py → src/dev_ops_sim/core/request.py
- `ApplicationServerConfig` --uses--> `Request`  [INFERRED]
  src/dev_ops_sim/nodes/application_server.py → src/dev_ops_sim/core/request.py
- `TrafficGenerator` --uses--> `Request`  [INFERRED]
  src/dev_ops_sim/nodes/traffic_generator.py → src/dev_ops_sim/core/request.py
- `TrafficGeneratorConfig` --uses--> `Request`  [INFERRED]
  src/dev_ops_sim/nodes/traffic_generator.py → src/dev_ops_sim/core/request.py
- `Database` --uses--> `Request`  [INFERRED]
  src/dev_ops_sim/nodes/database_node.py → src/dev_ops_sim/core/request.py

## Import Cycles
- None detected.

## Communities (9 total, 1 thin omitted)

### Community 0 - "Request"
Cohesion: 0.24
Nodes (6): Request, Database, DatabaseConfig, Environment, Store, Configuration for the Database.

### Community 1 - "TrafficGenerator"
Cohesion: 0.24
Nodes (6): main(), Environment, Store, Configuration for the TrafficGenerator., TrafficGenerator, TrafficGeneratorConfig

### Community 2 - "ApplicationServer"
Cohesion: 0.24
Nodes (5): ApplicationServer, ApplicationServerConfig, Environment, Store, Configuration for the ApplicationServer.

### Community 3 - "LoadBalancer"
Cohesion: 0.27
Nodes (4): load_balancing_algorithm(), LoadBalancer, Environment, Store

### Community 4 - "app.py"
Cohesion: 0.22
Nodes (4): render_configuration(), render_metrics(), render_topology(), load_styles()

### Community 5 - "run_simulation"
Cohesion: 0.50
Nodes (3): LoadBalancerConfig, Configuration for the LoadBalancer., run_simulation()

## Knowledge Gaps
- **1 isolated node(s):** `dev-ops-sim`
  These have ≤1 connection - possible missing edges or undocumented components.
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `run_simulation()` connect `run_simulation` to `Request`, `TrafficGenerator`, `ApplicationServer`, `LoadBalancer`, `app.py`?**
  _High betweenness centrality (0.398) - this node is a cross-community bridge._
- **Why does `LoadBalancer` connect `LoadBalancer` to `run_simulation`?**
  _High betweenness centrality (0.188) - this node is a cross-community bridge._
- **Why does `Request` connect `Request` to `TrafficGenerator`, `ApplicationServer`?**
  _High betweenness centrality (0.128) - this node is a cross-community bridge._
- **Are the 6 inferred relationships involving `Request` (e.g. with `ApplicationServer` and `ApplicationServerConfig`) actually correct?**
  _`Request` has 6 INFERRED edges - model-reasoned connections that need verification._
- **What connects `dev-ops-sim` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._