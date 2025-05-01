# 📘 Mr. Tasker - Azure Foundry Agent

> A real estate agent that connects with Azure Logic Apps using OpenAPI 3.0 schema.

---

## 🧠 Table of Contents

- 🚀 [Dependencies](#-dependencies)
- 🛠️ [Setup & Usage](#️-setup--usage)
- 🖥️ [Azure CLI Authentication](#️-azure-cli-authentication)
- 🤖 [Creating Your Agent](#-creating-your-agent)
- 💬 [Interacting with the Agent](#-interacting-with-the-agent)
- 👨‍💻 [Author](#-author)

---

## 🚀 Dependencies

To get started with the project, you'll need to install the following Python packages:

- `fastapi==0.115.12`
- `uvicorn==0.34.2`
- `azure-ai-projects`
- `azure-identity`

Install the dependencies by running the following command in your terminal:

pip install fastapi==0.115.12 uvicorn==0.34.2 azure-ai-projects azure-identity

Alternatively, if you have a `requirements.txt` file, simply use:

pip install -r requirements.txt

---

## 🛠️ Setup & Usage

### 1. Install Python

Ensure that **Python 3.12.5** (or a compatible version) is installed on your system. If you don’t have it, download the latest version from the official [Python website](https://www.python.org/downloads/).

### 2. Install Dependencies

Once Python is installed, navigate to your project directory in the terminal and install the required dependencies using `pip`:

pip install -r requirements.txt

### 3. Check Python Version

To verify that Python is installed correctly, you can check the version by running:

python --version

It should display **Python 3.12.5** (or your installed version).

---

## 🖥️ Azure CLI Authentication

To authenticate with Azure and access the Azure Foundry SDK, follow these steps:

1. **Install Azure CLI**  
   If you don't have the Azure CLI installed, you can follow the official [installation guide](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli) to set it up.

2. **Log in to Azure**  
   Once the Azure CLI is installed, open your terminal and log in with the following command:

   az login

   This will prompt you to authenticate via your browser. After logging in, you will be ready to use the Azure SDK.

---

## 🤖 Creating Your Agent

Once you're authenticated, follow these steps to create and configure your agent:

1. **Run the `createAgent` function**  
   This will initialize your agent in the Azure Foundry environment.

2. **Customization**  
   You can customize:

   - **Agent Name**: Define a unique name for your agent.
   - **Agent Instructions**: Specify the instructions or tasks that your agent will handle.
   - **OpenAPI 3.0 Schema**: Provide the schema URL or file that defines the API endpoints your agent will interact with.

3. **Prerequisites**  
   Ensure that your agent implementation is already set up and available in **Azure AI Foundry**.

---

## 💬 Interacting with the Agent

To interact with your deployed agent, follow these steps:

1. **Run the local server**  
   In your terminal, execute the following command to start a FastAPI server using the `app.py` script:

   uvicorn app:app

2. **Configuration**  
   Before running the command, make sure you:

   - Update the **Azure connection string** with your credentials.
   - Set the correct **Agent ID** in the script.

3. **Access the Agent API**  
   Once the server is running, open your browser and visit `http://127.0.0.1:8000`. This will open the Swagger UI, where you can interact with your agent and test the API endpoints.

---

## 👨‍💻 Author

**Eng. Estuardo Valenzuela**  
AI Developer & Cloud Solutions Engineer

---

Happy coding! 🚀
