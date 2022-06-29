from pydantic import BaseModel, validator


class BankCodeModel(BaseModel):
    bank_code: int

    @validator("bank_code")
    def validate_bank_code(cls, bank_code):
        if bank_code < 0:
            raise ValueError()
        return bank_code
