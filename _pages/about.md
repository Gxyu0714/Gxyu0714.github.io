---
layout: about
title: About
permalink: /
subtitle: 

# profile:
#   align: right
#   image: prof_pic.jpg
#   image_circular: false # crops the image to make it circular
#   more_info: >
#     <p>guoxinyu00714@gmail.com</p>
#     <p>Pronouns: she/her</p>

# news: true # includes a list of news items
# selected_papers: true # includes a list of papers marked as "selected={true}"
# social: true # includes social icons at the bottom of the page
---

<style>
  .research-container {
    max-width: 800px;
    margin: 0 auto;
  }
  .profile-section {
    display: flex;
    align-items: center;
    margin-bottom: 40px;
    gap: 30px;
  }
  .profile-text {
    flex: 1;
  }
  .profile-image {
    flex: 0 0 200px;
  }
  .profile-image img {
    width: 100%;
    border-radius: 50%;
    object-fit: cover;
  }
  .name {
    font-size: 2em;
    font-weight: bold;
    text-align: center;
    margin-bottom: 20px;
  }
  .research-item {
    background-color: transparent;
    padding: 20px;
    margin-bottom: 20px;
    border-radius: 8px;
    display: flex;
    gap: 20px;
  }
  .research-image {
    flex: 0 0 160px;
  }
  .research-image img {
    width: 100%;
    height: auto;
  }
  .research-content {
    flex: 1;
  }
  .papertitle {
    font-weight: bold;
    color: #333;
    text-decoration: none;
  }
  .papertitle: hover {
    color: #0066cc;
  }
  @media (max-width: 768px) {
    .profile-section {
      flex-direction: column;
      text-align: center;
    }
    .research-item {
      flex-direction: column;
    }
    .research-image {
      align-self: center;
    }
  }
</style>

<div class="research-container">
  <div class="profile-section">
    <div class="profile-text">
      <!-- <p class="name">Xinyu (Riley) Guo</p> -->
      <p>
        I'm a rising research assistant at the <a href="https://www.polyu.edu.hk/">Hong Kong Polytechnic University</a>, supervised by <a href="https://scholar.google.com/citations?user=bQegv-8AAAAJ&hl=en">Daniel T.L. Shek</a>.
        Previously, I got my master's degree in <a href="https://www.scu.edu.cn/">Sichuan University</a>.
      </p>
      <p style="text-align: center">
        <a href="mailto:xinyu714.guo@polyu.edu.hk">Email</a> &nbsp;/&nbsp;
        <a href="{{ '/assets/pdf/CV_Xinyu.pdf' | relative_url }}">CV</a> &nbsp;/&nbsp;
        <a href="https://scholar.google.com/citations?user=cDDGr3sAAAAJ&hl=en">Scholar</a> &nbsp;/&nbsp;
        <a href="https://x.com/XinyuGuo1654050">Twitter</a> &nbsp;/&nbsp;
        <a href="https://www.linkedin.com/in/xinyuguo714/">LinkedIn</a>
      </p>
    </div>
    <div class="profile-image">
      <img src="{{ '/assets/img/research/Xinyu.png' | relative_url }}" alt="Xinyu Guo">
    </div>
  </div>

  <div style="margin-bottom: 30px;">
    <h2>Research</h2>
    <p>
      I am interested in using computational, statistical, and data-driven methods to understand public and mental health, and to develop interpretable predictive models from electronic health records (EHR).
    </p>
  </div>

<!-- 1 Publication: Longitudinal NSSI Prediction -->
<div class="research-item">
  <div class="research-image">
    <img src="{{ '/assets/img/research/Workflow.jpg' | relative_url }}" alt="NSSI Research">
  </div>
  <div class="research-content">
    <a href="https://doi.org/10.1016/j.jad.2025.120110">
      <span class="papertitle">Longitudinal machine learning prediction of non-suicidal self-injury among Chinese adolescents: A prospective multicenter cohort study</span>
    </a>
    <br>
    <strong>Xinyu Guo</strong>, Liu, S., Jiang, L., Xiong, Z., Wang, L., Lu, L., ... &
    <a href="https://scholar.google.com/citations?user=bQegv-8AAAAJ&hl=en">Daniel T.L. Shek</a>
    <br>
    <em>Journal of Affective Disorders</em>, 2025, 120110. <strong>[Q1, IF: 4.9]</strong>
    <br>
    <a href="https://github.com/Gxyu0714/LongitudinalPredictor">code</a>
    /
    <a href="{{ 'https://doi.org/10.1016/j.jad.2025.120110' | relative_url }}">paper</a>
    <p> 
      We introduce a progressive prediction framework utilizing four waves of longitudinal data and seven machine learning algorithms to predict NSSI risk among 3,483 Chinese adolescents.
    </p>
  </div>
</div>

