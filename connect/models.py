from sqlmodel import Field , SQLModel

class Survey(SQLModel, table=True):
	id: int | None = Field(default=None, primary_key=True)
	name: str
	bloodtype: str
	diabetic: str
	std: str
	drink: str
	date: str
	blood: str
	anemia: str
	open: str
	permission: str


