AI Driving Scene Evaluation System (Ollama Vision)

Overview

This project is a lightweight AI evaluation system that tests a vision-language model (LLaVA via Ollama) on simplified self-driving decision tasks. The system classifies driving scenes into three categories:
	•	STOP
	•	SLOW
	•	GO

The goal of this project is not to train a model, but to evaluate the behavior, consistency, and limitations of an existing vision AI model on a custom labeled dataset.

⸻

How It Works
	1.	Images are manually labeled and organized into folders:
	•	dataset/STOP
	•	dataset/SLOW
	•	dataset/GO
	2.	Each image is sent to a local vision model (LLaVA via Ollama)
	3.	The model predicts one of:
	•	STOP
	•	SLOW
	•	GO
	4.	Predictions are compared against ground truth labels
	5.	Results are saved to results.csv and accuracy is computed

⸻

Model Used

This project uses:
	•	Ollama
	•	LLaVA (vision-language model)

The model runs locally and does not require external API calls.

⸻

Current Performance

Accuracy: ~30%

This level of performance is expected for a small-scale evaluation setup using a lightweight local vision-language model.

The relatively low accuracy is due to:
	•	Limited model capacity compared to production-grade self-driving systems
	•	Ambiguity in real-world driving scene interpretation
	•	Small and manually curated dataset
	•	Difficulty distinguishing the “SLOW” class, which is inherently subjective
	•	Lack of large-scale training or fine-tuning on driving-specific datasets

⸻

Important Note on Limitations

This project is intentionally a small-scale simulation of AI evaluation, not a production-level autonomous driving system.

Significant performance improvements would require:
	•	Large-scale labeled driving datasets (thousands to millions of images)
	•	Domain-specific training or fine-tuning
	•	Higher-capacity multimodal models
	•	More advanced perception pipelines (object detection + tracking + sensor fusion)

Given the constraints of a local lightweight model, performance is expected to plateau without additional computational and data resources.

⸻

Skills Demonstrated
	•	Vision-language model integration (Ollama + LLaVA)
	•	Dataset creation and manual labeling
	•	AI output evaluation and benchmarking
	•	Automation with Python
	•	Performance tracking and error analysis
	•	Understanding of model limitations and bias behavior

⸻

Key Insight

During evaluation, the model showed a strong bias toward extreme classifications (STOP/GO), with significantly lower confidence in intermediate “SLOW” scenarios. This highlights a common limitation in lightweight vision-language models when applied to nuanced decision-making tasks.

⸻

Tech Stack
	•	Python
	•	Ollama
	•	LLaVA vision model
	•	CSV logging
	•	Base64 image encoding

⸻

Output Example
    image | expected | predicted | correct
    img1  | STOP     | STOP      | 1
    img2  | SLOW     | GO        | 0