## Project Goal: The GitHub Gems helps you track and analyze GitHub repositories. It's great for spotting fast-growing projects and digging into specific repos using key metrics like star and commit growth rates.

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

## Models
Our GitHub Gems project utilizes the Kimball methodology, specifically employing a star schema to organize data into dimensional models. This structure allows users to easily query and analyze GitHub activity related to repository stars and commits.

### Fact and Dimension Tables
#### Fact Tables
•	fact_stars: Tracks star events on repositories.
            •	event_id: Unique identifier for the star event.
            •	repo_id: Repository ID.
            •	user_id: User ID who starred the repository.
            •	event_date: Date of the star event.
•	fact_commits: Records commit events in repositories.
            •	event_id: Unique identifier for the commit event.
            •	repo_id: Repository ID.
            •	user_id: User ID who made the commit.
            •	event_date: Date of the commit.
#### Dimension Tables
•	dim_repositories: Information about repositories.
            •	repo_id: Unique repository identifier.
            •	repo_name: Name of the repository.
            •	owner_login: Repository owner's username.
•	dim_users: User details.
            •	user_id: Unique user identifier.
            •	login: Username of the user.

## Sample Queries
Here are a few example queries to help you get started with analyzing the data:

1. Count of Stars by Repository:
```sql
SELECT r.repo_name,
COUNT(*) AS star_count FROM fact_stars
AS s JOIN dim_repositories AS r
ON s.repo_id = r.repo_id
GROUP BY r.repo_name
ORDER BY star_count DESC;
``` 

2. Commits Per User in a Specific Repository:
```sql
SELECT u.login, COUNT(*) AS commit_count
FROM fact_commits AS c JOIN dim_users AS u
ON c.user_id = u.user_id
WHERE c.repo_id = 12345 -- Replace 12345 with the actual repo_id
GROUP BY u.login
ORDER BY commit_count DESC;
```

3. Final Aggregated Fact Table:

```sql
SELECT month, yoy_growth
FROM fact_repo_stars_monthly
WHERE repo_name = "plotly/plotly.py";
```





