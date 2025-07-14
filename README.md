#  LLM-KG: Accurate Query Answering using Knowledge Graphs & LoRA-tuned LLMs

This project integrates structured **Knowledge Graphs** with a **LoRA fine-tuned Large Language Model (LLM)** to produce accurate, explainable answers to user queries. By combining symbolic reasoning from KGs and deep language understanding from LLMs, the system ensures higher factuality and contextual relevance.

##  Key Features
-  **Knowledge Graph Integration**: Encodes KGs using Graph Neural Networks (GCNs).
-  **LLM Fine-Tuning with LoRA**: Efficient adaptation using PEFT (Parameter-Efficient Fine-Tuning).
-  **Cross-Modality Pooling**: Merges graph and text representations for improved reasoning.
-  **Accurate QA**: Handles complex, multi-hop medical or scientific queries.
-  **Model Hosted on Drive**: Download and load models directly from Google Drive for lightweight deployment.

##  Technologies Used
-  HuggingFace Transformers
-  PyTorch & PyTorch Geometric (GNN)
-  PEFT (LoRA)
-  TextBlob for sentiment/useful linguistic features
-  Google Colab (for experiments)

##  Folder Structure

```
LLM-KG-Project/
├── LLM_KnowledgeGraph.ipynb       # Main notebook
├── data/                          # Example KG files (JSON/GraphML/etc.)
├── models/                        # (optional) Remote model path via Drive
├── utils/                         # Python scripts for graph loading & utilities
├── requirements.txt               # List of dependencies
└── README.md                      # Project overview
```

##  Running the Project

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run Notebook

Use Jupyter or Colab:

```bash
jupyter notebook
```

>  Make sure to mount your Google Drive to access the saved LoRA model.

### 3. Example Usage

```python
query = "What disease is caused by mutation in BRCA1 gene?"
output = model.generate_answer(query)
print(output)
```

##  Notes
- Model is fine-tuned and saved on Google Drive — link provided inside the notebook.
- Designed primarily for biomedical/scientific domain queries, but extensible to others.

---

##  Future Enhancements
- Convert notebook to script + API
- Add Streamlit or Gradio UI
- Extend to multi-graph querying

---

##  Author
**Rishav Kumar**  
**Rahul Kumar**  
Feel free to raise issues or pull requests!
