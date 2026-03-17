import torch
from torch.utils.data import DataLoader
from transformers import BertForSequenceClassification
from dataset_loader import load_data, FinancialDataset
from tokenizer import get_tokenizer
from sklearn.metrics import classification_report


def evaluate():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    tokenizer = get_tokenizer()

    _, val_texts, _, val_labels = load_data("data/data.csv")

    val_dataset = FinancialDataset(val_texts, val_labels, tokenizer)
    val_loader = DataLoader(val_dataset, batch_size=16)

    model = BertForSequenceClassification.from_pretrained("models/bert_sentiment")
    model.to(device)
    model.eval()

    preds, actual = [], []

    with torch.no_grad():
        for batch in val_loader:
            input_ids = batch["input_ids"].to(device)
            attention_mask = batch["attention_mask"].to(device)

            outputs = model(input_ids=input_ids, attention_mask=attention_mask)
            predictions = torch.argmax(outputs.logits, dim=1)

            preds.extend(predictions.cpu().numpy())
            actual.extend(batch["label"].numpy())

    print(classification_report(actual, preds))


if __name__ == "__main__":
    evaluate()
