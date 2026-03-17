class ChatMemory:
    def __init__(self):
        self.history = []

    def add(self, user, response):
        self.history.append({"user": user, "response": response})

    def get_context(self):
        context = ""
        for h in self.history[-3:]:
            context += f"User: {h['user']}\nAssistant: {h['response']}\n"
        return context
