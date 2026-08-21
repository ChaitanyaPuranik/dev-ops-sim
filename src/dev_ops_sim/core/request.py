from dataclasses import dataclass

# Example request types:
    # "health_check"
    # "login"
    # "get_user"
    # "search"
    # "create_order"
    # "upload_file"
    # "generate_report"

@dataclass
class Request:
    id: int
    created_at: float
    request_type: str = "default"
    payload_bytes: int = 0
    cpu_units: float = 1.0
    memory_mb: float = 1.0
    db_read_units: float = 0.0
    db_write_units: float = 0.0
    timeout: float | None = None