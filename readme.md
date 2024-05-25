# AI Agent for PDF Question Answering

This project creates an AI agent that extracts text from a PDF document, finds the most relevant chunks for a set of questions using embeddings, and queries the OpenAI API to generate answers. 

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

- Output: {'What is the name of the company?': 'The name of the company is Zania, Inc.', 'Who is the CEO of the company?': 'The CEO of Zania, Inc. is Shruti Gupta.', 'What is their vacation policy?': 'Zania, Inc. provides employees with paid vacation. All full-time regular employees are eligible to receive vacation time immediately upon hire. Vacation time is calculated according to the work anniversary year. There are two options for vacation accrual:\n\nOption 1: The amount of vacation received each year is based on the length of service and is either granted in a lump sum at the beginning of each year or accrues according to a schedule determined by the Company, with different amounts based on years of employment.\n\nOption', 'What is the termination policy?': 'The termination policy at Zania, Inc. is based on the "at-will" employment basis. This means that your employment may be terminated at any time, with or without notice and with or without cause. The company reserves the right to interpret, modify, or supplement the provisions of the handbook at any time. Only the CEO has the authority to make promises or negotiate with regard to guaranteed or continued employment, and any such promises are only effective if placed in writing and signed by the CEO.'}
