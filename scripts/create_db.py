from app.database import engine
from app.models.models import Base



# Create all tables in the database
Base.metadata.create_all(bind=engine)
