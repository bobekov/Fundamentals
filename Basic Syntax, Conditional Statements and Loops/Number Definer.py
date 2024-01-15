num = float(input())
result = None

if num > 0:
    if num < 1:
        result = 'small positive'
    elif num < 1000000:
        result = 'positive'
    else:
        result = 'large positive'
elif num < 0:
    if abs(num) < 1:
        result = 'small negative'
    elif abs(num) < 1000000:
        result = 'negative'
    else:
        result = 'large negative'
else:
    result = 'zero'

print(result)