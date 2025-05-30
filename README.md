### Key Concepts
* Optimization Algorithms
    - Implements greedy and dynamic programming approaches to maximize prioritization (e.g. profit-based or urgency-based scheduling)
    - Models constraints like satellite visibility windows, ground station communication limits, and resource availability (e.g. power, memory, etc)
* Cloud-Ready Design
    - Uses AWS Lambda (serverless) for scalable task processing and S3 for input/output storage simulation
    - Containerizes the scheduler with Docker for Kubernetes/EKA compatibility
* Satellite-Specific Logic
    - Simulates task dependencies (e.g. download tasks requiring prior observation tasks)
    - Integrates SAR imaging constraints (e.g. pitch/roll angles, revisit rates)

### Tools & Dependencies
* Language: Python 3.10+
* Libraries: ```pandas```(data handling), ```pytest``` (testing), ```boto3```(AWS integration), ```skyfield``` (orbit/visibility calculations)
* Infrastructure: Docker, AWS Lambda (serverless), S3 (data storage)
* Set-Up:
```bash
python -m venv venv
source venv/bin/activate # or .\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Notes
* What sort of data would I even be working with? Key objects: satellite, ground station, tasks. Create Python dataclasses for each, try to represent relevant fields (lots of guesswork here). Create fake satellite/ground station JSON's, write a  task generator script for the task objects.
* Need a way to calculate visibility windows....
* Fun fact: TLE's exist (Two-Line Element Set). Orbital mechanic data format (inclination, RAAN, eccentricity, argument of perigee, mean anomaly, mean motion, revolution number). See skyfield-tle-sandbox branch for a crash course on TLE's (and Skyfield). For dummy satellite data, use some TLE's from https://celestrak.org/. Orbital data can still be represented by JSON or CSV irl but I like having data already made to play with. Plus it's a really good into to the relevant physical aspects to consider.

### Sources
* https://davincisatellite.nl/task-scheduling-on-the-satellite/
* https://upcommons.upc.edu/bitstream/handle/2117/132523/satellite%20scheduling.pdf?sequence=3
* https://arc.aiaa.org/doi/10.2514/1.I010620
* https://github.com/lseman/satDP
* https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=02ce06a23df10ee06d879ed6075fe6d2d0d32424
* https://openreview.net/pdf?id=buIUxK7F-Bx