import simpy

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


def run_simulation(
    traffic_rate: float,
    traffic_pattern: str,
    traffic_duration: float,
    load_balancer_algorithm: str,
    server_capacity: int,
    processing_time: float,
    database_capacity: int,
    database_query_time: float,
) -> dict:

    env = simpy.Environment()

    traffic_to_balancer_store = simpy.Store(env)
    balancer_to_server_store = simpy.Store(env)
    server_to_database_store = simpy.Store(env)

    traffic_config = TrafficGeneratorConfig(
        rate=traffic_rate,
        pattern=traffic_pattern,
        duration=traffic_duration,
    )

    load_balancer_config = LoadBalancerConfig(
        algorithm=load_balancer_algorithm,
    )

    server_config = ApplicationServerConfig(
        capacity=server_capacity,
        processing_time=processing_time,
    )

    database_config = DatabaseConfig(
        capacity=database_capacity,
        query_time=database_query_time,
    )

    traffic_generator = TrafficGenerator(
        env=env,
        config=traffic_config,
        output=traffic_to_balancer_store,
    )

    load_balancer = LoadBalancer(
        env=env,
        config=load_balancer_config,
        input=traffic_to_balancer_store,
        outputs=[balancer_to_server_store],
    )

    application_server = ApplicationServer(
        env=env,
        config=server_config,
        input=balancer_to_server_store,
        output=server_to_database_store,
    )

    database = Database(
        env=env,
        config=database_config,
        input=server_to_database_store,
    )

    env.process(traffic_generator.run())
    env.process(load_balancer.run())
    env.process(application_server.run())
    env.process(database.run())

    env.run()

    generated = traffic_generator.requests_generated
    balancer_received = load_balancer.requests_received
    balancer_forwarded = load_balancer.requests_forwarded
    received = application_server.requests_received
    completed = application_server.requests_completed
    database_received = database.requests_received
    database_completed = database.requests_completed

    simulation_time = env.now

    completion_rate = (
        completed / generated * 100
        if generated > 0
        else 0
    )

    average_throughput = (
        completed / simulation_time
        if simulation_time > 0
        else 0
    )

    drain_time = max(
        0,
        simulation_time - traffic_duration,
    )

    return {
        "generated": generated,
        "balancer_received": balancer_received,
        "balancer_forwarded": balancer_forwarded,
        "received": received,
        "completed": completed,
        "database_received": database_received,
        "database_completed": database_completed,
        "simulation_time": simulation_time,
        "completion_rate": completion_rate,
        "average_throughput": average_throughput,
        "drain_time": drain_time,
    }