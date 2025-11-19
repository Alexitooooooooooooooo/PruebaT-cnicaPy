data = [
    {'username': 'alice_dev', 'score': 92, 'is_active': True},
    {'username': 'bob_qa', 'score': 78, 'is_active': False},
    {'username': 'charlie_pm', 'score': 85, 'is_active': True},
    {'username': 'david_analyst', 'score': 95, 'is_active': False},
    {'username': 'eve_eng', 'score': 88, 'is_active': True},
]

usernames_filtrados = [user['username'] for user in data if user['is_active'] and user['score'] >= 85]
print(usernames_filtrados)


##Con lambda
data_filtrada = filter(lambda user: user['is_active'] and user['score'] >= 85, data)
usernames_filtrados = list(map(lambda user: user['username'], data_filtrada))
print(usernames_filtrados)