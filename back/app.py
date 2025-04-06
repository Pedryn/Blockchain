# app.py
from flask import Flask
from routes.users import users_bp
from routes.cryptos import cryptos_bp
from routes.transactions import transactions_bp
from routes.mining import mining_bp
import logging
from apscheduler.schedulers.background import BackgroundScheduler
from utils.simulate_volatility import simulate_volatility
from utils.simulate_activity import simulate_user_activity
from utils.check_blockchain import check_blockchain_integrity
from init_data import initialize_data

app = Flask(__name__)

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

for logger_name in ['apscheduler', 'apscheduler.scheduler', 'apscheduler.executors.default']:
    logging.getLogger(logger_name).setLevel(logging.WARNING)
    logging.getLogger(logger_name).propagate = False

initialize_data()

# Registrar blueprints
app.register_blueprint(users_bp)
app.register_blueprint(cryptos_bp)
app.register_blueprint(transactions_bp)
app.register_blueprint(mining_bp)

if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(simulate_volatility, 'interval', minutes=1)
    scheduler.add_job(simulate_user_activity, 'interval', minutes=0.20)
    scheduler.add_job(check_blockchain_integrity, 'interval', minutes=1.5)

    scheduler.start()

    app.run(debug=True, use_reloader=False)