<!-- 2 Publication: Causal Analysis NSSI -->
<div class="research-item">
  <div class="research-image">
    <img src="{{ '/assets/img/research/NSSI.png' | relative_url }}" alt="Causal Analysis Research">
  </div>
  <div class="research-content">
    <a href="https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2024.1305746/full">
      <span class="papertitle">Factors and pathways of non-suicidal self-injury in children: Insights from computational causal analysis</span>
    </a>
    <br>
    <strong>Xinyu Guo</strong>, Wang, L., Li, Z., Feng, Z., Lu, L., Jiang, L., & Zhao, L.
    <br>
    <em>Frontiers in Public Health</em>, 2024, 12, 1305746. <strong>[Q1, IF: 3.4]</strong>
    <br>
    <a href="https://gxyu0714.github.io/projects/cpcd/">project</a>
    /
    <a href="{{ 'https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2024.1305746/full' | relative_url }}">paper</a>
    <p>
      Utilizing computational causal analysis to identify key factors and pathways contributing to non-suicidal self-injury behaviors in children, providing insights for intervention strategies.
    </p>
  </div>
</div>

<!-- 3 Publication: CRISP Framework -->
<div class="research-item">
  <div class="research-image">
    <img src="{{ '/assets/img/research/CRISP.png' | relative_url }}" alt="CRISP Framework">
  </div>
  <div class="research-content">
    <a href="https://link.springer.com/article/10.1186/s12911-025-02981-1">
      <span class="papertitle">CRISP: A causal relationships-guided deep learning framework for advanced ICU mortality prediction</span>
    </a>
    <br>
    Wang, L., <strong>Xinyu Guo</strong>, Shi, H., Ma, Y., Bao, H., Jiang, L., Zhao, L., Feng, Z., Zhu, T., & Lu, L.
    <br>
    <em>BMC Medical Informatics and Decision Making</em>, 2025, 25(1), 165. <strong>[Q2, IF: 3.8]</strong>
    <br>
    <a href="#">code</a>
    /
    <a href="{{ 'https://link.springer.com/article/10.1186/s12911-025-02981-1' | relative_url }}">paper</a>
    <p>
      A novel deep learning framework that leverages causal relationships to improve mortality prediction in intensive care units, demonstrating superior performance over traditional approaches.
    </p>
  </div>
</div>

<!-- 4 Publication: COVID-19 Study -->
<div class="research-item">
  <div class="research-image">
    <img src="{{ '/assets/img/research/Radar_chart.png' | relative_url }}" alt="COVID-19 Study">
  </div>
  <div class="research-content">
    <a href="https://link.springer.com/article/10.1007/s00787-024-02533-4">
      <span class="papertitle">Life changes and symptoms of depression and anxiety among Chinese children and adolescents before, during, and after the COVID-19 pandemic lockdown: a combination of cross-sectional, longitudinal, and clustering studies</span>
    </a>
    <br>
    Zeng, Y., Song, J., Zhang, Y., <strong>Xinyu Guo</strong>, Xu, X., Fan, L., Zhao, L., Song, H., & Jiang, L.
    <br>
    <em>European Child & Adolescent Psychiatry</em>, 2025, 34(3), 1025-1038. <strong>[Q1, IF: 4.9]</strong>
    <br>
    <a href="https://gxyu0714.github.io/projects/Covid19_Mental%20Health">project</a>
    /
    <a href="{{ 'https://link.springer.com/article/10.1007/s00787-024-02533-4' | relative_url }}">paper</a>
    <p>
      A comprehensive analysis of mental health changes in Chinese youth during the COVID-19 pandemic, combining multiple study designs to understand the impact of lockdown measures on depression and anxiety symptoms.
    </p>
  </div>
</div>

<!-- 5 Publication: Dynamic Causal Graph -->
<div class="research-item">
  <div class="research-image">
    <img src="{{ '/assets/img/research/Dynamic Causal.PNG' | relative_url }}" alt="Cognitive Impairment Research">
  </div>
  <div class="research-content">
    <a href="https://escholarship.org/uc/item/1gm9n38h">
      <span class="papertitle">Dynamic causal graph-based learning approach for predicting cognitive impairment in middle-aged and older adults</span>
    </a>
    <br>
    Wang, L., <strong>Xinyu Guo</strong>, Zhou, Y., Li, Z., Jiang, L., Zhao, L., Feng, Z., & Lu, L.
    <br>
    <em>In Proceedings of the 46th Annual Conference of the Cognitive Science Society</em>, 2024, Vol. 46. <strong>[Conference]</strong>
    <br>
    <a href="{{ 'https://escholarship.org/uc/item/1gm9n38h' | relative_url }}">paper</a>
    <p>
      A dynamic causal graph-based machine learning approach for predicting cognitive impairment in aging populations, incorporating temporal relationships and causal mechanisms for improved accuracy.
    </p>
  </div>
</div>

