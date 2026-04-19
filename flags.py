# flags.py

def detect_risk_flags(platform_data):
    flags = []

    if platform_data.get("hidden_prices"):
        flags.append("Possível falta de transparência")

    if platform_data.get("fake_profiles"):
        flags.append("Perfis suspeitos")

    if platform_data.get("aggressive_upsells"):
        flags.append("Upsells agressivos")

    if platform_data.get("payment_issues"):
        flags.append("Problemas de pagamento")

    return flags


if __name__ == "__main__":
    sample = {
        "hidden_prices": True,
        "fake_profiles": False,
        "aggressive_upsells": True,
        "payment_issues": False
    }

    print(detect_risk_flags(sample))
