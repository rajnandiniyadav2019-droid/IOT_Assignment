prices = [105, 110, 108, 112, 115, 116, 114]

for i in range(len(prices) - 2):
    avg = sum(prices[i:i+3]) / 3
    print(f"Days {i+1}-{i+3}: {avg:.2f}")
