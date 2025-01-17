# sa-law-db
A law database for student association, which written in React and Flask + SQLAlchemy.

## Introduction
The Student Association Law Database System aims to provide students with a convenient platform for legal regulation inquiries, enhancing information transparency and student understanding of campus regulations. The system includes law management, search functionality, and version revision records, along with a dedicated admin interface for administrators.

## Features
- Law Query and Display:
  - Support viewing by chapters and articles.
  - View historical revision records.
- Search Functionality:
  - Search by law name or article keywords.
- Admin Interface:
  - Add and edit legal content.
  - Handle complex article structures (e.g., "Section 1", "Section 2").
  - Record revision history.

## Technical Architecture
- **Backend**: Flask + SQLAlchemy
- **Frontend**: React
- **Database**: MariaDB
- **System Requirements**:
  - Operating System: Linux/Windows/MacOS
  - Python Version: 3.9+
  - Node.js Version: 16+

## Installation and Execution
### Environment Setup
1. Ensure Python and Node.js are installed.
2. Install and start MariaDB.

### Installation Steps
```bash
# Clone the repository
git clone https://github.com/your-repo/student-law-database.git
cd student-law-database

# Install backend dependencies
cd backend
pip install -r requirements.txt

# Install frontend dependencies
cd ../frontend
npm install
```

### Start the Project
```bash
# Start the backend
cd backend
python app.py

# Start the frontend
cd ../frontend
npm start
```

## Usage
1. Go to http://localhost:3000 to browse the frontend interface.
2. Use the search box to enter the law name or article keywords for inquiry.
3. If you have admin permissions, log in to access the admin interface for law management.

## Testing
```bash
# Backend tests
cd backend
pytest

# Frontend tests
cd frontend
npm test
```

## Deployment
1. Configure the server environment. It is recommended to use Nginx and Gunicorn for backend deployment.
2. The frontend can be packaged into static files and served via Nginx.
3. Configure database connections and ensure MariaDB is running properly.

## Contribution Guidelines
1. Fork this repository and create a new branch.
2. Submit modifications and send a Pull Request.
3. Ensure the code passes all tests.

## License
This project is licensed under the MIT License. See [LICENSE](./LICENSE) for details.

## Contact Information
- Project Maintainer: Bo-Jun "Kazan" Su
- Email: me@kazan.tw
- GitHub: [kazanTW](https://github.com/kazanTW)