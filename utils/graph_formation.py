# -*- coding: utf-8 -*-
"""Graph_formation.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1fcQuk_Au1kxYszwSOAaLoRKtAsmbf5sZ
"""

data3=pd.read_csv("C:/Users/CSE IIT BHILAI/Desktop/RishavKumar(M24DS012)/updated_diseases_dataset.csv")

disease_symptoms = {}

def extract_symptoms(row):
    return [col for col in data3.columns[1:-3] if row[col] == 1]

data3["symptom_list"] = data3.apply(extract_symptoms, axis=1)

data3["medicine"] = data3["medicine"].apply(lambda x: [med.strip() for med in x.split(",")] if isinstance(x, str) else x)


data4=data3[["diseases","prescription","medicine","symptom_list"]]
fever_rows = data4[data4['diseases'] == 'fever']

import networkx as nx

# Convert to DataFrame
df = data3.head(10)

# Create a directed graph
G = nx.DiGraph()
edge_labels={}

# Add nodes and edges
for _, row in df.iterrows():
    disease = row["diseases"]
    G.add_node(disease, type="disease")  # Add disease node

    # Add symptom nodes and edges
    for symptom in row["symptom_list"]:
        G.add_node(symptom, type="symptom")
        G.add_edge(disease, symptom, relation="has_symptom")
        edge_labels[(disease, symptom)] = "has_symptoms"

        G.add_edge(symptom, disease, relation="symptom_of")
        edge_labels[(symptom, disease)] = "symptom_of"

    # Add prescription node
    prescription = row["prescription"]
    G.add_node(prescription, type="prescription")
    G.add_edge(disease, prescription, relation="treated_with")
    edge_labels[(disease, prescription)] = "treated_with"

    G.add_edge(prescription, disease, relation="prescription of")
    edge_labels[(prescription, disease)] = "prescription of"

    # Add medicine nodes and edges
    #medicines = row["medicine"].split(", ")
    for med in row["medicine"]:
        G.add_node(med, type="medicine")
        G.add_edge(disease, med, relation="prescribed_medicine")
        edge_labels[(disease, med)] = "prescribed medecines"

        G.add_edge(med, disease, relation="medicine for")
        edge_labels[(med, disease)] = "medecines for"

plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G, seed=42)  # Positioning of nodes
nx.draw(G, pos, with_labels=True, node_size=3000, node_color="lightblue", font_size=8, edge_color="gray")

# Draw edge labels (relation names)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color="red", font_size=8)

# Show the graph
plt.title("Medical Knowledge Graph")
plt.show()