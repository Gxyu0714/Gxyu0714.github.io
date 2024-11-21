---
layout: page
title: Dynamic Causal Graph-Based Learning
description: Predicting Cognitive Impairment in Middle-Aged and Older Adults using a novel approach.
img: assets/img/DAG1.png
importance: 2
category: research
---

### Overview

This project introduces a **Dynamic Causal Graph-Based Learning Approach** designed to predict cognitive impairment risk among middle-aged and older adults. The study leverages longitudinal data, employing causal discovery methods to uncover relationships influencing cognitive changes over time. The developed model not only improves prediction accuracy but also enhances the understanding of causal mechanisms behind cognitive impairment.

---

### Features and Contributions

#### Key Highlights
- **Dynamic Causal Graph Generation**: Constructs causal graphs for resilient feature relationships.
- **Enhanced Model Performance**: Achieved higher accuracy with fewer input variables.
- **Longitudinal Insight**: Captures evolving factors contributing to cognitive changes over time.

### Data Source

The model utilizes data from the **[China Health and Retirement Longitudinal Study (CHARLS)](https://charls.pku.edu.cn/en/)**. CHARLS aims to collect a high-quality, nationally representative sample of Chinese residents aged 45 and older, serving the needs of scientific research on the elderly.
- **Baseline Survey**: Conducted in 2011, covering approximately 10,000 households and 17,500 individuals across 150 counties/districts and 450 villages/resident committees.
- **Follow-up Frequency**: Participants are revisited every two years to track longitudinal changes.
- **Data Availability**: All data is made publicly available one year after the conclusion of each data collection phase.

This comprehensive dataset forms the backbone of our model, enabling robust analysis of the evolving factors contributing to cognitive impairment in middle-aged and older adults.

---

### Methodology

- **Causal Discovery**: Uses Graph Autoencoder (GAE) and Causal Generative Neural Networks (CGNN) to identify causal relationships.
- **Model Architecture**: Combines Long Short-Term Memory (LSTM) for temporal dependencies with Multi-Layer Perceptron (MLP) for static features.
- **Dynamic Feature Selection**: Employs top-ranked causal features for enhanced prediction accuracy.

<div class="mt-3">
    {% include figure.liquid loading="eager" path="assets/img/DAG1.png" title="Graph Structure Example" class="img-fluid rounded z-depth-1" %}
</div>
<div class="caption">
    Cognitive impairment prediction framework in CHARLS. (a) shows how to process data, variables and label. (b)shows the structure of our prediction model.
</div>

### Results

- Achieved **AUROC of 0.87** and **AUPRC of 0.72** in the final round.
- Demonstrated superior performance compared to traditional machine learning models like Logistic Regression, Random Forest, and XGBoost.
- Identified persistent indicators including demographic data, health markers, and lifestyle factors critical for prediction.


<div class="mt-3">
    {% include figure.liquid loading="eager" path="assets/img/DAG2.png" title="Model Framework" class="img-fluid rounded z-depth-1" %}
</div>
<div class="caption">
    Figure 2: River plot for 4 rounds of variables. Different colors represent the categories to which the variables belong. The presence of this color indicates that the variable is a predictor variable in this round.
</div>

<div class="mt-3">
    {% include figure.liquid loading="eager" path="assets/img/DAG3.png" title="Performance Results" class="img-fluid rounded z-depth-1" %}
</div>
<div class="caption">
    Performance evaluation for Round 4 on full feature set and dynamic top causality feature set is presented, showcasing mean values for each metric, with corresponding 95% conffdence intervals (CI) in parentheses. 
</div>

---

### Conclusion

This project advances the prediction and understanding of cognitive impairment by:
- Offering interpretable insights into causal mechanisms.
- Enhancing prediction models with dynamic feature selection.
- Contributing to targeted intervention strategies for at-risk populations.

#### Related Links
- [Read the Full Paper](https://escholarship.org/uc/item/1gm9n38h)

---

