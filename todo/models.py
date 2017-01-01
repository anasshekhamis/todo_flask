#
# For simplicity, and because there is only task model, I created this as a place for models.
# In advanced and more practical case, models should have their own package module.
#

import datetime

from todo import db

class Task(db.Model):
    """Task Model"""
    # Preferably, the table name is plural
    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)

    # Represents what needs to be done
    title = db.Column(db.String(200))

    # Task is active (not done)
    active = db.Column(db.Boolean, default=True)

    # Keep track of task create time
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)

    # Keep track of task update time
    updated_at = db.Column(
        db.DateTime,
        default=datetime.datetime.now,
        onupdate=datetime.datetime.now
    )