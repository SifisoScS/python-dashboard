# ✨ Beautiful Python Dashboard with Docker

A stunning interactive data visualization dashboard built with Flask, Plotly, and Docker.

## 🎯 Features

- **Interactive Charts**: Real-time sales analytics with Plotly
- **Beautiful UI**: Gradient design with smooth animations
- **Responsive**: Works on desktop and mobile
- **Dockerized**: Easy deployment with Docker
- **RESTful API**: JSON endpoints for data access

## 📁 Project Structure

```bash
python-dashboard/
├── Dockerfile
├── requirements.txt
├── app.py
├── templates/
│   └── index.html
└── static/ (optional for additional assets)
```

## 🚀 Quick Start

### Step 1: Create Project Structure

```bash
# Create a new directory
mkdir python-dashboard
cd python-dashboard

# Create subdirectories
mkdir templates
mkdir static
```

### Step 2: Create Files

Create the following files with the content provided in the artifacts:

1. `Dockerfile`
2. `requirements.txt`
3. `app.py`
4. `templates/index.html`

### Step 3: Build Docker Image

```bash
docker build -t python-dashboard .
```

This will:

- Pull Python 3.11 base image
- Install all dependencies
- Copy your application files
- Set up the environment

### Step 4: Run the Container

```bash
docker run -p 5000:5000 python-dashboard
```

Or run in detached mode:

```bash
docker run -d -p 5000:5000 --name my-dashboard python-dashboard
```

### Step 5: Access the Dashboard

Open your browser and navigate to:

```bash
http://localhost:5000
```

## 🎨 What You'll See

- **4 Stat Cards** with key metrics
- **Sales Performance Chart** - Animated line chart with sales trends
- **Revenue by Category** - Interactive pie chart
- **Sales Heatmap** - Day/Month correlation heatmap

## 🛠️ Docker Commands

```bash
# Build image
docker build -t python-dashboard .

# Run container
docker run -p 5000:5000 python-dashboard

# Run in background
docker run -d -p 5000:5000 --name dashboard python-dashboard

# Stop container
docker stop dashboard

# Remove container
docker rm dashboard

# View logs
docker logs dashboard

# List running containers
docker ps

# Access container shell
docker exec -it dashboard /bin/bash
```

## 🔧 Customization

### Change Port

Modify the `docker run` command:

```bash
docker run -p 8080:5000 python-dashboard
```

### Modify Data

Edit `generate_sample_data()` function in `app.py` to use your own data source.

### Update Styling

Modify the CSS in `templates/index.html` to match your brand colors.

### Add New Charts

1. Create a new chart function in `app.py`
2. Add it to the `/api/charts` endpoint
3. Render it in `index.html`

## 📊 API Endpoints

- `GET /` - Main dashboard
- `GET /api/charts` - JSON data for all charts
- `GET /health` - Health check endpoint

## 🐳 Docker Best Practices Used

✅ **Multi-layer caching** - Dependencies installed before copying code  
✅ **Slim base image** - python:3.11-slim for smaller size  
✅ **No cache pip installs** - Reduces image size  
✅ **Proper .dockerignore** - Excludes unnecessary files  
✅ **Non-root user** - Can be added for production  
✅ **Environment variables** - Flask configuration externalized  

## 🚀 Production Deployment

For production, consider:

1. **Use Gunicorn** (already in requirements.
txt):

   ```dockerfile
   CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "app:app"]
   ```

2. **Add .dockerignore**:

   ```bash
   __pycache__
   *.pyc
   *.pyo
   *.pyd
   .Python
   env/
   venv/
   .git
   .gitignore
   ```

3. **Environment Variables**:

   ```bash
   docker run -p 5000:5000 -e FLASK_ENV=production python-dashboard
   ```

## 🎓 Learning Points

This project demonstrates:

- Python Flask web framework
- Plotly for data visualization
- Docker containerization
- RESTful API design
- Responsive web design
- Animation and UX best practices

## 📝 Next Steps

- Add database integration (PostgreSQL/MongoDB)
- Implement user authentication
- Add real-time updates with WebSockets
- Create Docker Compose for multi-container setup
- Deploy to cloud (AWS, Azure, GCP)

## 🤝 Contributing

Feel free to fork, modify, and enhance this dashboard!

---

**Built with ❤️ using Python & Docker** 🐍🐳
