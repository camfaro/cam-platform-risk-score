# risk_score.py

class RiskScore:
    def __init__(self, transparency, complaints, upsells, payment_issues):
        self.transparency = transparency
        self.complaints = complaints
        self.upsells = upsells
        self.payment_issues = payment_issues

    def calculate_score(self):
        score = 100

        score -= (10 - self.transparency) * 3
        score -= self.complaints * 5
        score -= self.upsells * 4
        score -= self.payment_issues * 6

        return max(score, 0)


if __name__ == "__main__":
    platform = RiskScore(
        transparency=6,
        complaints=3,
        upsells=4,
        payment_issues=2
    )

    print("Risk Score:", platform.calculate_score())
