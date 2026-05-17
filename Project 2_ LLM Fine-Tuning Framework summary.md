Summary
Project 2: LLM Fine-Tuning Framework

* Core Focus: Parameter-efficient and memory-optimized adaptation of Large Language Models (LLMs) to specialized tasks on consumer-grade hardware.

* Technologies Used: PyTorch, Hugging Face Transformers, PEFT, and BitsAndBytes.

* System Architecture: 
	Dataset -> Tokenization -> Frozen Base Model + Injected Trainable LoRA/QLoRA Adapters -> Validation -> Inference Adapter Merging.

Key Mechanisms & Results:

* LoRA & QLoRA: Frozen base weights modified via low-rank matrices (W -> W + A \times B) paired with 4-bit NormalFloat (NF4) quantization.

* Resource Efficiency: Reduced trainable parameters to <1% of the total model size, resulting in a 70–80% reduction in VRAM requirements (allowing large models to train within 16–24GB of GPU memory).

* Robustness: Integrated K-Fold cross-validation and fairness auditing, achieving a stable converged performance (F1-Score: 0.88, ROC-AUC: 0.91).
