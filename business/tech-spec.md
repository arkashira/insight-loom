```markdown
# Tech Spec: insight-loom

## Stack
- **Language**: Python (FastAPI)
- **Frontend**: React.js
- **Database**: PostgreSQL
- **Hosting**: AWS (free-tier-first: EC2, RDS, S3)
- **Containerization**: Docker
- **Orchestration**: Kubernetes (EKS)

## Hosting
- **AWS Free Tier**:
  - **EC2**: t2.micro instance for the backend
  - **RDS**: db.t2.micro instance for PostgreSQL
  - **S3**: Standard storage for static assets
- **CI/CD**: AWS CodePipeline

## Data Model
### Tables/Collections
1. **Users**
   - `id`: UUID (primary key)
   - `email`: String (unique)
   - `password_hash`: String
   - `created_at`: Timestamp
   - `updated_at`: Timestamp

2. **Teams**
   - `id`: UUID (primary key)
   - `name`: String
   - `created_by`: UUID (foreign key to Users)
   - `created_at`: Timestamp
   - `updated_at`: Timestamp

3. **Projects**
   - `id`: UUID (primary key)
   - `name`: String
   - `team_id`: UUID (foreign key to Teams)
   - `created_by`: UUID (foreign key to Users)
   - `created_at`: Timestamp
   - `updated_at`: Timestamp

4. **InformationSources**
   - `id`: UUID (primary key)
   - `name`: String
   - `type`: String (e.g., document, email, meeting notes)
   - `content`: Text
   - `project_id`: UUID (foreign key to Projects)
   - `created_by`: UUID (foreign key to Users)
   - `created_at`: Timestamp
   - `updated_at`: Timestamp

5. **Insights**
   - `id`: UUID (primary key)
   - `title`: String
   - `content`: Text
   - `project_id`: UUID (foreign key to Projects)
   - `created_by`: UUID (foreign key to Users)
   - `created_at`: Timestamp
   - `updated_at`: Timestamp

6. **Recommendations**
   - `id`: UUID (primary key)
   - `content`: Text
   - `insight_id`: UUID (foreign key to Insights)
   - `created_by`: UUID (foreign key to Users)
   - `created_at`: Timestamp
   - `updated_at`: Timestamp

## API Surface
1. **User Management**
   - `POST /api/users/register`: Register a new user
   - `POST /api/users/login`: Login a user
   - `GET /api/users/{user_id}`: Get user details
   - `PUT /api/users/{user_id}`: Update user details

2. **Team Management**
   - `POST /api/teams`: Create a new team
   - `GET /api/teams/{team_id}`: Get team details
   - `PUT /api/teams/{team_id}`: Update team details
   - `DELETE /api/teams/{team_id}`: Delete a team

3. **Project Management**
   - `POST /api/projects`: Create a new project
   - `GET /api/projects/{project_id}`: Get project details
   - `PUT /api/projects/{project_id}`: Update project details
   - `DELETE /api/projects/{project_id}`: Delete a project

4. **Information Source Management**
   - `POST /api/information-sources`: Add a new information source
   - `GET /api/information-sources/{source_id}`: Get information source details
   - `PUT /api/information-sources/{source_id}`: Update information source details
   - `DELETE /api/information-sources/{source_id}`: Delete an information source

5. **Insight Management**
   - `POST /api/insights`: Create a new insight
   - `GET /api/insights/{insight_id}`: Get insight details
   - `PUT /api/insights/{insight_id}`: Update insight details
   - `DELETE /api/insights/{insight_id}`: Delete an insight

6. **Recommendation Management**
   - `POST /api/recommendations`: Create a new recommendation
   - `GET /api/recommendations/{recommendation_id}`: Get recommendation details
   - `PUT /api/recommendations/{recommendation_id}`: Update recommendation details
   - `DELETE /api/recommendations/{recommendation_id}`: Delete a recommendation

## Security Model
- **Authentication**: JWT (JSON Web Tokens)
- **Authorization**: Role-Based Access Control (RBAC)
- **Secrets Management**: AWS Secrets Manager
- **IAM**: AWS Identity and Access Management for resource access control

## Observability
- **Logs**: AWS CloudWatch Logs
- **Metrics**: AWS CloudWatch Metrics
- **Traces**: AWS X-Ray

## Build/CI
- **Build Tool**: Docker
- **CI/CD Pipeline**: AWS CodePipeline
  - **Source Stage**: AWS CodeCommit
  - **Build Stage**: AWS CodeBuild
  - **Deploy Stage**: AWS Elastic Beanstalk
```