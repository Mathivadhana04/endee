from endee_client import insert_document

def load_data():
    with open("data/sample_docs.txt", "r", encoding="utf-8") as f:
        content = f.read()

    # Split into chunks (simple split by line)
    docs = content.split("\n")

    for doc in docs:
        if doc.strip():
            insert_document(doc)

    print("✅ Data loaded into Endee!")

if __name__ == "__main__":
    load_data()