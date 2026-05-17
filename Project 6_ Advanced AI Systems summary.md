Summary 
Project 6: Advanced AI Systems

* Core Focus: Engineering a decentralized, privacy-preserving, transparent, and computationally efficient machine learning framework.

* Technologies Used: scikit-learn (Ensembles), SHAP (Explainable AI), and distributed matrix computing tools (NumPy).

* System Architecture:

	Distributed Edge Nodes -> Federated Aggregation Server -> Global Model -> Ensemble Optimization -> Selective Layer Transfer Learning -> SHAP Explainability Layer.

Key Mechanisms & Results:

* Federated Learning: Implemented a decentralized training setup utilizing a federated averaging (FedAvg) algorithm. This managed to secure total data privacy on local edge nodes while suffering only minor performance variance (0.88 federated accuracy vs. 0.91 centralized baseline).

* Ensemble Optimization: Integrated a hard-voting ensemble layer (VotingClassifier combing bagging, boosting, and stacking) to lower model variance and bias, raising baseline predictive accuracy from 0.84 to 0.89.

* Transfer Learning: Frozen early feature extraction layers while selectively fine-tuning only the final layers, yielding a massive ~70% reduction in training time.

* Explainable AI (XAI): Integrated SHAP to extract local and global mathematical feature importances, enabling trustworthy debugging and compliance-ready model auditability.
