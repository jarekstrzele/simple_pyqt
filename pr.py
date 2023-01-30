from collections import defaultdict

senders = defaultdict(int)
receivers = defaultdict(int)

with open('email-Eu-core.txt', 'r') as f:
    for line in f:
        sender, receiver = map(int, line.strip().split())
        
        senders[sender] += 1
        receivers[receiver] += 1

num_vertices = len(set(senders.keys()).union(receivers.keys()))
print(f"Liczba wierzchołków: {num_vertices}")

num_edges = sum(senders.values())
print(f"Liczba połączeń: {num_edges}")

max_sender = max(senders, key=senders.get)
print(f"Największa wysłana liczba maili przez jedną osobę: {senders[max_sender]}")

max_mail = max(senders, key=senders.get)
print(f"Osoba o największej ilości wysłanych maili: {max_mail}")

max_receiver = max(receivers, key=receivers.get)
print(f"{receivers[max_receiver]} maili zostało wysłanych do osoby {max_receiver}")