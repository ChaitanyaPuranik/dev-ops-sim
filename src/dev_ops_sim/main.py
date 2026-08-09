import simpy
from dev_ops_sim.nodes.traffic_generator import (TrafficGenerator, TrafficGeneratorConfig)
from dev_ops_sim.nodes.application_server import (ApplicationServer, ApplicationServerConfig)

#Example configurations for the simulation
RUN_LENGTH = 10
TRAFFIC_GENERATOR_CONFIG = TrafficGeneratorConfig(
    rate=50,
    pattern="constant",
    duration=RUN_LENGTH,
)
APP_SERVER_CONFIG = ApplicationServerConfig(
    capacity=2,
    processing_time=0.1,
)


def main():
    env = simpy.Environment()
    request_store = simpy.Store(env)

    traffic_generator = TrafficGenerator(
        env=env,
        config=TRAFFIC_GENERATOR_CONFIG,
        output=request_store,
    )
    
    application_server = ApplicationServer(
        env=env,
        config=APP_SERVER_CONFIG,
        input=request_store,
    )

    env.process(traffic_generator.run())
    env.process(application_server.run())
    env.run(until=RUN_LENGTH)

    print("Simulation finished.")    
    print(
        "Generated:",
        traffic_generator.requests_generated,
    )

    print(
        "Received:",
        application_server.requests_received,
    )   

    print(
        "Completed:",
        application_server.requests_completed,
    )


if __name__ == "__main__":
    main()