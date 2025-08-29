from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Your details
FULL_NAME = "naman_boob"
DOB = "23082004"   # ddmmyyyy
EMAIL = "naman.22bcb7094@vitapstudent.ac.in"
ROLL_NUMBER = "22BCB7094"

class InputData(BaseModel):
    data: List[str]

def process_data(data: List[str]):
    odd_numbers = []
    even_numbers = []
    alphabets = []
    special_chars = []
    total_sum = 0

    for item in data:
        if item.isdigit():  # numbers
            num = int(item)
            if num % 2 == 0:
                even_numbers.append(item)
            else:
                odd_numbers.append(item)
            total_sum += num
        elif item.isalpha():  # alphabets
            alphabets.append(item.upper())
        else:  # special characters
            special_chars.append(item)

    # Concatenation of alphabets in reverse order with alternating caps
    letters = "".join([a for a in data if a.isalpha()])[::-1]
    concat_str = ""
    for i, ch in enumerate(letters):
        concat_str += ch.upper() if i % 2 == 0 else ch.lower()

    return {
        "is_success": True,
        "user_id": f"{FULL_NAME.lower()}_{DOB}",
        "email": EMAIL,
        "roll_number": ROLL_NUMBER,
        "odd_numbers": odd_numbers,
        "even_numbers": even_numbers,
        "alphabets": alphabets,
        "special_characters": special_chars,
        "sum": str(total_sum),
        "concat_string": concat_str
    }

@app.post("/bfhl")
async def bfhl(input_data: InputData):
    try:
        response = process_data(input_data.data)
        return response
    except Exception as e:
        return {"is_success": False, "error": str(e)}
