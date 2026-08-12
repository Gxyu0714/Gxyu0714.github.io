---
layout: about
title: About
title_zh: 关于
permalink: /
subtitle:

news: false
selected_papers: false
social: false
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
  .papertitle,
  .projecttitle {
    font-weight: bold;
    color: var(--global-text-color);
    text-decoration: none;
  }
  .papertitle:hover,
  .projecttitle:hover {
    color: var(--global-theme-color);
  }
  .research-content,
  .research-content p,
  .profile-text p {
    color: var(--global-text-color);
  }
  .home-news {
    margin: 0 0 36px;
  }
  .home-news h2 a {
    color: inherit;
  }
  .profile-links {
    text-align: center;
    margin-top: 0.75rem;
  }
  .profile-links a {
    color: var(--global-text-color);
    text-decoration: none;
    margin: 0 0.45rem;
    font-size: 1.35rem;
    line-height: 1;
  }
  .profile-links a:hover {
    color: var(--global-theme-color);
  }
  .profile-links i {
    vertical-align: middle;
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
      <p class="lang-en">
        I am a first-year PhD student at the <a href="https://www.ucr.edu/">University of California, Riverside</a>, supervised by <a href="https://sites.google.com/ucr.edu/hollyporourke">Prof. Holly O'Rourke</a>.
        My research focuses on methodological innovations in quantitative and computational psychology and psychiatry, integrating causal inference and machine learning to extract reliable information from complex behavioral and clinical data and to develop tools that support rigorous scientific inference and decision-making.
      </p>
      <p class="lang-zh">
        我是<a href="https://www.ucr.edu/">加州大学河滨分校</a>一年级博士生，导师为 <a href="https://sites.google.com/ucr.edu/hollyporourke">Holly O'Rourke</a> 教授。
        我的研究聚焦于定量与计算心理学及精神病学中的方法学创新，将因果推断与机器学习相结合，从复杂行为与临床数据中提取可靠信息，并开发支持严谨科学推断与决策的工具。
      </p>
      <p class="lang-en">
        Previously, I received my B.S. in E-commerce (Big Data) from <a href="https://www.njucm.edu.cn/">Nanjing University of Chinese Medicine</a> and my Master of Medicine from <a href="https://www.scu.edu.cn/">Sichuan University</a>.
        I was a research assistant at the <a href="https://www.polyu.edu.hk/">Hong Kong Polytechnic University</a>, supervised by <a href="https://scholar.google.com/citations?user=bQegv-8AAAAJ&hl=en">Daniel T.L. Shek</a>.
      </p>
      <p class="lang-zh">
        此前，我于<a href="https://www.njucm.edu.cn/">南京中医药大学</a>获得电子商务（大数据）理学学士学位，于<a href="https://www.scu.edu.cn/">四川大学</a>获得医学硕士学位。
        我曾在<a href="https://www.polyu.edu.hk/">香港理工大学</a>担任研究助理，导师为 <a href="https://scholar.google.com/citations?user=bQegv-8AAAAJ&hl=en">Daniel T.L. Shek</a>。
      </p>
      <p class="profile-links">
        <a href="mailto:xinyu714.guo@polyu.edu.hk" title="Email" aria-label="Email"><i class="fa-solid fa-envelope"></i></a>
        <a href="https://scholar.google.com/citations?user=cDDGr3sAAAAJ&hl=en" title="Google Scholar" aria-label="Google Scholar"><i class="ai ai-google-scholar"></i></a>
        <a href="https://x.com/XinyuGuo1654050" title="Twitter / X" aria-label="Twitter / X"><i class="fa-brands fa-x-twitter"></i></a>
        <a href="https://www.linkedin.com/in/xinyuguo714/" title="LinkedIn" aria-label="LinkedIn"><i class="fa-brands fa-linkedin"></i></a>
      </p>
    </div>
    <div class="profile-image">
      <img src="{{ '/assets/img/research/Xinyu.png' | relative_url }}" alt="Xinyu Guo">
    </div>
  </div>

  <div class="home-news">
    <h2>
      <a href="{{ '/news/' | relative_url }}">
        <span class="lang-en">News</span>
        <span class="lang-zh">动态</span>
      </a>
    </h2>
    {% include news.liquid limit=true %}
  </div>

  <div style="margin-bottom: 30px;">
    <h2>
      <a href="{{ '/research/' | relative_url }}" style="color: inherit">
        <span class="lang-en">Research</span>
        <span class="lang-zh">研究</span>
      </a>
    </h2>
  </div>

{% include research_list.liquid hide_abstract=true %}

<div style="margin-bottom: 30px;">
  <h2>
    <span class="lang-en">Project</span>
    <span class="lang-zh">项目</span>
  </h2>
  <p class="lang-en">
    Several projects that I lead are listed below:
  </p>
  <p class="lang-zh">
    以下是我主导或共同负责的部分项目：
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



</div>
