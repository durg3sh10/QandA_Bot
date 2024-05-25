import openai
import os
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
from embeddings import get_embeddings

from key import openaikey  
load_dotenv()

os.environ["OPENAI_API_KEY"]=openaikey
openai.api_key = os.getenv("OPENAI_API_KEY")

def find_most_relevant_chunk(chunks, question_embedding):
    chunk_embeddings = get_embeddings(chunks)
    similarities = cosine_similarity([question_embedding], chunk_embeddings)
    most_relevant_index = similarities.argmax()
    return chunks[most_relevant_index]

def get_answers(chunks, questions):
    answers = {}
    question_embeddings = get_embeddings(questions)
    for question, question_embedding in zip(questions, question_embeddings):
        relevant_chunk = find_most_relevant_chunk(chunks, question_embedding)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Based on the following text:\n{relevant_chunk}\nAnswer the question: {question}"}
            ],
            max_tokens=100
        )
        answer = response['choices'][0]['message']['content'].strip()
        answers[question] = answer if answer else "Data Not Available"
    return answers
