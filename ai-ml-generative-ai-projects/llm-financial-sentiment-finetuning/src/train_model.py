import torch
from torch.utils.data import DataLoader
from transformers import BertForSequenceClassification, AdamW, get_scheduler
from dataset_loader import load_data, FinancialDataset
from tokenizer import get_tokenizer
from tqdm import tqdm
import os


def train():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    tokenizer = get_tokenizer()

    train_texts, val_texts, train_labels, val_labels = load_data("data/data.csv")

    train_dataset = FinancialDataset(train_texts, train_labels, tokenizer)
    val_dataset = FinancialDataset(val_texts, val_labels, tokenizer)

    train_loader = DataLoader(train_dataset, batch_size=16, shuffle=True)

    model = BertForSequenceClassification.from_pretrained(
        "bert-base-uncased",
        num_labels=2
    )

    model.to(device)

    optimizer = AdamW(model.parameters(), lr=2e-5)

    num_epochs = 3
    total_steps = len(train_loader) * num_epochs

    scheduler = get_scheduler(
        "linear",
        optimizer=optimizer,
        num_training_steps=total_steps,
        num_warmup_steps=0
    )

    for epoch in range(num_epochs):
        model.train()
        total_loss = 0

        loop = tqdm(train_loader)

        for batch in loop:
            optimizer.zero_grad()

            input_ids = batch["input_ids"].to(device)
            attention_mask = batch["attention_mask"].to(device)
            labels = batch["label"].to(device)

            outputs = model(
                input_ids=input_ids,
                attention_mask=attention_mask,
                labels=labels
            )

            loss = outputs.loss
            total_loss += loss.item()

            loss.backward()
            optimizer.step()
            scheduler.step()

            loop.set_description(f"Epoch {epoch}")
            loop.set_postfix(loss=loss.item())

        print(f"Epoch {epoch} Loss: {total_loss / len(train_loader)}")

    os.makedirs("models", exist_ok=True)
    model.save_pretrained("models/bert_sentiment")
    tokenizer.save_pretrained("models/bert_sentiment")

    print("✅ Model saved successfully!")


if __name__ == "__main__":
    train()
