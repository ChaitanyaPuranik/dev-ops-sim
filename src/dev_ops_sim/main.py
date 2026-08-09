import simpy
from dev_ops_sim.nodes.traffic_generator import (TrafficGenerator, TrafficGeneratorConfig)

RUN_LENGTH = 10



def main():
    env = simpy.Environment()
    output_store = simpy.Store(env)

    config = TrafficGeneratorConfig(
        rate=2,
        pattern="constant",
        duration=RUN_LENGTH,
    )
    
    traffic_generator = TrafficGenerator(
        env=env,
        config=config,
        output=output_store,
    )

    env.process(traffic_generator.run())
    env.run(until=RUN_LENGTH)

    print("Simulation finished.")    
    print(f"Total requests generated: {traffic_generator.requests_generated}")


if __name__ == "__main__":
    main()