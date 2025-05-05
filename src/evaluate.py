import csv
import os

def save_results_to_csv(results, filepath="qa_results.csv"):
    file_exists = os.path.exists(filepath)

    with open(filepath, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Write header only if file is new
        if not file_exists or os.path.getsize(filepath) == 0:
            writer.writerow(["Question", "Prompt Type", "Response"])

        for prompt_type, qas in results.items():
            for question, answer in qas.items():
                writer.writerow([question, prompt_type, answer])
