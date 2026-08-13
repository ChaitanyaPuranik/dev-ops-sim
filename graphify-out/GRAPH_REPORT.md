# Graph Report - dev-ops-sim  (2026-08-13)

## Corpus Check
- 23 files · ~2,449 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 82 nodes · 116 edges · 13 communities (9 shown, 4 thin omitted)
- Extraction: 95% EXTRACTED · 5% INFERRED · 0% AMBIGUOUS · INFERRED: 6 edges (avg confidence: 0.5)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `25b4b2b4`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- Database
- TrafficGeneratorConfig
- ApplicationServerConfig
- run_simulation
- app.py
- Page
- dev-ops-sim
- Request
- ApplicationServer
- README.md

## God Nodes (most connected - your core abstractions)
1. `Request` - 12 edges
2. `run_simulation()` - 10 edges
3. `ApplicationServer` - 9 edges
4. `ApplicationServerConfig` - 8 edges
5. `LoadBalancer` - 8 edges
6. `TrafficGeneratorConfig` - 8 edges
7. `TrafficGenerator` - 8 edges
8. `DatabaseConfig` - 7 edges
9. `Database` - 7 edges
10. `Page()` - 7 edges

## Surprising Connections (you probably didn't know these)
- `ApplicationServer` --uses--> `Request`  [INFERRED]
  src/dev_ops_sim/nodes/application_server.py → src/dev_ops_sim/core/request.py
- `ApplicationServerConfig` --uses--> `Request`  [INFERRED]
  src/dev_ops_sim/nodes/application_server.py → src/dev_ops_sim/core/request.py
- `Database` --uses--> `Request`  [INFERRED]
  src/dev_ops_sim/nodes/database_node.py → src/dev_ops_sim/core/request.py
- `DatabaseConfig` --uses--> `Request`  [INFERRED]
  src/dev_ops_sim/nodes/database_node.py → src/dev_ops_sim/core/request.py
- `TrafficGeneratorConfig` --uses--> `Request`  [INFERRED]
  src/dev_ops_sim/nodes/traffic_generator.py → src/dev_ops_sim/core/request.py

## Import Cycles
- None detected.

## Communities (13 total, 4 thin omitted)

### Community 0 - "Database"
Cohesion: 0.24
Nodes (5): Database, DatabaseConfig, Environment, Store, Configuration for the Database.

### Community 1 - "TrafficGeneratorConfig"
Cohesion: 0.33
Nodes (4): Environment, Store, Configuration for the TrafficGenerator., TrafficGeneratorConfig

### Community 2 - "ApplicationServerConfig"
Cohesion: 0.29
Nodes (4): ApplicationServerConfig, Environment, Store, Configuration for the ApplicationServer.

### Community 3 - "run_simulation"
Cohesion: 0.20
Nodes (7): load_balancing_algorithm(), LoadBalancer, LoadBalancerConfig, Environment, Store, Configuration for the LoadBalancer., run_simulation()

### Community 4 - "app.py"
Cohesion: 0.22
Nodes (4): render_configuration(), render_metrics(), render_topology(), load_styles()

### Community 5 - "Page"
Cohesion: 0.14
Nodes (12): component, SimulationCanvas(), ConfigurationPanel(), component, Header(), component, MetricsPanel(), component (+4 more)

## Knowledge Gaps
- **2 isolated node(s):** `dev-ops-sim`, `DevOps Sim`
  These have ≤1 connection - possible missing edges or undocumented components.
- **4 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `run_simulation()` connect `run_simulation` to `Database`, `TrafficGeneratorConfig`, `ApplicationServerConfig`, `app.py`, `Request`, `ApplicationServer`?**
  _High betweenness centrality (0.218) - this node is a cross-community bridge._
- **Why does `Request` connect `Request` to `Database`, `TrafficGeneratorConfig`, `ApplicationServerConfig`, `ApplicationServer`?**
  _High betweenness centrality (0.070) - this node is a cross-community bridge._
- **Are the 6 inferred relationships involving `Request` (e.g. with `ApplicationServer` and `ApplicationServerConfig`) actually correct?**
  _`Request` has 6 INFERRED edges - model-reasoned connections that need verification._
- **What connects `dev-ops-sim`, `DevOps Sim` to the rest of the system?**
  _2 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Page` be split into smaller, more focused modules?**
  _Cohesion score 0.1437908496732026 - nodes in this community are weakly interconnected._