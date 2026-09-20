<p align="center">
  <img src="https://readme-typing-svg.demolab.com/?font=Fira+Code&weight=500&size=26&duration=3000&pause=1000&color=58A6FF&center=true&vCenter=true&width=650&lines=Hi%2C+I%27m+D%27Andre+%F0%9F%91%8B;Data+%26+Analytics+Engineer;I+build+pipelines+that+don%27t+fall+over;ETL+by+day%2C+ELT+when+the+warehouse+can+take+it" alt="Typing SVG" />
</p>

<p align="center">
  <a href="https://dandremcneish.github.io"><img src="https://img.shields.io/badge/Portfolio-dandremcneish.github.io-1f5fbf?style=for-the-badge" alt="Portfolio"></a>
  <a href="https://www.linkedin.com/in/dandre-mcneish/"><img src="https://img.shields.io/badge/LinkedIn-Connect-0a66c2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
  <a href="https://gitlab.com/dmcnei29"><img src="https://img.shields.io/badge/GitLab-Projects-fc6d26?style=for-the-badge&logo=gitlab&logoColor=white" alt="GitLab"></a>
</p>

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=dandremcneish&color=58a6ff&style=for-the-badge&label=PROFILE+VIEWS" alt="Profile views" />
</p>

**Live, interactive portfolio (real charts, real data, click-through demos): [dandremcneish.github.io](https://dandremcneish.github.io)**

I just graduated with a Master's in Data Analytics and Data Engineering from Western Governors University, on top of a Bachelor's in Data Analytics and Artificial Intelligence and an Associate's in Information Technology. I like building things that hold up past the first run: schemas that stay correct under real queries, pipelines with data-quality checks baked in rather than bolted on, and models that get validated before anyone trusts their output. My background's in technical support and IT operations, which is probably why I lean toward monitoring and reproducibility over getting something to work once and calling it done.

<p align="center">
  <code>Raw Data</code> ➜ 🧹 <code>Clean</code> ➜ 🔧 <code>Transform</code> ➜ 📦 <code>Load</code> ➜ ✅ <code>Validate</code> ➜ 📊 <code>Decide</code>
</p>

<br>

### 🛠️ What I work with

**Data Engineering:** Apache Airflow &middot; Python &middot; SQL &middot; ETL/ELT &middot; AWS Redshift &middot; AWS Glue &middot; DVC &middot; MLflow

**Cloud &amp; Platforms:** Google Cloud Platform &middot; BigQuery &middot; AWS &middot; Docker &middot; Azure &middot; GitLab CI/CD

**Analytics &amp; Modeling:** Linear/Logistic Regression &middot; PCA &middot; Hypothesis Testing &middot; Market Basket Analysis &middot; Tableau

<br>

### 📊 GitHub stats

<p align="center">
  <img src="https://github-readme-streak-stats.herokuapp.com/?user=dandremcneish&theme=tokyonight&hide_border=true" alt="GitHub streak" />
</p>

<br>

### 🐍 A snake, eating my own contribution graph

Because a static profile is boring. This repo has a scheduled GitHub Action that regenerates it daily.

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/dandremcneish/dandremcneish/output/github-contribution-grid-snake-dark.svg" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/dandremcneish/dandremcneish/output/github-contribution-grid-snake.svg" />
    <img alt="A snake animation eating my GitHub contribution graph" src="https://raw.githubusercontent.com/dandremcneish/dandremcneish/output/github-contribution-grid-snake.svg" />
  </picture>
</p>

<br>

### 🎲 Quick data riddle

<details>
<summary>Click to play: what does this query return?</summary>
<br>

```sql
SELECT customer_id, COUNT(*) AS orders
FROM orders
GROUP BY customer_id
HAVING COUNT(*) > 1
ORDER BY orders DESC
LIMIT 1;
```

Every customer with more than one order, ranked by order count, trimmed down to just the single busiest one. It's the classic "who's my most loyal customer" query, and it's usually the first thing I write against a new orders table before touching anything fancier.

</details>

<br>

### 🚀 Featured projects

| Project | Description | Link |
|---|---|---|
| Data Pipelines with Airflow | Custom Airflow operators and a DAG staging S3 data into Redshift with automated data-quality checks. Verified Udacity certificate. | [Code](https://github.com/dandremcneish/data-pipelines-with-airflow) |
| Interactive Portfolio | This profile's companion site: dark mode, real regression/PCA charts built from real data, an animated Airflow DAG walkthrough. | [Live site](https://dandremcneish.github.io) &middot; [Code](https://github.com/dandremcneish/dandremcneish.github.io) |
| ML Experiment Tracking Pipeline | Reproducible flight-delay prediction pipeline versioned with DVC, tracked with MLflow, deployed through GitLab CI/CD. | GitLab (hosted environment) |
| Program Implementation Automation | Python program analyzing an organizational dataset to evaluate program effectiveness. | [GitLab](https://gitlab.com/dmcnei29/qkn1-task-2-program-implementation) |

### ✅ Verified credentials

- WGU Data Analytics Professional Certificate
- WGU Data Engineering Professional Specialization
- Udacity: Data Pipelines with Airflow (Nanodegree)
- Udacity: Big Data Architecture at Scale (Nanodegree)
- CompTIA Competency in AI Agent Essentials (Credential ID 6-3C6-DTEWP)

### 📬 Get in touch

📧 dmcneish365@gmail.com &nbsp;|&nbsp; 💼 [LinkedIn](https://www.linkedin.com/in/dandre-mcneish/) &nbsp;|&nbsp; 🌐 [Portfolio](https://dandremcneish.github.io)
