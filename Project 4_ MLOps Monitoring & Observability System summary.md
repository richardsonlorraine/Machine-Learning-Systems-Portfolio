Summary 
Project 4: MLOps Monitoring & Observability System

* Core Focus: Mitigating production risks like silent model errors, performance degradation, and data drift through continuous telemetry collection and automated alerting.

* Technologies Used: Prometheus, Grafana, NumPy.

* System Architecture: 

	Live Predictions -> Metric Collection & Structured Logging -> Statistical Drift Detection -> Prometheus Storage -> Grafana Dashboards + Alerting Mechanism.

Key Mechanisms & Results:

* System Performance: Tracked real-time request metrics, capturing an average latency of 120ms and a P99 latency of 180ms.

* Data Drift Detection: Applied a statistical distribution comparison algorithm to compute a quantitative drift score against baseline training data, successfully triggering live alerts when the score crossed a designated threshold (0.12 score vs. 0.10 threshold).

* Model Tracking: Monitored real-time accuracy and captured a simulated live F1-score degradation from 0.87 down to 0.81, enabling proactive engineering interventions.
