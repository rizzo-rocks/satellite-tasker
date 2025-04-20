from dataclasses import dataclass
from datetime import datetime

@dataclass
class Satellite:
    satellite_id: str
    orbit_params: dict                      # altitude (km), inclination (deg) 
    max_power_w: int                        # watts
    data_capacity_gb: int                   # gigs
    downlink_rate_mbps: int                 # megabytes per second

@dataclass
class GroundStation:
    station_id: str
    location: tuple[float, float]
    elevation_m: float                      # meters
    supported_bands: list[str]              # most common for SAR: C, X, S
    max_downlink_rate_mbps: float

@dataclass
class ObservationTask:
    task_id: str
    priority: int                           # 1 -> 10 scale
    location: tuple[float, float]          
    duration_sec: int
    viz_windows: list[tuple[datetime, datetime]]  
    data_generated_gb: int
    power_required_w: int
