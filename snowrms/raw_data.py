from sqlalchemy import String, TIMESTAMP, Numeric, Text
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from typing import Optional
from datetime import datetime

class Base(DeclarativeBase):
    pass

class WeatherData(Base):
    __tablename__ = 'wx'
    
    site_code: Mapped[str] = mapped_column(String(15), primary_key=True)
    date_time: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), primary_key=True)
    air_temp: Mapped[Optional[float]] = mapped_column(Numeric)
    relative_humidity: Mapped[Optional[float]] = mapped_column(Numeric)
    wind_speed: Mapped[Optional[float]] = mapped_column(Numeric)
    wind_direction: Mapped[Optional[float]] = mapped_column(Numeric)
    wind_gust: Mapped[Optional[float]] = mapped_column(Numeric)
    
    def __repr__(self) -> str:
        return f"<WeatherData(site_code='{self.site_code}', date_time='{self.date_time}')>"

class SnotelData(Base):
    __tablename__ = 'snotel'
    
    site_code: Mapped[str] = mapped_column(String(15), primary_key=True)
    date_time: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), primary_key=True)
    air_temp: Mapped[Optional[float]] = mapped_column(Numeric)
    snow_depth: Mapped[Optional[float]] = mapped_column(Numeric)
    swe: Mapped[Optional[float]] = mapped_column(Numeric)
    site_name: Mapped[Optional[str]] = mapped_column(Text)
    
    def __repr__(self) -> str:
        return f"<SnotelData(site_code='{self.site_code}', date_time='{self.date_time}', site_name='{self.site_name}')>"