<!-- 6 Publication: Granger Causality -->
<div class="research-item">
  <div class="research-image">
    <img src="{{ '/assets/img/research/granger_causality.jpg' | relative_url }}" alt="Granger Causality Study">
  </div>
  <div class="research-content">
    <span class="papertitle">Prediction of cognitive impairment in middle-aged and elderly people: A method based on Granger causality</span>
    <br>
    Li, S., Wang, L., <strong>Xinyu Guo</strong>, Shi, H., Ma, Y., Zhang, X., Feng, Z., & Lu, L.
    <br>
    <em>In Proceedings of the 47th Annual Conference of the Cognitive Science Society</em>, 2025, Vol. 47. <strong>[Conference]</strong>
    <br>
    <a href="https://escholarship.org/uc/item/1v19r85x">paper</a>
    <p>
      A novel approach utilizing Granger causality methods for predicting cognitive impairment in middle-aged and elderly populations, focusing on temporal causal relationships in cognitive decline.
    </p>
  </div>
</div>

<!-- Publication: MDRO Study (Under Review 1) -->
<div class="research-item">
  <div class="research-image">
    <img src="{{ '/assets/img/todo.png' | relative_url }}" alt="MDRO Study">
  </div>
  <div class="research-content">
    <span class="papertitle">Causality-driven models for MDRO infection prediction: Enabling effective ICU antibiotic stewardship</span>
    <br>
    Wang, L., <strong>Xinyu Guo</strong>(co-first author), Jiang, L., Li, Z., Zhao, L., Feng, Z., & Lu, L.
    <br>
    2025. <strong>(Under review)</strong>
    <br>
    <p>
      Development of causality-driven predictive models for multidrug-resistant organism (MDRO) infections in ICU settings, aimed at improving antibiotic stewardship programs and reducing healthcare-associated infections.
    </p>
  </div>
</div>


<!-- Publication: Academic Values Study (Under Review 2) -->
<div class="research-item">
  <div class="research-image">
    <img src="{{ '/assets/img/todo.png' | relative_url }}" alt="Academic Values Study">
  </div>
  <div class="research-content">
    <span class="papertitle">Academic values, academic anxiety, and non-suicidal self-injury in Chinese adolescents: A three-wave longitudinal study</span>
    <br>
    <strong>Xinyu Guo</strong>, Peng, Y., Li, X., Zhao, L., Jiang, L., & Shek, D. T. L.
    <br>
    <em>BMC Psychology</em>, 2025. <strong>(Under review)</strong>
    <br>
    <p>
      A longitudinal investigation examining the relationships between academic values, academic anxiety, and non-suicidal self-injury behaviors among Chinese adolescents across three time points.
    </p>
  </div>
</div>



<div style="margin-bottom: 30px;">
  <h2>Project</h2>
  <p>
    Several projects that I lead are listed below:
  </p>
</div>

<div class="research-item">
  <div class="research-image">
    <img src="{{ '/assets/img/cpcd.png' | relative_url }}" alt="NSSI Research">
  </div>
  <div class="research-content">
    <a href="https://gxyu0714.github.io/projects/cpcd/">
      <span class="projecttitle"><strong>Chengdu Positive Child Development (CPCD) Survey</strong></span>
    </a>
    <br>
    <a href="https://gxyu0714.github.io/projects/cpcd/">Project Description</a>
    <p>
      I directed the 5th wave of the survey, including coordination with participating schools and logistical planning and managed field surveys, data entry using Epidata, and ensured accuracy in preliminary data processing.
    </p>
    <p>
      I independently conducted data matching, screening, cleaning, and missing value imputation for Waves 1-4, then developed a longitudinal machine learning model to predict adolescent NSSI, published in <em>Journal of Affective Disorders</em>, 2025.
    </p>
  </div>
</div>

<div class="research-item">
  <div class="research-image">
    <img src="{{ '/assets/img/cgss_logo.jpg' | relative_url }}" alt="Chinese General Social Survey (CGSS)">
  </div>
  <div class="research-content">
    <a href="http://cgss.ruc.edu.cn/English/Home.htm">
      <span class="projecttitle"><strong>Chinese General Social Survey (CGSS)</strong></span>
    </a>
    <br>
    <a href="https://gxyu0714.github.io/projects/cgss/">Project Description</a>
    <p>
      I co-led the 2023 Sichuan Province survey team, with responsibilities including project planning and coordination, field household interviews, and software management.
    </p>
  </div>
</div>

<div class="research-item">
  <div class="research-image">
    <img src="{{ '/assets/img/CDHL.jpg' | relative_url }}" alt="Chronic Disease and Health Literacy Survey">
  </div>
  <div class="research-content">
    <span class="projecttitle"><strong>Chronic Disease and Health Literacy Survey</strong></span>
    <p>
      I led a chronic disease and health literacy survey across 7 Sichuan Province cities, organizing field data collection and interviews, analyzing and visualizing results, and preparing the research report for government departments.
    </p>
  </div>
</div>



  <br>
  <p style="text-align:right;font-size:small;">
    Template from <a href="https://jonbarron.info/">Jon Barron</a>.
  </p>
</div>
