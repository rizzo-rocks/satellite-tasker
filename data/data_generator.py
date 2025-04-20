from faker import Faker
import random
from datetime import datetime, timedelta
import schemas as s

"""
Stage 1: Synthetic Task Generation

Did my best to fake the data but I'm sure some of these parameters are unrealistic.
"""

def generate_tasks(num_tasks:int):
    fake = Faker()
    tasks = []

    for _ in range(num_tasks):
        tasks.append(s.ObservationTask(
            task_id=fake.uuid4(),
            priority=random.randint(1,10),
            location=(fake.latitude(), fake.longitude()),
            duration_sec=random.randint(60, 600),    
            time_windows=[(datetime.utcnow(), datetime.utcnow()+timedelta(hours=2))],    
            data_generated_gb=random.randint(1, 20),
            power_required_w=random.randint(200, 1000)
            )
        )

    return tasks

