# UltraBoost Dashboard
UltraBoost Dashboard is an open-source application designed to assist in the creation, backtesting, and optimization of a wide variety of algorithmic trading strategies. Once refined, these strategies can be deployed as [UltraBoost](https://github.com/MohamedMagdy90/UltraGrid) bot instances in live trading modes, providing a seamless transition from strategy formulation to actual trading execution.
**Powered by BoostNova**
## Features
- **Bot Orchestration**: Deploy and manage multiple instances of UltraBoost
- **Strategy Backtesting and Optimization**: Evaluate the performance of your strategies against historical data and optimize them with Optuna
- **One-Click Deployment**: Seamlessly deploy your strategies as UltraBoost instances for paper or live trading.
- **Performance Analysis Monitoring**: Monitor and analyze the performance of your deployed strategies.
- **Credential Management**: Create and manage separate accounts for API keys
## Installation
### Using Docker (Recommended)
The easiest way to run UltraBoost Dashboard is using Docker:
```bash
git clone https://github.com/MohamedMagdy90/ultraboost-dashboard.git
cd ultraboost-dashboard
docker-compose up -d
```
### From Source
If you are a developer and want to make changes to the code:
1. **Install Dependencies**:
   - Docker Engine
   - Miniconda or Anaconda
2. **Clone Repository and Navigate to Directory**:
    ```bash
    git clone https://github.com/MohamedMagdy90/ultraboost-dashboard.git
    cd ultraboost-dashboard
    ```
3. **Create Conda Environment and Install Dependencies**:
    ```bash
    make install
    ```
4. **Activate the Isolated 'conda' Environment**:
    ```bash
    conda activate ultraboost-dashboard
    ```
5. **Start the Dashboard**:
    ```bash
    make run
    ```
For more detailed instructions on how to install and update the dashboard, refer to [INSTALLATION.md](INSTALLATION.md).
## Authentication
Authentication is disabled by default. To enable Dashboard Authentication please follow the steps below:
**Set Credentials (Optional):**
The dashboard uses `admin` and `abc` as the default username and password respectively. It's strongly recommended to change these credentials for enhanced security.:
- Navigate to the `ultraboost-dashboard` folder and open the `credentials.yml` file.
- Add or modify the current username / password and save the changes afterward
  ```
  credentials:
    usernames:
      admin:
        email: admin@boostnova.io
        name: Admin User
        logged_in: False
        password: abc
  cookie:
    expiry_days: 0
    key: some_signature_key # Must be string
    name: some_cookie_name
  pre-authorized:
    emails:
    - admin@boostnova.io
  ```
### Docker
- Ensure the dashboard container is not running.
- Open the `docker-compose.yml` file using a text editor.
- Locate the environment variable `AUTH_SYSTEM_ENABLED` under the dashboard service configuration.
  ```
  services:
  dashboard:
    container_name: ultraboost-dashboard
    image: ultraboost/dashboard:latest
    ports:
      - "8501:8501"
    environment:
        - AUTH_SYSTEM_ENABLED=True
        - BACKEND_API_HOST=backend-api
        - BACKEND_API_PORT=8000
  ```
- Change the value of `AUTH_SYSTEM_ENABLED` from `False` to `True`.
- Save the changes to the `docker-compose.yml` file.
- Relaunch Dashboard by running `docker-compose up -d`
### Source
- Open the `CONFIG.py` file located in the dashboard root folder
- Locate the line `AUTH_SYSTEM_ENABLED = os.getenv("AUTH_SYSTEM_ENABLED", "False").lower() in ("true", "1", "t")`.
  ```
  CERTIFIED_EXCHANGES = ["ascendex", "binance", "bybit", "gate.io", "hitbtc", "huobi", "kucoin", "okx", "gateway"]
  CERTIFIED_STRATEGIES = ["xemm", "cross exchange market making", "pmm", "pure market making"]
  AUTH_SYSTEM_ENABLED = os.getenv("AUTH_SYSTEM_ENABLED", "False").lower() in ("true", "1", "t")
  BACKEND_API_HOST = os.getenv("BACKEND_API_HOST", "127.0.0.1")
  ```
- Change the value from `False` to `True` to enable dashboard authentication.
- Save the CONFIG.py file.
- Relaunch dashboard by running `make run`
### Known Issues
- Refreshing the browser window may log you out and display the login screen again. This is a known issue that might be addressed in future updates.
## Contributing and Feedback
We welcome contributions from the community. Please read our [contributing guidelines](CONTRIBUTING.md) to get started.
## License
UltraBoost Dashboard is licensed under the Apache License, Version 2.0. See [LICENSE](LICENSE) for more details.
---
**UltraBoost Dashboard** - Built with BoostNova