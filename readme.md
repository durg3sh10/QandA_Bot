# AI Agent for PDF Question Answering

In this project, I have created an AI agent that extracts text from a PDF document, finds the most relevant chunks for a set of questions using embeddings, and queries the OpenAI API (chat-gpt-3.5-turbo) to generate answers and post the QA on slack using slackapi. 

## Features

- Extracts text from PDF documents.
- Splits the text into manageable chunks.
- Uses embeddings to find the most relevant chunk for each question.
- Queries the OpenAI API for answers.
- Posts results to a specified Slack channel.

## Requirements
- A req.txt file is provided for the requirements


## Sample Input and Output
- Input: python main.py --pdf_path D:\Zania_AI\handbook.pdf

- Output:
Question: What is the name of the company?
 Answer: The name of the company is Zania, Inc.
Question: Who is the CEO of the company?
 Answer: The CEO of Zania, Inc. is Shruti Gupta.
Question: What is their vacation policy?
 Answer: Zania, Inc. provides its employees with paid vacation time based on their length of service. Full-time regular employees are eligible for vacation time immediately upon hire/upon completion of the introductory period/after completing a certain number of days of employment. Vacation time is calculated according to the employee's work anniversary year/the calendar year/the fiscal year. The amount of vacation received each year is based on the length of service and is granted in a lump sum at the beginning of each year or accrues according to
Question: What is the termination policy?
 Answer: The termination policy at Zania, Inc. states that your employment with the company is on an "at-will" basis, meaning that your employment may be terminated at any time, with or without notice and with or without cause. The policy emphasizes that the company respects your right to leave the company at any time, with or without notice and with or without cause.

It is also mentioned that nothing in the company handbook or any other document should be understood as creating a contract for guaranteed or continued employment


Slack Post:
![image](https://github.com/durg3sh10/QandA_Bot/assets/79005878/2e44d764-b721-4b0f-bb3a-3a1ff2a98413)

