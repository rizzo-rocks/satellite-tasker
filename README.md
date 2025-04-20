### Key Concepts:
* Optimization Algorithms
    - Implements greedy and dynamic programming approaches to maximize prioritization (e.g. profit-based or urgency-based scheduling)
    - Models constraints like satellite visibility windows, ground station communication limits, and resource availability (e.g. power, memory, etc)
* Cloud-Ready Design
    - Uses AWS Lambda (serverless) for scalable task processing and S3 for input/output storage simulation
    - Containerizes the scheduler with Docker for Kubernetes/EKA compatibility
* Satellite-Specific Logic
    - Simulates task dependencies (e.g. download tasks requiring prior observation tasks)
    - Integrates SAR imaging constraints (e.g. pitch/roll angles, revisit rates)