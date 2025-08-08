# 📝 Task Management API

A simple yet powerful RESTful API for task management built with **FastAPI** and **Pydantic**. This lightweight API provides full CRUD operations for managing tasks with an elegant in-memory storage solution.

## ✨ Features

- 🚀 **Fast & Modern**: Built with FastAPI for high performance and automatic API documentation
- 📋 **Complete CRUD Operations**: Create, Read, Update, and Delete tasks seamlessly  
- 🔍 **Task Filtering**: Retrieve all tasks or find specific tasks by ID
- ✅ **Data Validation**: Powered by Pydantic models for robust data validation
- 📊 **Auto Documentation**: Interactive API docs with Swagger UI
- 🎯 **Simple & Clean**: Minimalist architecture that's easy to understand and extend

## 🏗️ Current Architecture

### Project Structure
```
📦 Task Management API
├── 📁 models/
│   └── task.py          # Task data model
├── 📁 crud/
│   └── task_crud.py     # CRUD operations
└── 📁 routes/
    └── task_routes.py   # API endpoints
```

### Data Model
The `Task` model includes:
- **id**: Unique identifier (integer)
- **title**: Task title (string)
- **body**: Task description (string) 
- **completed**: Completion status (boolean, defaults to False)

## 🚀 Current Implementation

### Core Components

#### 1. **Task Model** (`models/task.py`)
```python
from pydantic import BaseModel

class Task(BaseModel):
    id: int
    title: str
    body: str
    completed: bool = False
```
Pydantic model ensuring type safety and automatic validation for all task data.

#### 2. **CRUD Operations** (`crud/task_crud.py`)
- **In-Memory Storage**: Tasks stored in a Python list for simplicity
- **Full CRUD Support**: Create, read, update, and delete operations
- **Error Handling**: Proper error responses for missing tasks
- **Data Persistence**: Maintains tasks during runtime session

#### 3. **API Routes** (`routes/task_routes.py`)
Clean, RESTful endpoints with intuitive URL patterns:

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Welcome message |
| `GET` | `/all` | Retrieve all tasks |
| `GET` | `/tasks/{id}` | Get specific task by ID |
| `POST` | `/new` | Create a new task |
| `PUT` | `/task/{id}` | Update existing task |
| `DELETE` | `/task/{id}` | Delete task by ID |

## 📋 API Usage Examples

### Create a Task
```bash
POST /new
{
  "id": 1,
  "title": "Complete project documentation",
  "body": "Write comprehensive README and API docs",
  "completed": false
}
```

### Get All Tasks
```bash
GET /all
```

### Get Task by ID
```bash
GET /tasks/1
```

### Update Task
```bash
PUT /task/1
{
  "id": 1,
  "title": "Complete project documentation",
  "body": "Write comprehensive README and API docs",
  "completed": true
}
```

### Delete Task
```bash
DELETE /task/1
```

## 🛠️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd task-management-api
   ```

2. **Install dependencies**
   ```bash
   pip install fastapi uvicorn pydantic
   ```

3. **Run the application**
   ```bash
   uvicorn main:app --reload
   ```

4. **Access the API**
   - API Base URL: `http://localhost:8000`
   - Interactive Docs: `http://localhost:8000/docs`
   - ReDoc Documentation: `http://localhost:8000/redoc`

## 🔮 Future Roadmap

### 🗄️ Database Integration
- **PostgreSQL/MySQL Support**: Replace in-memory storage with persistent database
- **Database Models**: Implement SQLAlchemy ORM models
- **Connection Pooling**: Optimize database connections for better performance
- **Data Migrations**: Version-controlled database schema changes

### 🛡️ Enhanced Validation & Security
- **Advanced Validation Rules**: Custom validators for task fields
- **Authentication & Authorization**: JWT-based user authentication
- **Rate Limiting**: API request throttling for better security
- **Input Sanitization**: Enhanced data cleaning and validation

### 🖥️ Frontend Integration
- **React/Vue.js Dashboard**: Modern web interface for task management
- **Real-time Updates**: WebSocket integration for live task updates  
- **Mobile App**: React Native or Flutter mobile application
- **API Client Libraries**: SDKs for popular programming languages

### 📈 Advanced Features
- **Task Categories & Tags**: Organize tasks with labels and categories
- **Due Dates & Reminders**: Time-based task management
- **Task Dependencies**: Link related tasks together
- **User Management**: Multi-user support with role-based permissions
- **Analytics Dashboard**: Task completion metrics and reporting
- **File Attachments**: Upload and manage task-related files

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **FastAPI** for the incredible web framework
- **Pydantic** for powerful data validation
- **Python Community** for continuous inspiration

---

<div align="center">

**Built with ❤️ using FastAPI**

[⭐ Star this repo](https://github.com/yourusername/task-management-api) | [🐛 Report Bug](https://github.com/yourusername/task-management-api/issues) | [✨ Request Feature](https://github.com/yourusername/task-management-api/issues)

</div>
