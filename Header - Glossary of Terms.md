Glossary of Terms

Infrastructure & Orchestration

* Auto-Scaling: A cloud computing method that automatically adjusts the number of computational resources (e.g., virtual machines, containers) in a server farm based on the load (CPU/RAM usage or custom metrics) to maintain performance and optimize costs.
* Horizontal Scaling: The strategy of adding more nodes or machines to an existing system (scaling "out") rather than increasing the capacity of an individual machine (scaling "up").
* Kubernetes Pod: The smallest deployable unit of computing in Kubernetes. A Pod encapsulates one or more containers that share storage, network IP, and specifications for how to run the containers.

Machine Learning Performance & Validation

* F1 Score: The harmonic mean of Precision and Recall. It provides a single score that balances the trade-off between the two, calculated as:   

F_1 = 2 • Precision • Recall/Precision + Recall

* ROC-AUC: The "Area Under the Receiver Operating Characteristic Curve." It measures a classifier's ability to distinguish between classes across various threshold settings. A score of 1.0 represents a perfect model, while 0.5 represents random guessing.
* Z-Score Attribution: A method of quantifying the contribution of a feature to a specific model output by normalizing the feature's influence relative to the mean and standard deviation of all feature influences (often used to identify anomalies or high-impact variables).

Data Integrity & Drift

* Concept Drift: A phenomenon in machine learning where the statistical properties of the target variable (what the model is trying to predict) change over time, rendering the model's learned patterns obsolete.
* Data Drift: A change in the distribution of input data compared to the training data. While the underlying relationship (the "concept") might remain the same, the model performs poorly because it encounters data it did not see during training.

Privacy-Preserving Machine Learning

* Differential Privacy: A system for sharing information about a dataset by describing the patterns of groups within the dataset while withholding information about individuals in the dataset (mathematically guaranteed by adding "noise" to the data).
* Homomorphic Encryption: A form of encryption that allows computation on ciphertexts, generating an encrypted result which, when decrypted, matches the result of the operations as if they had been performed on the plaintext.
* Federated Averaging: An algorithm for federated learning that updates a global model by aggregating the locally computed model weights from multiple edge devices without ever sharing the raw data from those devices.

Model Interpretability & Explainability (XAI)

* LIME (Local Interpretable Model-agnostic Explanations): A technique that explains the predictions of any classifier by approximating it locally with an interpretable model (like a linear regressor) in the vicinity of a specific data point.
* SHAP (SHapley Additive exPlanations): A game-theoretic approach to explain the output of any machine learning model by assigning each feature an importance value (Shapley value) for a particular prediction.

Model Training & Lifecycle

* LoRA (Low-Rank Adaptation): A technique for fine-tuning Large Language Models (LLMs) that freezes the pre-trained model weights and injects trainable rank decomposition matrices into each layer of the Transformer architecture, significantly reducing the number of trainable parameters.
* QLoRA (Quantized LoRA): An extension of LoRA that quantizes the pre-trained model to 4-bit precision before fine-tuning, further reducing memory usage while maintaining performance levels comparable to full fine-tuning.
* Model Registry: A centralized repository/service used to track the lifecycle of machine learning models, including versioning, artifacts, metadata, and deployment status.
* Observability: The measure of how well you can understand the internal state of a system—such as an ML model in production—by analyzing its external outputs (logs, metrics, and traces) to detect and diagnose performance degradation or drift.
* Isolation Forest: An unsupervised anomaly detection algorithm that detects anomalies by isolating observations. It works on the principle that anomalies are "few and different" and thus easier to isolate in a tree-based structure.