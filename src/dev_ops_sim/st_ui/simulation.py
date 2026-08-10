import simpy

from dev_ops_sim.nodes.traffic_generator import (
    TrafficGenerator,
    TrafficGeneratorConfig,
)
from dev_ops_sim.nodes.application_server import (
    ApplicationServer,
    ApplicationServerConfig,
)


def run_simulation(
    traffic_rate: float,
    traffic_pattern: str,
    traffic_duration: float,
    server_capacity: int,
    processing_time: float,
) -> dict:

    env = simpy.Environment()

    # Connection between Traffic Generator
    # and Application Server.
    request_store = simpy.Store(env)

    traffic_config = TrafficGeneratorConfig(
        rate=traffic_rate,
        pattern=traffic_pattern,
        duration=traffic_duration,
    )

    server_config = ApplicationServerConfig(
        capacity=server_capacity,
        processing_time=processing_time,
    )

    traffic_generator = TrafficGenerator(
        env=env,
        config=traffic_config,
        output=request_store,
    )

    application_server = ApplicationServer(
        env=env,
        config=server_config,
        input=request_store,
    )

    env.process(traffic_generator.run())
    env.process(application_server.run())

    env.run()

    generated = traffic_generator.requests_generated
    received = application_server.requests_received
    completed = application_server.requests_completed

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
        "received": received,
        "completed": completed,
        "simulation_time": simulation_time,
        "completion_rate": completion_rate,
        "average_throughput": average_throughput,
        "drain_time": drain_time,
    }