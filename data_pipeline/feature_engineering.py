# Feature extraction from logs
def extract_features(logs):
    features = []
    for log in logs:
        features.append({
            'user_id': log.get('user'),
            'action_count': len(log.get('actions', []))
        })
    return features
