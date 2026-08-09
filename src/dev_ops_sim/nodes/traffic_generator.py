import simpy
from dataclasses import dataclass
from dev_ops_sim.core.request import Request

@dataclass
class TrafficGeneratorConfig:
    """
    Configuration for the TrafficGenerator.
    """
    
    rate: float 
    '''
    rate(float): Number of requests generated per simulated second. (requests/second)
    '''
    
    pattern: str 
    '''
    pattern(str): Defines how requests arrive over time.
    '''
    
    duration: float 
    '''
    duration(float): Amount of simulated time, in seconds, for which traffic is generated.
    '''

    def __post_init__(self):
        if self.rate <= 0:
            raise ValueError("rate must be greater than 0")

        if self.duration <= 0:
            raise ValueError("duration must be greater than 0")

        if self.pattern != "constant":
            raise ValueError(
                f"Unsupported traffic pattern: {self.pattern}"
            )

class TrafficGenerator:
    def __init__(
        self,
        env: simpy.Environment,
        config: TrafficGeneratorConfig,
        output: simpy.Store,
    ):
        self.env = env
        self.config = config
        self.output = output

        self.requests_generated = 0

    #Core Simulation Logic 
    def run(self):
        arrival_interval = 1 / self.config.rate
        total_requests = int(
            self.config.rate * self.config.duration
        )

        for _ in range(total_requests):
            request = Request(
                id=self.requests_generated,
                created_at=self.env.now,
            )

            yield self.output.put(request)

            self.requests_generated += 1

            yield self.env.timeout(arrival_interval)