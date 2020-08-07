# DevOps Design Doc

We use Heroku for deploying our frontend

We use a hosted standalone database as our backend (firebase(?))

## Flow

1. retrieve data (Python)
2. push to database on local machine (Flask)
3. generate static site with data from database (GatsbyJS)
4. push static site (paginated) to the web

This way we can deploy a static site with nearly dynamic data without having to pay for any additional hosting costs.