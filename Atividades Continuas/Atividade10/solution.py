import heapq

def convert_time(tstr):
    # Converte uma string no formato HHMM para minutos (inteiro)
    hours = int(tstr[:2])
    minutes = int(tstr[2:])
    return hours * 60 + minutes

def format_time(minutes):
    # Converte minutos para string no formato HHMM com zeros à esquerda se necessário
    h = minutes // 60
    m = minutes % 60
    return f"{h:02d}{m:02d}"

def solve_railroads(test_cases):
    results = []
    scenario_num = 1
    # Processa cada caso de teste
    for cities, schedules, start_time_str, source, destination in test_cases:
        # Constrói um dicionário com as conexões (arestas) de cada cidade
        # Cada conexão é representada como: (horário de partida, horário de chegada, cidade destino)
        outgoing = {city: [] for city in cities}
        for schedule in schedules:
            # Para cada horário, cria as conexões entre paradas consecutivas
            for i in range(len(schedule) - 1):
                dep_time, from_city = schedule[i]
                arr_time, to_city = schedule[i+1]
                # Só adiciona a conexão se o horário de chegada for igual ou superior ao de partida
                if arr_time >= dep_time:
                    outgoing[from_city].append((dep_time, arr_time, to_city))
        
        start_time = convert_time(start_time_str)
        # best: para cada cidade, guarda (melhor horário de chegada, horário da primeira partida usada)
        best = {city: (float('inf'), None) for city in cities}
        best[source] = (start_time, None)
        
        # Heap para estados, cada estado é (horário_atual, cidade, primeiro_horário_de_partida)
        heap = []
        heapq.heappush(heap, (start_time, source, None))
        
        while heap:
            cur_time, city, first_dep = heapq.heappop(heap)
            # Se o estado atual não é o melhor conhecido para a cidade, ignora-o
            if cur_time != best[city][0]:
                continue
            # Se chegamos ao destino, podemos interromper a busca
            if city == destination:
                break
            # Para cada conexão saindo da cidade atual
            for dep, arr, nxt in outgoing[city]:
                # Só pode pegar o trem se o horário de partida for maior ou igual ao horário atual
                if dep >= cur_time:
                    # Se ainda não pegamos um trem, define a primeira partida como o horário deste trem
                    new_first_dep = first_dep if first_dep is not None else dep
                    # Se a chegada pela conexão atual melhora o horário registrado para a cidade de destino
                    if arr < best[nxt][0]:
                        best[nxt] = (arr, new_first_dep)
                        heapq.heappush(heap, (arr, nxt, new_first_dep))
        
        # Monta a saída conforme o caso: se não houve conexão, imprime "No connection"
        if best[destination][0] == float('inf'):
            result = f"Scenario {scenario_num}\nNo connection"
        else:
            dep_time_str = format_time(best[destination][1])
            arr_time_str = format_time(best[destination][0])
            result = f"Scenario {scenario_num}\nDeparture {dep_time_str} {source}\nArrival {arr_time_str} {destination}"
        results.append(result)
        scenario_num += 1
    return results

def main():
    # Lê o arquivo "input.txt" e extrai as linhas não vazias
    with open("input.txt", "r") as f:
        lines = [line.strip() for line in f if line.strip() != ""]
    
    test_cases = []
    index = 0
    t = int(lines[index])  # Número de casos de teste
    index += 1
    for _ in range(t):
        # Lê o número de cidades e os nomes das cidades
        n = int(lines[index])
        index += 1
        cities = []
        for _ in range(n):
            cities.append(lines[index])
            index += 1
        # Lê o número de horários (schedules)
        m = int(lines[index])
        index += 1
        schedules = []
        for _ in range(m):
            k = int(lines[index])  # Número de paradas neste schedule
            index += 1
            schedule = []
            for _ in range(k):
                parts = lines[index].split()
                time_str = parts[0]
                city_name = " ".join(parts[1:])  # Caso o nome da cidade contenha espaços
                schedule.append((convert_time(time_str), city_name))
                index += 1
            schedules.append(schedule)
        # Lê o horário de partida, a cidade de origem e a cidade de destino
        start_time_str = lines[index]
        index += 1
        source = lines[index]
        index += 1
        destination = lines[index]
        index += 1
        test_cases.append((cities, schedules, start_time_str, source, destination))
    
    results = solve_railroads(test_cases)
    for res in results:
        print(res)
        print()

if __name__ == "__main__":
    main()
