class RecoveryAgent:

    def __init__(
        self,
        customer_id,
        risk_score,
        recovery_probability,
        expected_recovery
    ):
        self.customer_id = customer_id
        self.risk_score = float(risk_score)
        self.recovery_probability = float(recovery_probability)
        self.expected_recovery = float(expected_recovery)

        self.attempts = 0
        self.previous_actions = []
        self.memory = []
        self.recovered = False
        self.status = "AT_RISK"
        self.max_attempts = 3

    def observe(self):
        return {
            "customer_id": self.customer_id,
            "risk_score": self.risk_score,
            "recovery_probability": self.recovery_probability,
            "expected_recovery": self.expected_recovery,
            "attempts": self.attempts,
            "previous_actions": self.previous_actions.copy(),
            "status": self.status
        }

    def analyze_customer(self):

        if self.risk_score >= 70:
            risk_level = "HIGH"
        elif self.risk_score >= 40:
            risk_level = "MEDIUM"
        else:
            risk_level = "LOW"

        if self.recovery_probability >= 70:
            recovery_strength = "HIGH"
        elif self.recovery_probability >= 50:
            recovery_strength = "MEDIUM"
        else:
            recovery_strength = "LOW"

        return {
            "risk_level": risk_level,
            "recovery_strength": recovery_strength,
            "risk_score": self.risk_score,
            "recovery_probability": self.recovery_probability,
            "expected_recovery": self.expected_recovery
        }

    def decide(self):

        if self.recovered or self.attempts >= self.max_attempts:
            return "STOP"

        if self.risk_score >= 80:
            action = "Payment Recovery Link"
        elif self.recovery_probability >= 60:
            action = "SMS Reminder"
        else:
            action = "Email Reminder"

        if action in self.previous_actions:
            for alternative in [
                "Payment Recovery Link",
                "SMS Reminder",
                "Email Reminder"
            ]:
                if alternative not in self.previous_actions:
                    return alternative

            return "STOP"

        return action

    def get_reason(self, action=None):

        if action is None:
            action = self.decide()

        analysis = self.analyze_customer()

        return (
            f"Customer has {analysis['risk_level']} risk with "
            f"{self.recovery_probability:.1f}% recovery probability. "
            f"The AI agent selected {action} as the next recovery action."
        )

    def guardrail_check(self, action):

        if action == "STOP":
            return True, "No further recovery action required."

        if self.attempts >= self.max_attempts:
            return False, "Maximum recovery attempts reached."

        if (
            action == "Payment Recovery Link"
            and self.risk_score >= 90
        ):
            return False, "Human approval required for high-risk action."

        if action in self.previous_actions:
            return False, "Action already attempted."

        return True, "Action approved by AI guardrails."

    def act(self, action):

        if action == "STOP":
            self.status = "STOPPED"

            result = {
                "action": "STOP",
                "result": "STOPPED",
                "message": "Recovery stopped."
            }

            self.memory.append(result)
            return result

        allowed, message = self.guardrail_check(action)

        if not allowed:
            self.status = "WAITING_FOR_APPROVAL"

            result = {
                "action": action,
                "result": "BLOCKED",
                "message": message
            }

            self.memory.append(result)
            return result

        self.attempts += 1
        self.previous_actions.append(action)

        success = self.simulate_result(action)

        if success:
            self.recovered = True
            self.status = "RECOVERED"

            result = {
                "action": action,
                "result": "SUCCESS",
                "message": (
                    f"Recovery successful. "
                    f"Revenue recovered: "
                    f"£{self.expected_recovery:,.2f}"
                )
            }

        else:
            self.status = "RECOVERY_ATTEMPT_FAILED"

            result = {
                "action": action,
                "result": "FAILED",
                "message": "Recovery attempt unsuccessful."
            }

        self.memory.append(result)
        return result

    def simulate_result(self, action):

        if action == "SMS Reminder":
            return self.recovery_probability >= 50

        if action == "Payment Recovery Link":
            return self.recovery_probability >= 65

        if action == "Email Reminder":
            return self.recovery_probability >= 70

        return False

    def learn(self, result):

        if result["result"] == "SUCCESS":
            self.recovered = True
            self.status = "RECOVERED"

        elif result["result"] == "FAILED":
            self.status = "READY_FOR_NEXT_ACTION"

        elif result["result"] == "BLOCKED":
            self.status = "WAITING_FOR_APPROVAL"

        elif result["result"] == "STOPPED":
            self.status = "STOPPED"

    