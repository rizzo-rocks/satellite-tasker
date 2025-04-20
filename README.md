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
* Infrascruture: Docker, AWS Lambda (serverless), S3 (data storage)
* Set-Up:
```bash
python -m venv venv
source venv/bin/activate

pip install pandas pytest boto3 skyfield