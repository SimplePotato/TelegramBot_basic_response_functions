from datetime import datetime

def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello", "hi", "sup'"):
        return "kwa'j dej?"

    if user_message in ("lalala", "Na Horuk", "zavriskaj"):
        return "jah bo kar bo"

    if user_message in ("ura", "ura?", "cajt"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")

        return str(date_time)

    return "kuga? Ne vem kaj bi odgovoril"    