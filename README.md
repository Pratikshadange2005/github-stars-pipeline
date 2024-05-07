# GitHub Gems: Driving Open-Source Investments With Data

Welcome to the GitHub Gems project! This project hosts a data analytics pipeline that enables smarter investment decisions by measuring the popularity of open-source repos on Github.

## Project Overview

The goal of this project is to develop an efficient data pipeline that streamlines analytics, reduces manual effort, and enables deeper insights into the open-source ecosystem on GitHub. By leveraging modern data tools and best practices, such as dbt (data build tool) and Airflow, we aim to create a scalable and reliable solution for data-driven decision-making.

## Getting Started

To get started with the GitHub Gems project, follow these steps (click on the
links for guides):

### Set up your IDE

> ℹ️ Skip some steps if you're already set!
>
> If you already have git, VSCode, and/or Python installed, just skip the corresponding step(s).

1. If you don't already use git, [install it here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

2. If you don't have a coding editor installed, [install VSCode](https://code.visualstudio.com/download). After that, [install the Python and Python extension](https://code.visualstudio.com/docs/languages/python#_install-python-and-the-python-extension).

3. Make sure you have Python 3 installed (or [install it here](https://www.python.org/downloads/)).

### Create your personal repo

1. [Create a new repo](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository) in your Github account and name it `github-stars-pipeline`.

2. Clone this repo.

```bash
git clone https://github.com/edsioufi/github-stars-pipeline.git
```


3. Point your local clone to your own remote (so that you can modify your copy of the repo, not the template). Make sure you repalce `{your_github_username}` with the corresponding value.

```bash
cd github-stars-pipeline
git remote set-url origin https://github.com/{your_github_username}/github-stars-pipeline.git
```

4. Push to your new github repo.

```bash
git push origin master
```

### Set up your python environment and DuckDB

1. Create a python virtual environment for your repo:

```bash
python -m venv venv
source venv/bin/activate
```

2. [Install DuckDB](https://duckdb.org/docs/installation/?version=stable&environment=python) (make sure you select the Python option), your first python dependency.

> ℹ️ You might have to install additional dependencies if you're on Windows.

3. [Install DBeaver](https://duckdb.org/docs/guides/sql_editors/dbeaver.html) to explore DuckDB.

4. Create a new git branch:
```bash
git checkout -b add_duck_db
```

5. Add your newly installed packages to your requirements file:
```bash
pip freeze > requirements.txt
```

6. Commit and push:
```bash
git add --all
git commit
git push origin -u add_duck_db
```

7. [Create a Pull Request (PR)](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request#creating-the-pull-request) in Github.

8. [Merge your first PR](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/merging-a-pull-request#merging-a-pull-request).

### Project Goal: The GitHub Gems helps you track and analyze GitHub repositories. It's great for spotting fast-growing projects and digging into specific repos using key metrics like star and commit growth rates.

## Features
•	Identify Fast-Growing Repositories:  Pinpoint repositories that are rapidly gaining stars or commits to highlight emerging trends or popular projects.
•	Analyze Specific Repository:  Get detailed insights into any repository of interest.
Key Metrics:
•	Analyze growth rate of stars and commits to gauge repository popularity and activity.
•	Daily Updates: Keep data fresh with daily updates, ensuring up-to-date insights.
•	SQL Database Output: Data is delivered in an SQL database format, facilitating easy querying and integration with other systems.
•	Update Frequency: The data is updated daily, ensuring that the insights provided are up-to-date and relevant.


## Important Metrics and Data Points
1. Growth Rate of Stars: Measures how quickly a repository is gaining stars over time.
2. Growth Rate of Commits: Measures how quickly a repository is receiving new commits.
3. Total Stars: The total number of stars a repository has received.
4. Total Commits: The total number of commits in a repository.
   
## Data Source
The data is sourced from [GH Archive] (https://www.gharchive.org/). GH Archive was chosen because it provides hourly snapshots of GitHub activity, offering a good balance between freshness and simplicity of data loading.
