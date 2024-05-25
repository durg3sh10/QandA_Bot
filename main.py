import argparse
from pdf_reader import extract_text_from_pdf
from question_answering import get_answers
from slack_post import post_results_on_slack


def main(pdf_path, questions, slack_channel):
    chunks = extract_text_from_pdf(pdf_path)
    answers = get_answers(chunks, questions)
    post_results_on_slack(slack_channel, answers)

if __name__ == "__main__":

    questions = [
        "What is the name of the company?",
        "Who is the CEO of the company?",
        "What is their vacation policy?",
        "What is the termination policy?"
    ]
    slack_channel = "#general"


    parser = argparse.ArgumentParser(description='Process a PDF and answer questions based on its content.')
    parser.add_argument('--pdf_path', type=str, help='Path to the PDF file')
    args = parser.parse_args()

    main(args.pdf_path, questions, slack_channel)
 