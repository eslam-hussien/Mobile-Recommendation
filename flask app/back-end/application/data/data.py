mapping = {
    1: {'nppi': 1, 'cpu_score': 0.2, 'nram': 0.2},
    2: {'nbattery_endurance_time': 1, 'nppi': 0.8},
    3: {'nstorage_size': 0.8, 'nbattery_endurance_time': 1, 'cpu_score': 1, 'nram': 1, 'nppi': 0.7},
    4: {'make': 1},
    5: {'cpu_score': 0.3, 'nbattery_endurance_time': 0.8, 'nram': 0.3,
        'nstorage_size': 0.3},
    6: {'nbattery_endurance_time': 0.8, 'nram': 0.3, 'nppi': 0.1},
    7: {'nstorage_size': 1, 'nmain_camera': 1},
    8: {'nstorage_size': 1, 'nbattery_endurance_time': 0.4, 'cpu_score': 0.5},
    9: {'nthickness': 0.4, 'nedge': 0.6},
    10: {'nstorage_size': 1, 'nppi': 0.8, 'nbattery_endurance_time': 1},
    11: {'nstorage_size': 0.8, 'selfie': 1},
    12: {'nbattery_endurance_time': 1},
    13: {'nbattery_endurance_time': 0.3, 'nppi': 0.4}
}

interests_readable = [
    {"id": 1,  "name": "ease of typing"},
    {"id": 2,  "name": "battery life"},
    {"id": 3,  "name": "gaming"},
    {"id": 4,  "name": "barnd"},
    {"id": 5,  "name": "apps"},
    {"id": 6,  "name": "browsing"},
    {"id": 7,  "name": "photography"},
    {"id": 8,  "name": "Storing and reading books and files"},
    {"id": 9,  "name": "Styling"},
    {"id": 10,  "name": "Run media files locally"},
    {"id": 11,  "name": "selfie"},
    {"id": 12,  "name": "Mobile Network Phone calls"},
    {"id": 13,  "name": "SMS Text"}
]

levels_weights = [(1, 5), (2, 3), (3, 1)]
