"""
As principais ideias para resolução deste problema são:
    1. Converter os horários para minutos desde a meia-noite, facilitando os cálculos.
    2. Ordenar os compromissos e adicionar os limites do expediente (10 as 18)
    3. Calcular os intervalos livres entre compromissos e identificar o maior.

Um código que peguei de inspiração e de onde tirei a ideia de converter tudo para minutos foi do:
    https://github.com/morris821028/UVa/blob/master/volume101/10191%20-%20Longest%20Nap.cpp
"""

def parse_time(time_str):
    # Converte uma string de horário (HH:MM) para minutos desde a meia-noite.
    hours, minutes = map(int, time_str.split(":"))
    return hours * 60 + minutes

def format_time(minutes):
    # Converte minutos desde a meia-noite para uma string de horário (HH:MM).
    # O :02 é para formatar com 2 numeros, tanto horas quanto minutos
    return f"{minutes // 60:02}:{minutes % 60:02}"

def find_longest_nap(schedule):
    # Encontra o maior intervalo de tempo livre (cochilo mais longo) na agenda diária.
    start_time = parse_time("10:00")
    end_time = parse_time("18:00")
    
    # Ordena considerando primeira posição de uma tupla, se houver empate usa a segunda
    schedule = sorted(schedule)
    schedule = [(start_time, start_time)] + schedule + [(end_time, end_time)]

    max_nap = 0
    nap_start = start_time
    for i in range(1, len(schedule)):
        prev_end = schedule[i - 1][1] # Fim do compromisso anterior
        curr_start = schedule[i][0] # Inicio do proximo compromisso
        nap_duration = curr_start - prev_end # Duração do intervalo livre (cochilo)
        if nap_duration > max_nap: # Novo maior cochilo
            max_nap = nap_duration
            nap_start = prev_end

    return nap_start, max_nap

def process_file(file_path):
    # Processa o arquivo de entrada e calcula o cochilo mais longo para cada dia
    with open(file_path, 'r') as file:
        lines = file.readlines()

    results = []
    i = 0
    while i < len(lines):
        n = int(lines[i].strip()) # numero de compromisso dos dias 
        i += 1

        schedule = []
        # Le os compromissos do dia atual
        for _ in range(n):
            time_range, description = lines[i].split(maxsplit=2)[:2], lines[i].split(maxsplit=2)[2]
            start_time = parse_time(time_range[0])
            end_time = parse_time(time_range[1])
            schedule.append((start_time, end_time))
            i += 1
        
        # Calcula maior cochilo do dia
        nap_start, nap_duration = find_longest_nap(schedule)
        
        # Formata o resultado
        nap_start_formatted = format_time(nap_start)
        if nap_duration >= 60:
            nap_hours = nap_duration // 60
            nap_minutes = nap_duration % 60
            results.append(f"Day #{len(results) + 1}: the longest nap starts at {nap_start_formatted} and will last for {nap_hours} hours and {nap_minutes} minutes.")
        else:
            results.append(f"Day #{len(results) + 1}: the longest nap starts at {nap_start_formatted} and will last for {nap_duration} minutes.")

    return results

def main():
    input_file = "input.txt"
    results = process_file(input_file)
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
