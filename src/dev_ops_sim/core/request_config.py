from dataclasses import dataclass


@dataclass
class RequestConfig:
    request_type: str = "default"
    payload_bytes: int = 0
    cpu_units: float = 1.0
    memory_mb: float = 1.0
    db_read_units: float = 0.0
    db_write_units: float = 0.0
    timeout: float | None = None

    def __post_init__(self):
        if not self.request_type:
            raise ValueError("request_type cannot be empty")

        if self.payload_bytes < 0:
            raise ValueError("payload_bytes cannot be negative")

        if self.cpu_units < 0:
            raise ValueError("cpu_units cannot be negative")

        if self.memory_mb < 0:
            raise ValueError("memory_mb cannot be negative")

        if self.db_read_units < 0:
            raise ValueError("db_read_units cannot be negative")

        if self.db_write_units < 0:
            raise ValueError("db_write_units cannot be negative")

        if self.timeout is not None and self.timeout <= 0:
            raise ValueError("timeout must be greater than 0")