import random
import simpy
from dataclasses import dataclass


ALGORITHMS = {}


def load_balancing_algorithm(name):
    def register(function):
        ALGORITHMS[name] = function
        return function

    return register


@dataclass
class LoadBalancerConfig:
    """Configuration for the LoadBalancer."""

    algorithm: str = "round_robin"

    def __post_init__(self):
        if not self.algorithm:
            raise ValueError(
                "Algorithm must be specified "
                "for the LoadBalancer."
            )


class LoadBalancer:
    def __init__(
        self,
        env: simpy.Environment,
        config: LoadBalancerConfig,
        input: simpy.Store,
        outputs: list[simpy.Store],
    ):
        self.env = env
        self.config = config
        self.input = input
        self.outputs = outputs

        if not self.outputs:
            raise ValueError(
                "LoadBalancer requires at least "
                "one backend."
            )

        if config.algorithm not in ALGORITHMS:
            raise ValueError(
                f"Unsupported load balancing algorithm: "
                f"{config.algorithm}"
            )

        self.next_backend = 0

        self.requests_received = 0
        self.requests_forwarded = 0

        self.requests_per_backend = [
            0 for _ in self.outputs
        ]

    def run(self):
        while True:
            request = yield self.input.get()

            self.requests_received += 1

            backend_index = self.select_backend()

            yield self.outputs[
                backend_index
            ].put(request)

            self.requests_forwarded += 1

            self.requests_per_backend[
                backend_index
            ] += 1

    def select_backend(self) -> int:
        algorithm = ALGORITHMS[
            self.config.algorithm
        ]

        return algorithm(self)

    @load_balancing_algorithm("round_robin")
    def select_round_robin(self) -> int:
        backend_index = self.next_backend

        self.next_backend = (
            self.next_backend + 1
        ) % len(self.outputs)

        return backend_index

    @load_balancing_algorithm("random")
    def select_random(self) -> int:
        return random.randrange(
            len(self.outputs)
        )