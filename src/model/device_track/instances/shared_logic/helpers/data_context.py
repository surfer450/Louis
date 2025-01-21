from typing import NamedTuple, Any, Dict


class DataContext(NamedTuple):
    """Encapsulates the data context."""
    data: Any
    metadata: Dict[str, Any]
