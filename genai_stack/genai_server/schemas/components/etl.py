from sqlalchemy import Column, Integer, JSON

from genai_stack.genai_server.schemas.base_schemas import TimeStampedSchema


class ETLJob(TimeStampedSchema):
    """
    SQL Schema for Stack Sessions.

    Args:
        stack_id : Integer
        meta_data : JSON
    """

    __tablename__ = "etl_jobs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    stack_id = Column(Integer, nullable=False)
    meta_data = Column(JSON)
