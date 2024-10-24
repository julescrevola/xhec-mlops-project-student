"""Pydantic models for the web service."""

from pydantic import BaseModel


class AbaloneData(BaseModel):
    """Pydantic model for the input data to the web service."""

    Length: float
    Diameter: float
    Height: float
    Whole_weight: float
    Shucked_weight: float
    Viscera_weight: float
    Shell_weight: float
    Sex: str
