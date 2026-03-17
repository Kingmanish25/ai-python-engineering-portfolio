import pandas as pd
from sklearn.model_selection import train_test_split
import torch
from torch.utils.data import Dataset


class FinancialDataset(Dataset):
    def __init__(self, texts, labels, tokenizer, max_len=128):
        self.texts = texts
        self.labels = labels
        self.tokenizer = tokenizer
        self.max_len = max_len

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, idx):
        text = str(self.texts[idx])
        label = int(self.labels[idx])

        encoding = self.tokenizer(
            text,
            truncation=True,
            padding="max_length",
            max_length=self.max_len,
            return_tensors="pt"
        )

        return {
            "input_ids": encoding["input_ids"].flatten(),
            "attention_mask": encoding["attention_mask"].flatten(),
            "label": torch.tensor(label, dtype=torch.long)
        }


def load_data(path):
    df = pd.read_csv(path)

    df = df[["text", "sentiment"]].dropna()
    df["sentiment"] = df["sentiment"].astype(int)

    train_texts, val_texts, train_labels, val_labels = train_test_split(
        df["text"].tolist(),
        df["sentiment"].tolist(),
        test_size=0.2,
        random_state=42,
        stratify=df["sentiment"]
    )

    return train_texts, val_texts, train_labels, val_labels
