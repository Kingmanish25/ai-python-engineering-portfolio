import torch
from transformers import BertForSequenceClassification, BertTokenizer


class SentimentPredictor:
    def __init__(self, model_path="models/bert_sentiment"):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        self.tokenizer = BertTokenizer.from_pretrained(model_path)
        self.model = BertForSequenceClassification.from_pretrained(model_path)

        self.model.to(self.device)
        self.model.eval()

        self.label_map = {
            0: "Negative",
            1: "Positive"
        }

    def predict(self, text):
        encoding = self.tokenizer(
            text,
            return_tensors="pt",
            truncation=True,
            padding=True,
            max_length=128
        )

        input_ids = encoding["input_ids"].to(self.device)
        attention_mask = encoding["attention_mask"].to(self.device)

        with torch.no_grad():
            outputs = self.model(input_ids=input_ids, attention_mask=attention_mask)

        probs = torch.softmax(outputs.logits, dim=1)

        pred = torch.argmax(probs, dim=1).item()
        confidence = torch.max(probs).item()

        return self.label_map[pred], confidence, probs.cpu().numpy()[0]
