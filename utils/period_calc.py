from datetime import datetime, timedelta


def calculate_cycle(last_period_date: datetime, cycle_length: int = 28):
    next_period = last_period_date + timedelta(days=cycle_length)
    ovulation = last_period_date + timedelta(days=cycle_length - 14)
    fertile_start = ovulation - timedelta(days=5)
    fertile_end = ovulation + timedelta(days=1)
    pms_start = next_period - timedelta(days=7)
    today = datetime.now()
    days_until_next = (next_period - today).days

    return {
        "next_period": next_period,
        "ovulation": ovulation,
        "fertile_start": fertile_start,
        "fertile_end": fertile_end,
        "pms_start": pms_start,
        "days_until_next": max(0, days_until_next),
        "cycle_day": (today - last_period_date).days + 1,
    }


def get_cycle_phase(cycle_day: int, cycle_length: int = 28):
    if cycle_day <= 5:
        return (
            "🩸 Menstrual Phase",
            "#e74c8b",
            "Rest, hydrate, use heating pad for cramps",
        )
    elif cycle_day <= 13:
        return (
            "🌱 Follicular Phase",
            "#7C3AED",
            "Energy is rising! Great time to start new projects",
        )
    elif cycle_day <= 16:
        return (
            "🌟 Ovulation Phase",
            "#f59e0b",
            "Peak energy & confidence. Best time for important tasks",
        )
    else:
        return "🌙 Luteal Phase", "#6366f1", "Take it slow. Self-care is important now"
