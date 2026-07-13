def format_filter(number, frequency, gain):
    string = f"Filter  {number}: ON  PK       Fc     {frequency} Hz   Gain  {gain} dB  Q 4.32"
    return string

def format_preamp(preamp):
    string = f"Preamp: {preamp} dB"
    return string

def generate_config(gains):
    frequency = [20, 25, 32, 40, 50, 63, 80, 100, 125, 160, 200, 250, 315, 400, 500, 630, 800, 1000, 1250, 1600, 2000, 2500, 3150, 4000, 5000, 6300, 8000, 10000, 12500, 16000, 20000]
    for i in range(31):
        format_filter(i+1, frequency[i], gains)

with open("preset.txt", "w", encoding="utf-8") as file:
    file.write("Filter  " , number ,": ON  PK       Fc     " , frequency ,"Hz   Gain  " , gain, " dB  Q 4.32")