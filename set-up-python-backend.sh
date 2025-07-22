mkdir -p minelab_backend/app/{models,schemas,routes,services}
mkdir -p minelab_backend/tests
mkdir -p minelab_backend/scripts
mkdir -p minelab_backend/alembic

touch minelab_backend/app/__init__.py
touch minelab_backend/app/main.py
touch minelab_backend/app/config.py
touch minelab_backend/app/database.py

# Models
touch minelab_backend/app/models/__init__.py
touch minelab_backend/app/models/user.py
touch minelab_backend/app/models/plugin.py
touch minelab_backend/app/models/license.py
touch minelab_backend/app/models/payment.py

# Schemas
touch minelab_backend/app/schemas/user.py
touch minelab_backend/app/schemas/plugin.py
touch minelab_backend/app/schemas/license.py
touch minelab_backend/app/schemas/payment.py

# Routes
touch minelab_backend/app/routes/__init__.py
touch minelab_backend/app/routes/auth.py
touch minelab_backend/app/routes/licenses.py
touch minelab_backend/app/routes/plugins.py
touch minelab_backend/app/routes/payments.py
touch minelab_backend/app/routes/admin.py

# Services
touch minelab_backend/app/services/license_checker.py
touch minelab_backend/app/services/payment_handler.py
touch minelab_backend/app/services/email_sender.py

# Autres
touch minelab_backend/.env
touch minelab_backend/requirements.txt
touch minelab_backend/README.md
