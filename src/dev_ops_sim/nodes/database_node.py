from dataclasses import dataclass
from dev_ops_sim.core.request import Request
import simpy


@dataclass
class DatabaseConfig:
    """Configuration for the Database."""
    capacity: int
    '''
    capacity(int): Maximum number of database operations that can execute concurrently.
    '''

    query_time: float
    '''
    query_time(float): Simulation time required to execute one database operation
    '''
    def __post_init__(self):
        if self.capacity <= 0:
            raise ValueError("capacity must be greater than 0")

        if self.query_time <= 0:
            raise ValueError("query_time must be greater than 0")
        
class Database:
    def __init__(
        self,
        env: simpy.Environment,
        config: DatabaseConfig,
        input: simpy.Store,
        output: simpy.Store | None = None,
    ):
        self.env = env
        self.config = config
        self.input = input
        self.output = output

        self.resource = simpy.Resource(
            env,
            capacity=config.capacity,
        )

        self.requests_received = 0
        self.requests_completed = 0
        self.requests_processing = 0

    def run(self):
        while True:
            request = yield self.input.get()

            self.requests_received += 1

            self.env.process(
                self.process_request(request)
            )

    def process_request(self, request: Request):
        with self.resource.request() as resource_request:
            yield resource_request

            self.requests_processing += 1

            yield self.env.timeout(
                self.config.query_time
            )

            self.requests_processing -= 1
            self.requests_completed += 1

            if self.output is not None:
                yield self.output.put(request)