---
layout: about
title: about
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
  .papertitle:hover {
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
      <!-- <p class="name">Xinyu Guo</p> -->
      <p>
        I'm a rising research assistant at the <a href="https://www.polyu.edu.hk/">Hong Kong Polytechnic University</a>, supervised by <a href="https://scholar.google.com/citations?user=bQegv-8AAAAJ&hl=en">Daniel T.L. Shek</a>.
        Previously, I got my master's degree in <a href="https://www.scu.edu.cn/">Sichuan University</a>.
      </p>
      <p style="text-align: center">
        <a href="mailto:guoxinyu714@stu.scu.edu.cn">Email</a> &nbsp;/&nbsp;
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
      I'm interested in leveraging compute, data, and statistics to understand public health.
    </p>
  </div>

  <div class="research-item">
    <div class="research-image">
      <img src="{{ '/assets/img/research/Workflow.png' | relative_url }}" alt="NSSI Research">
    </div>
    <div class="research-content">
      <a href="https://szymanowiczs.github.io/bolt3d">
        <span class="papertitle">Longitudinal Machine Learning Prediction of Non-Suicidal Self-Injury Among Chinese Adolescents: A Prospective Multicenter Cohort Study</span>
      </a>
      <br>
      <strong>Xinyu Guo</strong>,
      <a href="https://scholar.google.com/citations?user=bQegv-8AAAAJ&hl=en">Daniel T.L. Shek</a>
      <br>
      <em>Journal of Affective Disorders</em>, 2025
      <br>
      <a href="https://github.com/Gxyu0714">code</a>
      /
      <a href="{{ '/assets/img/Workflow.jpg' | relative_url }}">paper</a>
      <p> 
        We introduce a progressive prediction framework utilizing four waves of longitudinal data and seven machine learning algorithms to predict NSSI risk among 3,483 Chinese adolescents. 
      </p>
    </div>
  </div>

  <div class="research-item">
            <div class="research-image">
                <img src="{{ '/assets/img/research/CRISP.png' | relative_url }}" alt="CRISP Framework">
            </div>
            <div class="research-content">
                <a href="#" class="papertitle">CRISP: A causal relationships-guided deep learning framework for advanced ICU mortality prediction</a>
                <br>
                Linna Wang, <strong>Xinyu Guo</strong>, Haoyue Shi, and 7 more authors
                <br>
                <em>BMC Medical Informatics and Decision Making</em>, 2025
                <br>
                <a href="#">code</a>
                /
                <a href="#">paper</a>
                <p>
                    A novel deep learning framework that leverages causal relationships to improve mortality prediction in intensive care units, demonstrating superior performance over traditional approaches.
                </p>
            </div>
        </div>
        
   <div class="research-item">
            <div class="research-image">
                <img src="{{ '/assets/img/research/NSSI Causal.png' | relative_url }}" alt="Causal Analysis Research">
            </div>
            <div class="research-content">
                <a href="#" class="papertitle">Factors and pathways of non-suicidal self-injury in children: insights from computational causal analysis</a>
                <br>
                <strong>Xinyu Guo</strong>, Linna Wang, Zhenchao Li, and 4 more authors
                <br>
                <em>Frontiers in Public Health</em>, 2024
                <br>
                <a href="#">code</a>
                /
                <a href="#">paper</a>
                <p>
                    Utilizing computational causal analysis to identify key factors and pathways contributing to non-suicidal self-injury behaviors in children, providing insights for intervention strategies.
                </p>
            </div>
        </div>

  <div class="research-item">
            <div class="research-image">
                <img src="{{ '/assets/img/research/Radar chart.png' | relative_url }}" alt="COVID-19 Study">
            </div>
            <div class="research-content">
                <a href="#" class="papertitle">Life changes and symptoms of depression and anxiety among Chinese children and adolescents before, during, and after the COVID-19 pandemic lockdown: a combination of cross-sectional, longitudinal, and clustering studies</a>
                <br>
                Yu Zeng, Jie Song, Yanan Zhang, and 6 more authors
                <br>
                <em>European Child & Adolescent Psychiatry</em>, 2024
                <br>
                <a href="#">code</a>
                /
                <a href="#">paper</a>
                <p>
                    A comprehensive analysis of mental health changes in Chinese youth during the COVID-19 pandemic, combining multiple study designs to understand the impact of lockdown measures on depression and anxiety symptoms.
                </p>
            </div>
        </div>

  <div class="research-item">
            <div class="research-image">
                <img src="{{ '/assets/img/research/Dynamic Causal.png' | relative_url }}" alt="Cognitive Impairment Research">
            </div>
            <div class="research-content">
                <a href="#" class="papertitle">Dynamic Causal Graph-Based Learning Approach for Predicting Cognitive Impairment in Middle-Aged and Older Adults</a>
                <br>
                Linna Wang, <strong>Xinyu Guo</strong>, Yunyi Zhou, and 5 more authors
                <br>
                <em>In Proceedings of the Annual Meeting of the Cognitive Science Society</em>, 2024
                <br>
                <a href="#">code</a>
                /
                <a href="#">paper</a>
                <p>
                    A dynamic causal graph-based machine learning approach for predicting cognitive impairment in aging populations, incorporating temporal relationships and causal mechanisms for improved accuracy.
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
      <img src="{{ '/assets/img/research/NSSI.png' | relative_url }}" alt="NSSI Research">
    </div>
    <div class="research-content">
      <a href="https://gxyu0714.github.io/projects/cpcd/">
        <span class="papertitle">Chengdu Positive Child Development (CPCD) Survey</span>
      </a>
      <br>
      <strong>Xinyu Guo</strong>,
      <a href="https://scholar.google.com/citations?user=bQegv-8AAAAJ&hl=en">Daniel T.L. Shek</a>
      <br>
      <em>Journal of Affective Disorders</em>, 2025
      <br>
      <a href="https://gxyu0714.github.io/projects/cpcd/">Project Description</a>
      <p>
        I Directed the 5th wave of the survey, including coordination with participating schools and logistical planning and managed field surveys, data entry using Epidata, and ensured accuracy in preliminary data processing.
      </p>
    </div>
  </div>





  <br>
  <p style="text-align:right;font-size:small;">
    Template from <a href="https://jonbarron.info/">Jon Barron</a>.
  </p>
</div>
