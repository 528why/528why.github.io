---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

I am Huyu Wu(伍胡宇), a graduate student at the [Institute of Computing Technology, Chinese Academy of Sciences (ICT)](http://www.ict.cas.cn/). I received my bachelor's degree in Artificial Intelligence from the [School of Computer Science](https://cs.scu.edu.cn/).

My research interests lie in the **Multimodal Large Language Models** and **Dataset Distillation**. You can find my main research interests on <a href='https://scholar.google.com/citations?user=ehxjrc8AAAAJ'><img src="https://img.shields.io/badge/Citations-21-blue.svg?logo=google-scholar"></a>


# 🔥 News
- *2025.09*: &nbsp;🎉🎉 One paper is accepted by Neural Networks.
- *2024.10*: &nbsp;🎉🎉 One paper is accepted by Applied Soft Computing.
- *2024.06*: &nbsp;🎉🎉 One paper is accepted by Expert Systems with Applications.
- *2024.03*: &nbsp;🎉🎉 One paper is accepted by IJCNN 2024
- 
# 📝 Publications 

<!--
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">IJCNN 2024</div><img src='images/500x300.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Deep Residual Learning for Image Recognition](https://openaccess.thecvf.com/content_cvpr_2016/papers/He_Deep_Residual_Learning_CVPR_2016_paper.pdf)

**Huyu Wu**, Xiangyu Zhang, Shaoqing Ren, Jian Sun

[**Project**](https://scholar.google.com/citations?view_op=view_citation&hl=zh-CN&user=DhtAFkwAAAAJ&citation_for_view=DhtAFkwAAAAJ:ALROH1vI_8AC) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
- Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 
</div>
</div>
-->
- **Wu H**, Jia B, Yuan X M. LLM-Led Vision-Spectral Fusion: A Zero-Shot Approach to Temporal Fruit Image Classification[J]. **Neural Networks**, 2025: 108155. (First Author, CCF-B)
- Jia B, Guo Z, Huang T, Guo F, & **Wu H**. A generalized Lorenz system-based initialization method for deep neural networks[J]. **Applied Soft Computing**, 2024, 167: 112316. (Last Author, 中科院一区TOP)
- Jia B, **Wu H**, Guo K. Chaos theory meets deep learning: A new approach to time series forecasting[J]. **Expert Systems with Applications**, 2024, 255: 124533. (Co-First Author, 中科院一区TOP)
- **Wu H**, Jia B, Sheng G. Early-Late Dropout for DivideMix: Learning with Noisy Labels in Deep Neural Networks[C]//2024 International Joint Conference on Neural Networks (**IJCNN**). IEEE, 2024: 1-8. (First Author, CCF-C)

  
# 📖 Educations
- *2025.09 - Present*, Institute of Computing Technology, University of Chinese Academy of Sciences
- *2021.09 - 2025.06*, College of Computer Science, Artificial Intelligence, Sichuan University
- *2020.09 - 2021.06*, Business School, Business Administration, Sichuan University



# 💻 Internships
- *2024.08 - 2025.09*, Intern of [TSAIL - Tsinghua University](https://ml.cs.tsinghua.edu.cn/projects.html)
<!--
- *2024.04 - 2024.08*, Intern of [Institute of Automation Chinese Academy](http://english.ia.cas.cn/)
-->
- *2023.12 - 2024.04*, Research Assistant of [National University of Singapore - Institute of Operations Research and Analytics](https://iora.nus.edu.sg/) 
<!--
  Associate Professor YUAN, Xue-Ming
-->
- *2022.11 - 2024.08*, Research Assistant of [Sichuan University - Machine Intelligence Lab](https://www.machineilab.org/)
<!--
  Associate Professor Quan Guo
-->


# 📙 Projects

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">2025.03 - 2025.09</div><img src='images/DAP.png' alt="sym" width="60%"></div></div>
<div class='paper-box-text' markdown="1">
**Diffusion Models As Dataset Distillation Priors**   
Dataset distillation seeks to create compact yet informative datasets, but balancing diversity, generalization, and representativeness remains challenging. We propose Diffusion As Priors (DAP), which leverages the inherent representativeness prior in diffusion models by quantifying synthetic–real data similarity in feature space with a Mercer kernel and guiding the reverse diffusion process without retraining. 
</div>
</div>



<div class='paper-box'><div class='paper-box-image'><div><div class="badge">2025.05 - 2025.08</div><img src='images/MLLM.png' alt="sym" width="60%"></div></div>
<div class='paper-box-text' markdown="1">
**When Language Overrules: Revealing Text Dominance in Multimodal Large Language Models**   
Multimodal Large Language Models (MLLMs) achieve strong results but suffer from text dominance, where textual inputs outweigh other modalities. We present the first systematic study of this issue across images, videos, audio, time-series, and graphs, introducing two metrics—the Modality Dominance Index (MDI) and Attention Efficiency Index (AEI)—to quantify the imbalance. Our analysis reveals its pervasive nature and key causes, and we propose a simple token compression method that rebalances attention, reducing LLaVA-7B’s MDI from 10.23 to 0.86. This work offers insights and methods for building more balanced multimodal models.
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">2024.08 - 2025.03</div><img src='images/DC3.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
**Dataset Condensation with Color Compensation**   
Dataset condensation faces inherent trade-offs between performance and fidelity. Current methods struggle with inefficiency (image-level selection) or semantic distortion (pixel-level optimization). We identify color’s dual role as an information carrier and semantic unit as critical. To address this, we propose DC3, which enhances color diversity via latent diffusion models after calibrated image selection. Experiments show DC3 outperforms SOTA methods across benchmarks. Notably, DC3 enables fine-tuning pre-trained diffusion models with condensed datasets without degradation (validated by FID scores), marking the first exploration of this capability.
</div>
</div>

<!--
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">2024.12 - 2025.03</div><img src='images/FMCHS_Framework.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
**FMCHS: Advancing Traditional Chinese Medicine Herb Recommendation with Fusion of Multiscale Correlations of Herbs and Symptoms**   
Traditional Chinese medicine (TCM) exhibits remarkable therapeutic efficacy in disease treatment and healthcare through personalized herb prescriptions. However, current herb recommendation models inadequately capture the multiscale relations between herbs and clinical symptoms, particularly neglecting latent correlations at the chemicalmolecular scale. To address these limitations, we propose the Fusion of Multiscale Correlations of Herbs and Symptoms (FMCHS), an innovative framework that synergistically integrates molecular-scale chemical characteristics of herbs with clinical symptoms. The framework employs multi-relational graph transformer layers to generate enriched embeddings that preserve both structural and semantic features within herbs and symptoms. Through systematic incorporation of herb chemical profiles into node embeddings and implementation of attention-based feature fusion, FMCHS effectively utilizes multiscale correlations.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">2024.07 - 2024.12</div><img src='images/Temporally Relevant Images.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
**Multimodal Classification of Temporally Relevant Images Using Large Pretrained Models**   
Temporally relevant images are visual representations that capture and convey information directly tied to specific points or periods in time. These images may exhibit gradual transformations in appearance, texture, or other visual cues that are challenging for traditional classification algorithms to recognize. To more accurately capture the features of temporally relevant images, we introduce spectral data corresponding to these images and propose a multimodal image classification method. The proposed approach leverages the expert knowledge of the large language model
(i.e. Claude-3.5, GPT-4o) to guide a grounded vision language model and a segment anything model for zero-shot object detection and image segmentation.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">2024.01 - 2024.03</div><img src='images/fruit.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
**Optimizing Tropical Fruit Supply Chain Dynamics through Computer Vision-Driven Pricing Strategies**   
Remote participation in a project at the National University of Singapore Institute of Operations Research, which aims to optimize pricing strategies within the tropical fruit supply chain through the utilization of computer vision technology to expand profit margins.   
My primary responsibility involves the development and implementation of an advanced deep learning-based image analysis technique, designed to accurately predict the shelf life of tropical fruits.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">2023.09 - 2023.12</div><img src='images/SegMix1.png' alt="sym" width="50%"><img src='images/SegMix2.png' alt="sym" width="50%"></div></div>
<div class='paper-box-text' markdown="1">
**Noisy-Label Driven Weakly-Supervised Semantic Segmentation**      
In image classification, noisy labels are a recognized issue and subject of extensive research. Labeling in image segmentation is more error-prone and time-intensive. Many studies advocate for weakly-supervised methods, indicating segmentation can be efficiently performed using basic annotations like bounding boxes or scribbles. Such labels are inherently noisy; therefore, it is natural for us to apply the classical concept of noisy labels to the study of image segmentation tasks. We aim to introduce new insights and outcomes to the field by leveraging this approach.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">2023.07 - 2023.12</div><img src='images/malware.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
**Improving Few-shot Malware Classification with Multi-modal Supervision**   
Pioneered the integration of malware binary grayscale images with runtime API call sequencesas multimodal data, significantly improving classification accuracy.  
Managed the construction of private datasets, implemented classification algorithms, and authored the project proposal.
</div>
</div>
-->


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">2018.09 - 2019.09</div><img src='images/vex1.jpg' alt="sym" width="50%"><img src='images/vex2.jpg' alt="sym" width="50%"></div></div>
<div class='paper-box-text' markdown="1">
**VEX Robotics Competition**      
Led the school’s VEX Robotics club, responsible for programming and debugging of the robotic systems.  
Attained Gold Awards at China Zone Selections, the Asia Championships, Asia Open and the World Championships in the United States during the 2018 season.  
</div>
</div>


# 🎖 Honors and Awards
- *2023.06* Champion, 3rd Youth Campus Volleyball League of Sichuan Province.
- *2022.11* Second Prize, Asia-Pacific Undergraduate Mathematical Contest in Modeling. 
- *2022.06* Third Prize, 2th Youth Campus Volleyball League of Sichuan Province. 

# 📚 Academic Services
- **Conference Reviewer:** IJCNN 2024, ACL 2024, CaLM @NeurIPS 2024, ICLR 2025, AAAI 2026

- **Journal Reviewer:** IEEE Transactions on Neural Networks and Learning Systems(IEEE TNNLS)

# 🌏 Visitor Map
<script type="text/javascript" id="mapmyvisitors" src="//mapmyvisitors.com/map.js?d=7em4cMIIWlwnjcm-0tJhSO8vrChpSZvg-YeTEIOwS44&cl=ffffff&w=a"></script>

