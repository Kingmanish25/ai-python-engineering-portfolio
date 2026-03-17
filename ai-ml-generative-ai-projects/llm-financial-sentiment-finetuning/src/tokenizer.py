from transformers import BertTokenizer


def get_tokenizer():
    return BertTokenizer.from_pretrained("bert-base-uncased")
