import time

class RateLimiter:
    def __init__(self, max_tokens, refill_rate):
        # max_tokens: bucket capacity
        # refill_rate: tokens added per second
        # clients: dictionary to track each IP
        self.max_tokens = max_tokens
        self.refill_rate = refill_rate
        self.clients = {}

    def is_allowed(self, client_ip):
        # 1. Get current time
        current_time = time.time()

        # 2. If client not seen before, give them a full bucket
        if client_ip not in self.clients:
            self.clients[client_ip] = {
                "tokens": self.max_tokens,
                "last_request_time": current_time
            }

        # 3. Calculate tokens to add based on time elapsed
        client_data = self.clients[client_ip]
        elapsed_time = current_time - client_data["last_request_time"]

        # 4. Add tokens but don't exceed max_tokens
        client_data["tokens"] = min(
            self.max_tokens,
            client_data["tokens"] + elapsed_time * self.refill_rate
        )

        client_data["last_request_time"] = current_time

        # 5. If tokens > 0, consume one and return True
        if client_data["tokens"] > 0:
            client_data["tokens"] -= 1
            return True
        return False
