from dataclasses import dataclass
from datetime import datetime

@dataclass
class Satellite:
    id: str
    orbit_altitude_km: float                # kilometers
    max_power_w: int                        # watts
    data_capacity_gb: int                   # gigs
    current_location: tuple[float, float]   # lat, long 

@dataclass
class ObservationTask:
    task_id: str
    priority: int                           # 1 -> 10 scale
    location: tuple[float, float]          
    duration_sec: int
    time_windows: list[tuple[datetime, datetime]]  
    data_generated_gb: int
    power_required_w: int
