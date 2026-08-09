import simpy
from dev_ops_sim.core.request import Request
from dataclasses import dataclass

@dataclass
class ApplicationServerConfig:
    
    """Configuration for the ApplicationServer.
    """
    
    capacity: int
    '''
    capacity(int): The maximum number of requests that can be processed simultaneously.
    '''
    
    processing_time: float
    '''
    processing_time(float): The time it takes to process a single request.
    '''

    def __post_init__(self):
        if self.capacity <= 0:
            raise ValueError("capacity must be greater than 0")

        if self.processing_time <= 0:
            raise ValueError("processing_time must be greater than 0")
        


class ApplicationServer:
    def __init__(
        self,
        env: simpy.Environment,
        config: ApplicationServerConfig,
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
                self.config.processing_time
            )

            self.requests_processing -= 1
            self.requests_completed += 1

            if self.output is not None:
                yield self.output.put(request)