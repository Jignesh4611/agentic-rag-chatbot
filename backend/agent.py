import re
from rag import answer_question


def is_math_question(text: str) -> bool:
    return bool(re.fullmatch(r"[0-9+\-*/(). ]+", text))

def calculator_tool(expression: str) -> str:
    try:
        if not re.match(r"^[0-9+\-*/(). ]+$", expression):
            return "Invalid Expression"
        return str(eval(expression))
    except:
        return "Calculation error"
def rag_tool(question: str) -> str:
    answer, _ = answer_question(question)
    return answer


def run_agent(question: str) -> str:
    question = question.strip()

    if is_math_question(question):
        return calculator_tool(question)

    return rag_tool(question)
