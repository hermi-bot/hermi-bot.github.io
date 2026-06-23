import json
try:
    with open('dd_results.json', 'r') as f:
        data = json.load(f)
    results = data.get('results', [])
    for i, res in enumerate(results[:5]):
        print(f'{i+1}. {res.get("title")}')
        print(f'   Source: {res.get("href")}')
        print(f'   Snippet: {res.get("abstract")}')
        print()
except Exception as e:
    print(f'Error: {e}')
