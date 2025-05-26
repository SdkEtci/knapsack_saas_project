# 🎒 Knapsack SaaS Application

This project is a Software as a Service (SaaS) application designed to solve the Knapsack problem and visualize the results. Built with Flask for the backend and Chart.js for the frontend, it provides an interactive interface for users to input data and observe optimized solutions.

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/SdkEtci/knapsack_saas_project.git
cd knapsack_saas_project
```

### 2. Set Up the Backend

Navigate to the `backend` directory and create a virtual environment:

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
```

Install the required packages:

```bash
pip install flask flask-cors pandas numpy
```

### 3. Run the Application

Start the Flask application:

```bash
python app.py
```

By default, the application will be accessible at `http://localhost:5000`.

## 🌐 Deployment on Railway

To deploy this application on [Railway](https://railway.app), follow these steps:

1. **Connect to GitHub**: Push your project to a GitHub repository if you haven't already.

2. **Create a New Project on Railway**:
   - Log in to your Railway account.
   - Click on "New Project" and select "Deploy from GitHub Repo".
   - Choose your `knapsack_saas_project` repository.

3. **Configure Environment Variables**:
   - In the Railway dashboard, navigate to your project's settings.
   - Add any necessary environment variables required by your application.

4. **Set Up the Start Command**:
   - In the "Deploy" settings, specify the start command for your application. For example:

   ```bash
   python app.py
   ```

5. **Deploy the Application**:
   - Click on "Deploy" to start the deployment process.
   - Once deployed, Railway will provide a public URL to access your application.

For more detailed guidance on deploying applications with Railway, refer to their [official documentation](https://docs.railway.com/guides/deployments).

## 🌐 Live Demo

You can access the live version of this application deployed on Railway at: https://knapsacksaasproject-production.up.railway.app/

## 📊 Features

- **Dynamic Visualization**: Input your own datasets and observe how the Knapsack problem is solved and visualized in real-time.
- **RESTful API**: Interact with the backend through a RESTful API built with Flask.
- **Modular Design**: Clear separation between backend and frontend components for easier maintenance and scalability.

## 🛠 Technologies Used

- **Backend**: Python, Flask, Flask-CORS, Pandas, NumPy
- **Frontend**: HTML
- **Deployment**: Railway

## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## 📄 License

This project is licensed under the [MIT License](LICENSE).
